import json
from io import BytesIO

from PIL import Image, ImageChops

def read_image(image_url):
    image = Image.open(BytesIO(image_url))
    return image

def read_process_dict(process_dict_path):
    with open(process_dict_path, encoding='utf-8') as file:
        process_dict = json.load(file)
    return process_dict

def process_text(summarized_text, process_dict):
    processed_text = summarized_text
    for word in process_dict.keys():
        processed_text = processed_text.replace(word, process_dict[word])
    return processed_text

def crop_image_border(image_url):
    image = read_image(image_url)
    bbox = ImageChops.add(image, image, 1, -100).getbbox()
    cropped_image = image.crop(bbox) if bbox else image
    return cropped_image

def save_image(image, image_file_path):
    image.save(image_file_path)