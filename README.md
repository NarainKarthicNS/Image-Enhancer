# Image-Enhancer
It is an Image Enhancer that enhances your image's Colors , Sharpness , Brightness , Contrast using Python.It is Powered by Pillow Module and supported by tkinter module.

## Steps
1) Install Pillow using `python3 -m pip install --upgrade Pillow`
2) Run the main.py file

## How It Works
It works by increasing factors of the image seperately(such as sharpness,brightness,contrast and etc) and then merging the file into a single ".png" as the output.You can see how it works behind the hood by reading the in-line comments in the "main.py" file.But in Brief we use `PIL.Image` and `PIL.ImageEnhance` classes and `Image.enhance()` function to adjust the image's parameters.You can also check out a few sample in the "Samples" folder.Try it out and Hope it is Useful!
