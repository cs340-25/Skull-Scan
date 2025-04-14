from transformers import pipeline
import argparse
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

parser = argparse.ArgumentParser()
parser.add_argument('--model', help="specify path to model", type=str, default="./model")
parser.add_argument('imagePath', help="specify path to image you want to classify", type=str)

args = parser.parse_args()

classifier = pipeline("image-classification", model=args.model)

try :
    image =  Image.open(args.imagePath)
    print(classifier(image))
except :
    print("couldn't classify imate")