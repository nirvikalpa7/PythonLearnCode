from tkinter import *
from PIL import Image, ImageTk


def draw_image(img_width: int, img_height: int):
    img = Image.new(mode="RGB", size=(img_width, img_height), color=(153, 153, 255))
    pixels = []

    for i in range(img_height):
        for j in range(img_width):
            r = int(abs(2 * j - i) % 255)
            g = int(abs(2 * i - j) % 255)
            b = int(abs(j + 2 * i) % 255)
            pix = (r, g, b)
            pixels.append(pix)

    # Set the pixel values of the image
    img.putdata(pixels)
    return img


root = Tk()
root.title("My first GUI app on Python")

img_width = 400
img_height = 400

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (img_width/2)
y = (hs/2) - (img_height/2)
root.geometry('%dx%d+%d+%d' % (img_width, img_height, x, y))

img = draw_image(img_width, img_height)

test = ImageTk.PhotoImage(img)

w = Label(root, width = img_width, height = img_height, image=test)
w.pack()
root.mainloop()
