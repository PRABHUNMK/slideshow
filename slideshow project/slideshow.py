import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk



# adjust window
root=tk.Tk()
root.geometry("1200x1200")

# loading the images
img=ImageTk.PhotoImage(Image.open("1.jpg"))
img2=ImageTk.PhotoImage(Image.open("2.jpg"))
img3=ImageTk.PhotoImage(Image.open("3.jpg"))
img4=ImageTk.PhotoImage(Image.open("4.jpg"))
img5=ImageTk.PhotoImage(Image.open("5.jpg"))

l=Label()
l.pack()



# using recursion to slide to next image
x = 1

# function to change to next image
def move():
	global x
	if x == 6:
		x = 1
	if x == 1:
		l.config(image=img)
	elif x == 2:
		l.config(image=img2)
	elif x == 3:
		l.config(image=img3)
	elif x == 4:
		l.config(image=img4)
	elif x == 5:
		l.config(image=img5)
	x = x+1
	root.after(20000, move)

# calling the function
move()



root.mainloop()
