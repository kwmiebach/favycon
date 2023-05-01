#!/usr/bin/env python3

import json
import PIL
from PIL import Image, ImageDraw

def load_colors_from_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return {color["color"]: color["hex"] for color in data["colorlist"]}

def create_favicon(color):
    size = (64, 64)
    image = Image.new("RGB", size, color)
    draw = ImageDraw.Draw(image)
    return image

def save_favicon(image, fullpath):
    image.save(fullpath)

def ensure_favicon_folder(path):
    import os
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == "__main__":
    ensure_favicon_folder("./icon")
    colors = load_colors_from_file("color.json")
    for colorname, colorvalue in colors.items():
        image = create_favicon(colorvalue)
        save_favicon(image, fullpath=f"./icon/{colorname}.ico")
