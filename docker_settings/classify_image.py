from datasets import load_dataset
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
#ds = load_dataset("imagefolder", data_dir=<path-to-image-data>, split="train[:10]")

#image = ds["image"][0]
fileName = input("enter image path: ")
image =  Image.open(fileName)


from transformers import pipeline

classifier = pipeline("image-classification", model="./model")

print(classifier(image))