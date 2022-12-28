# Image-Enhancer
It is an Image Enhancer that enhances your image's Colors , Sharpness , Brightness , Contrast using Python.It is Powered by Pillow Module and supported by tkinter module.

## Steps
1) Install Pillow using `python3 -m pip install --upgrade Pillow`
2) Run the main.py file

## How It Works
It works by increasing factors of the image seperately(such as sharpness,brightness,contrast and etc) and then merging the file into a single ".png" as the output.You can see how it works behind the hood by reading the in-line comments in the "main.py" file.But in Brief we use `PIL.Image` and `PIL.ImageEnhance` classes and `Image.enhance()` function to adjust the image's parameters.You can also check out a few sample in the "Samples" folder.Try it out and Hope it is Useful!
![Sample1](https://user-images.githubusercontent.com/76911069/209784784-9b71aff6-1a5f-4c71-a2b2-19850baf303e.jpg)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
![Sample1_Edited](https://user-images.githubusercontent.com/76911069/209784839-b1fab520-09b4-4f56-99e3-5e07d5f9984c.png)

