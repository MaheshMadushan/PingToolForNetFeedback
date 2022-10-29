# Import the required libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import time

import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import ping3
i = 0
n = 0
# Create an instance of tkinter frame or window
win=Tk()

def ping():
    global i
    global n
    t = ping3.ping("google.com")
    if(t == None):t = 0
    i = i+t
    n+=1
    print("Response time: ",t,"Avg Response time: ", (i/n))
    if(t == 0 or (i/n) > 0.8 ):
        label.config(text="Net is Slow", fg="white", bg="red")
    elif(t == False):
        label.config(text="Connection is closed", fg="white", bg="blue")
    else:
        label.config(text="Net OK", fg="white", bg="green")
    win.after(1000,ping)

# Set the size of the window
win.geometry("80x20")

label = Label(text="Hi", fg="white", bg="black")
label.pack()

ping()
    
win.mainloop()


