from tkinter import messagebox
messagebox.showinfo(title = "A Friendly Message", message = "Hello, Tkinter!")
messagebox.askyesno(title = "Hungry?", message = "Do you want SPAM?")

from tkinter import filedialog
filename = filedialog.askopenfile()
print(filename.name)
from tkinter import colorchooser
colorchooser.askcolor(initialcolor = "#FFFFF")

