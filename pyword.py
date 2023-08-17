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
    button.pack()



# Creates a TK object
root = Tk()
frm = ttk.Frame(root, padding= 20)
frm.grid()

mennubar = Menu(root)
filem = Menu(mennubar, tearoff=0)
filem.add_command(label="New", command= placeHolder)
filem.add_command()
# ////////Buttons

quit = ttk.Button(frm, text = 'quit', command= root.destroy).grid(column = 1, row = 0)
save = ttk.Button(frm, text = 'save', command = root.destroy).grid(column = 1, row = 1)
post = ttk.Button 

# Text field 
text = Text().grid(column=0, row=1)

root.config(menu=mennubar)
# Creates the window
root.mainloop()