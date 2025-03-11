# Skull Scan
We will be using the CLIP software from OpenAI
Here is the link to the instructions for installing 
[CLIP](https://github.com/openai/CLIP/tree/main)



To use this you must first make batch folders of the content you want to scan
Then you will use the Image_proccessing.py script to make binary forms of the folders
Instructions for that can be found here: [Usage_of_image_Processing.md](/Usage_of_image_processing.md)

This site has a lot of data sets to work with.
[kaggle.com](https://www.kaggle.com/datasets/aladdinpersson/flickr8kimagescaptions)

## Using the Database

To get image html path use browse in icputrd and click image and keep clicking images.

images are in `/opt/mean.js/public`

Mockus used `zcat master_dataset_w_ADD.csv.gz|grep ,head, |cut -d, -f4| sort -R | head -300 > forMylon`
to copy data from csv file

He used this to remove part of the path on the images
`sed -i 's|.*/public/||' forMylon`

the main csv file is in the default directory
`master_dataset_w_ADD.csv.gz`

forMylon has some head image paths.
