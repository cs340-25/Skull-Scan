
# This program will uses the flickr8k dataset from kaggle.com
# it uses the cpations.txt file to sort the images into folders name dog and other
from pathlib import Path
import shutil

with open('./archive/flickr8k/captions.txt', 'r') as file :
    lines = list(file)[1:]

line_count = 0
for line in lines :
    if line_count >= 500 : break
    line_count += 1

    parts = line.split(',')
    path = parts[1]
    src_path = Path("./archive/flickr8k/images/" + parts[0])


    if path.lower().find("dog") != -1 :
        dest_path = Path("./docker_settings/database/dog/" + parts[0])
    else :
        dest_path = Path("./docker_settings/database/other/" + parts[0])
        
    try :
        shutil.copyfile(src_path, dest_path)
    except Exception as error :
        print(error)