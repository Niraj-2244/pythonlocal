from tkinter import*
from tkinter.ttk import*\

from time import strftime
root = Tk()
root.title("watch")
root.resizable(0,0)

def time():
    String = strftime('%H:%M:%S %p')
    label.config(text=String)
    label.after(1000, time)


label = Label(root, font=("poppins", 70, ), background="black", foreground="cyan")
label.pack(anchor='center')
time()

mainloop()
