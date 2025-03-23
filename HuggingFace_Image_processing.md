# HuggingFace Iamge Processing

## Resources

* https://huggingface.co/docs/transformers/model_doc/clip
* https://github.com/huggingface/transformers
* https://github.com/huggingface/transformers/blob/main/examples/pytorch/image-classification/README.md
* https://huggingface.co/docs/transformers/en/tasks/image_classification
* https://huggingface.co/docs/datasets/en/image_load
* https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/pipelines#transformers.ImageClassificationPipeline

## Steps

1. install PyTorch. I used conda to do this.
2. `git clone https://github.com/huggingface/transformers`
3. `cd transformers`
4. `pip install .
5. navigate terminal to `transformers/examples/pytorch/image-classification`
6. format your data by putting images into a folder structure where the folders holding the images are named after the labels you want to use. e.g. data/dog/image1.png
7. I wrote a simple python script to do this.
8. run ```python run_image_classification.py \
    --train_dir <path-to-train-data-dir> \
    --output_dir <path-to-model-result> \
    --remove_unused_columns False \
    --do_train \
    --do_eval```
9. I wrote another simple python script to classify an image using the resulting model, and huggingface pipeline.
10. run it and it will print the classification results for an image defined in the script.
