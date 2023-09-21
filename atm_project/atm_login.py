# ATM banking app
# Created: 9-17-23
# By Christopher Kennedy
from tkinter import *
from tkinter import ttk

# window
root = Tk()
root.title('Bank of inritum')

# content section
content = ttk.Frame(root)

#children of content
header = ttk.Frame(content, borderwidth=4, relief="ridge",width=250,height=150)
h1 = ttk.Label(content, text = "Bank of inritum")
user = ttk.Label(content, text="User name/E-mail")
pw = ttk.Label(content, text="Password")
enter = ttk.Button(content, text = "Enter", command= root.destroy)
username = ttk.Entry(content,textvariable=StringVar)
password = ttk.Entry(content, show="*",textvariable=StringVar)

# grid placement
content.grid(column=0, row=0, rowspan=5)
header.grid(column=0, row=0)
h1.grid(column=0, row=0)
enter.grid(column=1, row=5)
username.grid(column=1, row=3)
password.grid(column=1, row=4)
user.grid(column=0, row=3)
pw.grid(column=0, row=4)

# main loop
root.mainloop()