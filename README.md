# Skull Scan
This is a set of software that classifies images using libraries and model from Hugging Face Hub.
The first goal is for this software to accurately identify whether an image of a head is fresh or skeletal.
The stretch goal is to match a pair of image by identifying if a picture of a skull and a fresh head are of the same person.

To use this you must first make batch folders of the content you want to scan
Then you will use the Image_proccessing.py script to make binary forms of the folders
Instructions for that can be found here: [Usage_of_image_Processing.md](/Usage_of_image_processing.md)

## Using the Database

The data we are fine-tuning a model with is located on one of Dr. Mockus's machines and accessible over SSH.
You will need to have your UTK VPN activated to access Mockus's machines from home.
You will also need to create a ssh key pair. (checkout the git tutorial linked below)

Here are the commands to connect.
* To server the web tool run `ssh -p3047 -L3000:localhost:3000 anau@da1.eecs.utk.edu` and navigate to localhost:3000 in your web browser.
* To use are docker container run `ssh anau@da6.eecs.utk.edu`

## Docker Details
Our software is set up inside a docker container. [hub.docker.com](https://hub.docker.com/repository/docker/mylonjones/huggingface_transformers/general)

* To start the image run `docker start -a -i skull1` this lets you run commands in the container
* To create a new container from the image run `docker run -it --name skull1 -p8000:8000 mylonjones/huggingface_transformers bash`
* To build a new image run `docker build -t <image-name> .` inside the docker_settings folder
* To exit out of a container run `exit`
* To get help with docker run `docker --help`

## Extracted data 
The shell scripts extract the images from the .gz file and put them into seprate .csv files so we can run the model on this data
- `dataExtractor.sh` -> takes all stage 4-6 head images and puts into `stg4heads.csv`
- `extractHead3.sh` -> takes all stage 1 head images and puts into `stg1heads.csv`

## Resources

[Hugging Face Transformers Tutorial](https://huggingface.co/learn/nlp-course/chapter1/1)

This site has a lot of data sets to work with.
[kaggle.com](https://www.kaggle.com/datasets/aladdinpersson/flickr8kimagescaptions)

[Set up ssh tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Mockus used `zcat master_dataset_w_ADD.csv.gz|grep ,head, |cut -d, -f4| sort -R | head -300 > forMylon`
to copy data from csv file

He used this to remove part of the path on the images
`sed -i 's|.*/public/||' forMylon`

the main csv file is in the default directory
`master_dataset_w_ADD.csv.gz`

forMylon has some head image paths.

start docker 
docker run -it -p 3050:22 -p 8886:8888 -p 6004:6006 -v /home/anau/:/home/anau/ --name skull huggingface/transformers-pytorch-cpu bash

command to copy files
cut -d, -f4 ../stg4heads.csv | grep JPG | while read i; do cp $i .; done

cammand to run example fine-tuner (must be run in image-classification folder)
python run_image_classification.py --train_dir ../database --output_dir ../model/ --remove_unused_columns False --do_train --do_eval


