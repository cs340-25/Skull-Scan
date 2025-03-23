from datasets import load_dataset

ds = load_dataset("imagefolder", data_dir=<path-to-image-data>, split="train[:10]")

image = ds["image"][0]

from transformers import pipeline

classifier = pipeline("image-classification", model=<path-to-fine-tuned-model>)

print(classifier(image))
