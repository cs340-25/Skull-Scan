## How to use the script
# Organize the images: 
Place the images in subdirectories within a main directory, where each subdirectory represents a class. For example:

images/
├── class1/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── class2/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── ...

# Run the script: 
Use the command line to run the script, specifying the input directory and the output file name:

python process_images.py images/ processed_data.pkl

This script will process all images, resize them to 32x32 pixels, and save them in a pickle file along with their labels. 
The structure of the output file will be similar to CIFAR-10, with 'data' containing the image arrays, 'labels' containing the class labels, and 'label_names' containing the names of the classes.

# The images do not need to have labels attached to them. 
The script will automatically assign labels based on the names of the subdirectories that contain the images.

# Here's how it works:
  * Each subdirectory inside the input_dir represents a different class/category of images.
  * The script will read the names of these subdirectories and use them as class labels.
  * It will then process the images in each subdirectory, resize them, and assign a numerical label based on the order of the subdirectories.

For example, if your directory structure is like this:

images/
├── cats/
│   ├── cat1.jpg
│   ├── cat2.jpg
│   └── ...
├── dogs/
│   ├── dog1.jpg
│   ├── dog2.jpg
│   └── ...
└── birds/
    ├── bird1.jpg
    ├── bird2.jpg
    └── ...

  * The subdirectory cats will be assigned the label 0.
  * The subdirectory dogs will be assigned the label 1.
  * The subdirectory birds will be assigned the label 2.

The labels are inserted by the script during the processing stage, so you don't need to manually label each image. 
Just ensure that the images are organized in subdirectories named according to their classes.
