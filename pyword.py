# Word processor made in python
# Note app
#By Christopher Kennedy
#8/16/2023
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
## import tkMessageBox
# function for callbacks

    
# function for menu items
def placeHolder():
    file = Toplevel(root)
    button = Button(file, text="This is a place holder")
    button.pack()
# Function for the about section
def Aboot():
    file = Toplevel(root)
    button = Button (file, text="This is where I would put any questions that were frequent and asked.")
    button.pack()
    
# function for saving .txt files
def saved():
    file = asksaveasfile(mode = 'w', defaultextension=".txt")
    if file is None:
        return
    saveText = str(text.get(1.0, END))
    file.write(saveText)
    file.close()
# Function for opening .txt files  
def open():
    file = askopenfile(mode='r', filetypes=[('Text files','*.txt')])
    if file is not None:
        text
        text.insert(1.0,file.read())
# Function for NEW files :)
def new():
    Input = entry.get()
    file = str("filepath" + Input + ".txt")
    text = open()
        
    
                
    
  


# Creates a TK object
root = Tk()
root.title('Pyword!')
root.geometry('600x300')
frm = ttk.Frame(root, padding= 20)
entry = Entry(root)


# Menu toolbar
# creates a menu object
mennubar = Menu(root)
# 
filem = Menu(mennubar, tearoff=0)
# File pull-down section
mennubar.add_cascade(menu= filem, label = "File")
filem.add_command(label="New", command= new)
filem.add_command(label = "Open", command = open)
filem.add_command(label = "Save", command = saved)
filem.add_command(label = "Save as...", command = saved)
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

about = Menu(mennubar, tearoff=0)
mennubar.add_cascade(label="About", menu=about)
about.add_command(label = "FAQ", command=Aboot)


# Text field 
# text = Text().grid(column=0, row=1)

text = Text(root)
text.pack()
root.config(menu=mennubar)
# Creates the window
root.mainloop()