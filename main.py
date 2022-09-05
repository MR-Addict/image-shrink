import os
import PIL
from PIL import Image

max_width = 1000                    # Image max width
max_size = 500                      # Image max
src_path = './'                     # Image source folder you put
img_types = '.jpg', '.png', 'jpeg'  # Image types you got

all_files = {}


def get_files(path):
    all_files[path] = os.listdir(path)
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            get_files(path+file+'/')


def get_imgs(img_types):
    all_imgs = []
    for dir in all_files.keys():
        for file in all_files[dir]:
            if os.path.isfile(dir+file):
                if file.lower().endswith((img_types)):
                    all_imgs.append(dir+file)
    return all_imgs


def resize_img(img_path, max_width, max_size):
    if os.path.getsize(img_path) > 1024*max_size:
        img = Image.open(img_path)
        if img.width > max_width:
            wpercent = (max_width/float(img.width))
            hsize = int((float(img.height)*float(wpercent)))
            img = img.resize((max_width, hsize), PIL.Image.ANTIALIAS)
            img.save(img_path, optimize=True, quality=30)


def main():
    get_files(src_path)
    for img_path in get_imgs(img_types):
        resize_img(img_path, max_width, max_size)


if __name__ == '__main__':
    main()
