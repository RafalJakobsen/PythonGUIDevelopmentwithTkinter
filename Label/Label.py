from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text="Hello, Tkinter")
label.pack()
label.config(text="Howdy, Tkinter! It`s been a shile since we last met. Great to see you again!")
label.config(wraplength=150)
label.config(justify=CENTER)
label.config(foreground="blue", background="yellow")
label.config(font=("arial", 18, "bold"))
label.config(text="Howdy, Tkinter!")
PhotoImage(file="C:/Users/rafal/Desktop/InLearning/Ex_Files_Python_Tkinter/Exercise Files/Ch03/python_logo.gif")
logo = PhotoImage(file="C:/Users/rafal/Desktop/InLearning/Ex_Files_Python_Tkinter/Exercise Files/Ch03/python_logo.gif")
label.config(image=logo)
label.config(compound="text")
label.config(compound="left")
label.img = logo
label.config(image=label.img)

root.mainloop()
