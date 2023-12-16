
# Importing Image and ImageDraw from PIL 
# python -m pip install Pillow
# python -m pip install numpy

from PIL import Image, ImageDraw
import numpy as np
import math
import time

def time_it(func):
    def wrapper (*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print (func.__name__  + " took " + str ( (end -start)*1000) + " mil sec")
        return result
    return wrapper

@time_it
def myImage (width = 100, height = 100) :

    img = Image.new(mode="RGB", size=(width, height), color = (153, 153, 255))

    # Create a list of pixel values
    #pixels = [(255, 0, 0)] * (width * height)  # Red pixels
    pixels = []

    for i in range(height) :
        for j in range(width) :
            r = int (abs(2*j - i) % 255)
            g = int (abs(2*i - j) % 255)
            b = int (abs(j + 2*i) % 255)
            pix = (r, g, b)
            pixels.append(pix)

    # Set the pixel values of the image
    img.putdata(pixels)
    img.show()


@time_it
def myImageMatrix (width = 100, height = 100) :

    # EXACTLY! height at first, then width
    pixel_buffer = np.empty( (height, width, 3)) 

    for i in range(height):
        for j in range(width):
            r = int (abs(2*j - i) % 255)
            g = int (abs(2*i - j) % 255)
            b = int (abs(j + 2*i) % 255)
            pix = np.array([r, g, b])
            pixel_buffer[i, j] = pix

    img = Image.fromarray(np.uint8(pixel_buffer)) # casting to UINT8 is obligatory!
    img.show()

myImage(800, 600)
#myImageMatrix(800, 600)