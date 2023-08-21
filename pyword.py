# Word processor made in python
# Note app
#By Christopher Kennedy
#8/16/2023
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
## import tkMessageBox
# function for callbacks
def hello():
    tkMessageBox.showinfo("Saved!", "Sike!")
    
# function for menu items
def placeHolder():
    file = Toplevel(root)
    button = Button(file, text="This is a place holder")
    button.pack()
    
def saved():
    file = asksaveasfile(mode = 'w', defaultextension=".txt")
    if file is None:
        return
    saveText = str(text.get(1.0, END))
    file.write(saveText)
    file.close()
                
    
  


# Creates a TK object
root = Tk()
frm = ttk.Frame(root, padding= 20)


# Menu toolbar
# creates a menu object
mennubar = Menu(root)
# 
filem = Menu(mennubar, tearoff=0)
# File pull-down section
mennubar.add_cascade(menu= filem, label = "File")
filem.add_command(label="New", command= placeHolder)
filem.add_command(label = "Open", command = placeHolder)
filem.add_command(label = "Save", command = saved)
filem.add_command(label = "Save as...", command = placeHolder)
filem.add_command(label = "Close", command = root.destroy)

filem.add_separator()

filem.add_command(label = "Exit", command = root.destroy)

# Edit pull-down menu
edit = Menu(mennubar, tearoff=0)
mennubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut", command=placeHolder)
edit.add_command(label="Copy", command=placeHolder)
edit.add_command(label="Paste", command=placeHolder)
edit.add_command(label="Delete", command=placeHolder)
edit.add_command(label="Select All", command=placeHolder)


# Text field 
# text = Text().grid(column=0, row=1)

text = Text(root)
text.pack()
root.config(menu=mennubar)
# Creates the window
root.mainloop()