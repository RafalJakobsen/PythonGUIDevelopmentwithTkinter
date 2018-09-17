from tkinter import *
from tkinter import ttk

root = Tk()
checkbutton = ttk.Checkbutton(root, text="SPAM?")
checkbutton.pack()
spam = StringVar()
spam.set("SPAM!")
print(spam.get())

checkbutton.config(variable=spam, onvalue="SPAM Please", offvalue="Boo SPAM")
print(spam.get())

breakfast = StringVar()
ttk.Radiobutton(root, text="SPAM", variable=breakfast, value="SPAM").pack()
ttk.Radiobutton(root, text="Eggs", variable=breakfast, value="Eggs").pack()
ttk.Radiobutton(root, text="Sausage", variable=breakfast, value="Sausage").pack()
ttk.Radiobutton(root, text="Mais", variable=breakfast, value="Mais").pack()
print(breakfast.get())

checkbutton.config(textvariable=breakfast)

root.mainloop()
