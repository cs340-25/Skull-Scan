import requests
import shutil
import os



def copy_image_from_url(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        with open(file_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
        print(f'Image copied successfully to {file_path}')

    except requests.exceptions.RequestException as e:
        print(f'Error copying image: {e}')


try :
    with open('stg4.csv', 'r') as csv :
        entries = list(csv)[1:]

    imgNum = 0
    # os.mkdir('stg4')
    for entry in entries :
        path = entry.split(',')[3]
        path = path[path.find('public/') + len('public/') - 1:]
        image_url = f'http://localhost:3000{path}'
        save_path = f'stg4/skull-image{imgNum}.png'
        copy_image_from_url(image_url, save_path)
        imgNum += 1

except Exception as e:
    print(e)
        

image_url = 'http://localhost:3000/anau_img3/00b/00b00706.08.JPG'
save_path = 'skull-image.png'
copy_image_from_url(image_url, save_path)
