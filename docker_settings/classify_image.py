from datasets import load_dataset

ds = load_dataset("imagefolder", data_dir="./database", split="train[-10:]")

image = ds["image"][0] # .show()

from transformers import pipeline

classifier = pipeline("image-classification", model="./model")

print(classifier(image))