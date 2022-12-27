#Importing all Dependencies
import PIL.Image
from PIL import ImageEnhance
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
import time

def Enhance(img):
    #Enhancing Visuals
    ''' An enhancement factor of 0.0 results in a 
        full black image and an enhancement factor
        1.0 results the same as the original image.'''

    print("Enhancing your Image...")
    time.sleep(1)
    #Getting Current Sharpness
    curr_sharp = ImageEnhance.Sharpness(img)
    new_sharp = 2.0 #New Adjustment

    #Enhancing Sharpness
    output = curr_sharp.enhance(new_sharp)
    print("Increasing SHARPNESS...")
    time.sleep(1)

    img = output

    #Getting the Current Brightness
    curr_bri = ImageEnhance.Brightness(img)
    new_bri = 1.15#New Adjustment

    #Enhancing Brightness
    output = curr_bri.enhance(new_bri)
    print("Adjusting BRIGHTNESS...")
    time.sleep(1)

    img = output

    # Getting Current Color Data
    curr_col = ImageEnhance.Color(img)
    new_col = 1.25 #New Adjustment

    #Enhancing Color
    output = curr_col.enhance(new_col)
    print("beautifying COLOR FACTORS...")
    time.sleep(1)
    img = output

    #Getting Current Contrast Data
    curr_con = ImageEnhance.Contrast(img)
    new_con = 1.25 #New Adjustment

    #Enhancing Contrast
    output = curr_con.enhance(new_con)
    print("Tweeking Images's CONTRAST PARAMETERS...")
    time.sleep(2)

    
    print("Done Processing!")
    time.sleep(1)

    print("Select a filename and location to save your image")
    files = [('PNG', '*.png')] #Save File Type

    #Asking File Save As Name and Location
    saveAsName = asksaveasfile(mode="w",defaultextension="*.png",filetypes=files).name 

    #Saving Image
    output.save(saveAsName)
    print("Here is Your ENHANCED image!")
    output.show()
    

if __name__ == '__main__':
    print("Select An Image File")

    #Getting Image and Its Location
    imgObj = askopenfile(mode="r") 
    path = f"{imgObj.name}"

    # Assisgning The Specified Image
    img = PIL.Image.open(path)
    
    #This is to Open The Image
    img.show()
    Enhance(img=img)
      


