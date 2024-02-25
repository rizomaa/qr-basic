from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

def generate():
    name = name_entry.get()
    link = link_entry.get()

    file_name = name+".png"    
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)

    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(root, image=image)
    image_label.image = image

    canvas.create_window(200, 450, window=image_label)

root = Tk()
root.geometry("500x500")

canvas = Canvas(root, width=400, height=800)
canvas.pack()

app_label = Label(root, text="QR generator", fg='blue', font=("Ubuntu", 30))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="Link name")
link_label = Label(root, text="Link")
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

button = Button(text="GENERATE QR", command=generate)
canvas.create_window(200, 230, window=button)


root.mainloop()