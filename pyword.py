# Word processor made in python
# Note app
#By Christopher Kennedy
#8/16/2023
from tkinter import *
from tkinter import ttk
## import tkMessageBox
# function for callbacks
def hello():
    tkMessageBox.showinfo("Saved!", "Sike!")
    
# function for menu items
def placeHolder():
    file = Toplevel(root)
    button = Button(file, text="This is a place holder")
  


# Creates a TK object
root = Tk()
frm = ttk.Frame(root, padding= 20)
frm.grid()

# Menu toolbar
# creates a menu object
mennubar = Menu(root)
# 
filem = Menu(mennubar, tearoff=0)
# File pull-down section
mennubar.add_cascade(menu= filem, label = "File")
filem.add_command(label="New", command= placeHolder)
filem.add_command(label = "Open", command = placeHolder)
filem.add_command(label = "Save", command = placeHolder)
filem.add_command(label = "Save as...", command = placeHolder)
filem.add_command(label = "Close", command = root.destroy)

filem.add_separator()

filem.add_command(label = "Exit", command = root.destroy)

# Text field 
text = Text().grid(column=0, row=1)

root.config(menu=mennubar)
# Creates the window
root.mainloop()