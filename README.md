# Image Shrink Python Script

## 1. Preview

Features:

- Resize all images in specific folder
- Custom image maximum width and maximum size

Attention

- Do not put upper case image type in `img_types` variable, such as `.PNG`, `.JPG`
- After execute code, all your images will be `replaced` with resized images


## 2. How to use

Clone this repository and change `main.py` user variable.

```python
max_width = 1000                    # Image max width
max_size = 500                      # Image max
src_path = './'                     # Image source folder you put
img_types = '.jpg', '.png', 'jpeg'  # Image types you got
```

There no requirement packages you need to install if you're using python 3.8+

After that execute python code

```bash
python main.py
```

Happy coding!