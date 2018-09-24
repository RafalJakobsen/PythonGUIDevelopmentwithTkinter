from tkinter import *
from tkinter import ttk
root = Tk()
treeview = ttk.Treeview(root)
treeview.pack()
treeview.insert("", "0", "item1", text = "First Item")
treeview.insert("", "2", "item2", text = "Second Item")
treeview.insert("", "end", "item3", text = "Third Item")
logo = PhotoImage(file = "C:/Users/rafal/Desktop/Project Fjordkraft/GUI/fjordkraft logo.gif").subsample(10, 10)
treeview.insert("item2", "end", "fjordkraft", text = "Fjordkraft", image = logo)
treeview.config(height = 5)
treeview.move("item2", "item1", "end")
treeview.item("item1", open = True)
print(treeview.item("item1", "open"))
treeview.detach("item3")
treeview.move("item3", "item2", "0")
# treeview.delete("item3")
treeview.config(columns = ("version"))
treeview.column("version", width = 50, anchor = "center")
treeview.column("#0", width = 150)
treeview.heading("version", text = "Version")
treeview.set("fjordkraft", "version", "3.4.1")
treeview.item("fjordkraft", tags = ("software"))
treeview.tag_configure("software", background = "orange")

def callback(event):
    print(treeview.selection())

treeview.bind("<<TreeviewSelect>>", callback)
treeview.config(selectmode = "browse")
treeview.config(selectmode = "none")
# treeview.selection_add("python")
# treeview.selection_remove("python")
# treeview.selection_toggle("python")








root.mainloop()