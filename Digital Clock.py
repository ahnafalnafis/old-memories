from tkinter import * 
from tkinter.ttk import *
from time import strftime

root = Tk()
def times():
    string = strftime("%H:%M:%S %p")
    string = strftime('%H:%M:%S %p %d/%m/%y')
    lable.config(text = string)
    lable.after(1000,times)

lable = Label(root,font=("time",80),background="White",foreground="Black")
lable.pack(anchor="center")
times()
mainloop()