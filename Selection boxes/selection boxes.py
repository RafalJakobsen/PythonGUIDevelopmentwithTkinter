from tkinter import *
from tkinter import ttk

root = Tk()
month = StringVar()
combobox = ttk.Combobox(root, textvariable=month)
combobox.pack()
combobox.config(values=("Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                        "November", "Desember"))

year = StringVar()
Spinbox(root, from_=1990, to=2018, textvariable=year).pack()

root.mainloop()

print(month.get() + " " + year.get())
