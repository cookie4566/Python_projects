# ATM banking app
# Created: 9-17-23
# By Christopher Kennedy
from tkinter import *
from tkinter import ttk

# window
root = Tk()
root.title('Bank of inritum')
content = ttk.Frame(root)
header = ttk.Frame(content, borderwidth=4, relief="ridge",width=250,height=150)
h1 = ttk.Label(content, text = "Bank of inritum")

content.grid(column=0, row=0)
header.grid(column=0, row=0)
h1.grid(column=0, row=0)
root.mainloop()