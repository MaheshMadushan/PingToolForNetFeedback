# Import the required libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import time

import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import ping3

# Create an instance of tkinter frame or window
win=Tk()

def ping():
    t = ping3.ping("google.com")
    if(t == None):
        label.config(text="Net is Slow", fg="white", bg="red")
    elif(t == False):
        label.config(text="Net Connection is closed", fg="white", bg="blue")
    else:
        label.config(text="Net OK", fg="white", bg="green")
    win.after(100,ping)

# Set the size of the window
win.geometry("100x100")

label = Label(text="Hi", fg="white", bg="black")
label.pack()

ping()
    
win.mainloop()


