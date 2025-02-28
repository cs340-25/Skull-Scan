import os
import numpy as np
from PIL import Image
import pickle

def process_images(input_dir, output_file, image_size=(32, 32), num_classes=10):
    data = []
    labels = []
    label_names = sorted(os.listdir(input_dir))
    
    for label_idx, label_name in enumerate(label_names):
        class_dir = os.path.join(input_dir, label_name)
        if os.path.isdir(class_dir):
            for file_name in os.listdir(class_dir):
                file_path = os.path.join(class_dir, file_name)
                with Image.open(file_path) as img:
                    img = img.resize(image_size)
                    img_array = np.array(img)
                    if img_array.shape == (32, 32, 3):  # Ensure the image is in the correct shape
                        data.append(img_array)
                        labels.append(label_idx)
    
    data = np.array(data)
    labels = np.array(labels)
    
    output = {
        'data': data,
        'labels': labels,
        'label_names': label_names
    }
    
    with open(output_file, 'wb') as f:
        pickle.dump(output, f)
    
    print(f"Processed {len(data)} images into {output_file}")

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Process images into CIFAR-10 format')
    parser.add_argument('input_dir', type=str, help='Directory containing class subdirectories of images')
    parser.add_argument('output_file', type=str, help='Output file name for processed dataset')
    
    args = parser.parse_args()
    
    process_images(args.input_dir, args.output_file)
