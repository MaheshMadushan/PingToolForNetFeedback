# Import the required libraries
from tkinter import *
import ping3

sum_of_response_times = 0
num_of_icmp_pkts = 0
num_of_responses_recived = 0
squared_sum = 0

# Create an instance of tkinter frame or window
win=Tk()

def ping():
    global sum_of_response_times
    global num_of_icmp_pkts
    global num_of_responses_recived
    global squared_sum

    response_time = ping3.ping("google.com")
    response_time_in_int = 0
    if(t == None):
        response_time_in_int = 0
    else:
        response_time_in_int = response_time
        
    sum_of_response_times = sum_of_response_times+response_time_in_int
    num_of_icmp_pkts+=1
    if(t != 0):
        num_of_responses_recived+=1
    
    avg_response_time = sum_of_response_times / num_of_responses_recived
    squared_sum += (tl - avg_response_time)**2
    std = (squared_sum / num_of_responses_recived) ** 0.5
    print("Response time: ",response_time,"Avg Response time: ", avg_response_time, "std deviation: ",std)

    if(t == None or avg_response_time > 0.8 ):
        label.config(text="Net is Slow", fg="white", bg="red")
    elif(t == False):
        label.config(text="Connection closed", fg="white", bg="blue")
    else:
        label.config(text="Net OK", fg="white", bg="green")
    
    win.after(1000,ping)

# Set the size of the window
win.geometry("80x20")

label = Label(text="Hi", fg="white", bg="black")
label.pack()

ping()
    
win.mainloop()