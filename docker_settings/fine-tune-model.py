
import os
import evaluate
import numpy as np
import torch
from datasets import load_dataset
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from torchvision.transforms import (
    CenterCrop,
    Compose,
    Lambda,
    Normalize,
    RandomHorizontalFlip,
    RandomResizedCrop,
    Resize,
    ToTensor,
)

from transformers import (
    MODEL_FOR_IMAGE_CLASSIFICATION_MAPPING,
    AutoConfig,
    AutoImageProcessor,
    AutoModelForImageClassification,
    TimmWrapperImageProcessor,
    Trainer,
    TrainingArguments,
    set_seed,
)
# from transformers.trainer_utils import get_last_checkpoint
# from transformers.utils import check_min_version


# check_min_version("4.52.0.dev0")

MODEL_CONFIG_CLASSES = list(MODEL_FOR_IMAGE_CLASSIFICATION_MAPPING.keys())
MODEL_TYPES = tuple(conf.model_type for conf in MODEL_CONFIG_CLASSES)


def pil_loader(path: str):
    with open(path, "rb") as f:
        im = Image.open(f)
        return im.convert("RGB")

def main():
    
    output_dir = "./model/"
    train_dir = "./database"
    seed: int = 42
    train_val_split = 0.15
    model_name_or_path = "google/vit-base-patch16-224-in21k"

    if not os.path.exists(output_dir) :
        os.makedirs(output_dir)

    trainer_args = TrainingArguments()
    trainer_args.train_dir = train_dir
    trainer_args.do_eval = True
    trainer_args.do_train = True
    trainer_args.output_dir = "./model/"
    trainer_args.remove_unused_columns = False
    trainer_args.run_name = "./model/"

    # Detecting last checkpoint.
    # last_checkpoint = None
    # last_checkpoint = get_last_checkpoint(output_dir)
    # if last_checkpoint is None and len(os.listdir(output_dir)) > 0: exit()

    # Set seed before initializing model.
    set_seed(seed)

    # Initialize our dataset and prepare it for the 'image-classification' task.
   
    data_files = {}
    if train_dir is not None:
        data_files["train"] = os.path.join(train_dir, "**")
    # if validation_dir is not None:
    #     data_files["validation"] = os.path.join(validation_dir, "**")
    dataset = load_dataset(
        "imagefolder",
        data_files=data_files,
        cache_dir=None,
    )


    # What does this do?
    def collate_fn(examples):
        pixel_values = torch.stack([example["pixel_values"] for example in examples])
        labels = torch.tensor([example["label"] for example in examples])
        return {"pixel_values": pixel_values, "labels": labels}

    
    # split training and validation data
    split = dataset["train"].train_test_split(train_val_split)
    dataset["train"] = split["train"]
    dataset["validation"] = split["test"]

    # Prepare label mappings.
    # We'll include these in the model's config to get human readable labels in the Inference API.
    labels = dataset["train"].features["label"].names
    label2id, id2label = {}, {}
    for i, label in enumerate(labels):
        label2id[label] = str(i)
        id2label[str(i)] = label

    # Load the accuracy metric from the datasets package
    metric = evaluate.load("accuracy", cache_dir=None)

    # What's going on here
    def compute_metrics(p):
        """Computes accuracy on a batch of predictions"""
        return metric.compute(predictions=np.argmax(p.predictions, axis=1), references=p.label_ids)

    # how do these work? do we need all these arguments?
    config = AutoConfig.from_pretrained(
        model_name_or_path,
        num_labels=len(labels),
        label2id=label2id,
        id2label=id2label,
        finetuning_task="image-classification",
        cache_dir=None,
        revision="main",
        token=None,
        trust_remote_code=False,
    )
    model = AutoModelForImageClassification.from_pretrained(
        model_name_or_path,
        from_tf=False,
        config=config,
        cache_dir=None,
        revision="main",
        token=None,
        trust_remote_code=False,
        ignore_mismatched_sizes=False,
    )
    image_processor = AutoImageProcessor.from_pretrained(
        model_name_or_path,
        cache_dir=None,
        revision="main",
        token=None,
        trust_remote_code=False,
    )

    # I have no idea what's going on here
    # Define torchvision transforms to be applied to each image.
    if isinstance(image_processor, TimmWrapperImageProcessor):
        _train_transforms = image_processor.train_transforms
        _val_transforms = image_processor.val_transforms
    else:
        if "shortest_edge" in image_processor.size:
            size = image_processor.size["shortest_edge"]
        else:
            size = (image_processor.size["height"], image_processor.size["width"])

        # Create normalization transform
        if hasattr(image_processor, "image_mean") and hasattr(image_processor, "image_std"):
            normalize = Normalize(mean=image_processor.image_mean, std=image_processor.image_std)
        else:
            normalize = Lambda(lambda x: x)
        _train_transforms = Compose(
            [
                RandomResizedCrop(size),
                RandomHorizontalFlip(),
                ToTensor(),
                normalize,
            ]
        )
        _val_transforms = Compose(
            [
                Resize(size),
                CenterCrop(size),
                ToTensor(),
                normalize,
            ]
        )


    # functions used in trining
    def train_transforms(example_batch):
        """Apply _train_transforms across a batch."""
        example_batch["pixel_values"] = [
            _train_transforms(pil_img.convert("RGB")) for pil_img in example_batch["image"]
        ]
        return example_batch

    def val_transforms(example_batch):
        """Apply _val_transforms across a batch."""
        example_batch["pixel_values"] = [
            _val_transforms(pil_img.convert("RGB")) for pil_img in example_batch["image"]
        ]
        return example_batch

    dataset["train"].set_transform(train_transforms)
    dataset["validation"].set_transform(val_transforms)

    # Initialize our trainer
    trainer = Trainer(
        model=model,
        args=trainer_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"],
        compute_metrics=compute_metrics,
        processing_class=image_processor,
        data_collator=collate_fn,
    )

    # Training
    checkpoint = None
    # if last_checkpoint is not None:
    #     checkpoint = last_checkpoint
    train_result = trainer.train(resume_from_checkpoint=checkpoint)
    trainer.save_model()
    trainer.log_metrics("train", train_result.metrics)
    trainer.save_metrics("train", train_result.metrics)
    trainer.save_state()

    # Evaluation
    metrics = trainer.evaluate()
    trainer.log_metrics("eval", metrics)
    trainer.save_metrics("eval", metrics)

    # I don't think we need this
    # Write model card and (optionally) push to hub
    kwargs = {
        "finetuned_from": model_name_or_path,
        "tasks": "image-classification",
        "dataset": train_dir,
        "tags": ["image-classification", "vision"],
    }
    trainer.create_model_card(**kwargs)


if __name__ == "__main__":
    main()
