from tkinter import *  #a simple way to create GUI elements using the widgets found in the Tk toolkit
from tkinter.ttk import *

from time import strftime #used to convert date and time objects to their string representation

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root,font=("ds-digital",80),background="black",foreground = "cyan")
label.pack(anchor='center')
time()

mainloop()
