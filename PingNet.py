# Import the required libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import time

import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import ping3

sum_of_response_times = 0
num_of_icmp_pkts = 0
num_of_responses_recived = 1

# Create an instance of tkinter frame or window
win=Tk()

def ping():
    global sum_of_response_times
    global num_of_icmp_pkts
    global num_of_responses_recived

    t = ping3.ping("google.com")
    tl = 0
    if(t == None):
        tl = 0
    else:
        tl = t
        
    sum_of_response_times = sum_of_response_times+tl
    num_of_icmp_pkts+=1
    if(t != 0):
        num_of_responses_recived+=1
    
    avg_response_time = sum_of_response_times / num_of_responses_recived
    
    print("Response time: ",t,"Avg Response time: ", avg_response_time)

    if(t == None or avg_response_time > 0.8 ):
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