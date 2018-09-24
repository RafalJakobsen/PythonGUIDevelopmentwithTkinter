from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text="Trippel Garanti")
button.pack()


def clickTrippelGaranti():
    print("22.5%")


button.config(command=clickTrippelGaranti)
# print (button.invoke())
# button.state(["disabled"])
# print (button.instate(["disabled"]))
# (button.state(["!disabled"]))
# button.state(["disabled"])
# print(button.instate(["!disabled"]))
logo = PhotoImage(file="C:/Users/rafal/Desktop/Project Fjordkraft/GUI/fjordkraft logo.gif")
button.config(image=logo, compound=LEFT)
small_logo = logo.subsample(5, 5)
button.config(image=small_logo)

root.mainloop()
