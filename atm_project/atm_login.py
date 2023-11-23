# ATM banking app
# Created: 9-17-23
# By Christopher Kennedy
from tkinter import *
from tkinter import ttk

#       METHODS             #

# Main banking menu.


# new window with if statment

# checking acconut balance
def money():
    dough = 2000
    return dough

def checkingAccount(cash):
    money = cash
    return str(money)

def newAccount():
    account = Toplevel(root)
    account.title('New Account')
    account.geometry('200x200')
    nu_user_name = ttk.Label(account, text='New Email/User')
    nu_user_password = ttk.Label(account, text='New User Password')
    new_user = ttk.Entry(account,textvariable=StringVar)
    new_user_passwod = ttk.Entry(account, textvariable=StringVar)
    new_user_button = ttk.Button(account,text='Enter', command= lambda: [newAccountAdd(new_user.get,new_user_passwod.get), account.destroy()])
    nu_user_name.grid(row=0,column=0)
    nu_user_password.grid(row=1,column=0)
    new_user.grid(row=0, column=1)
    new_user_passwod.grid(row=1, column=1)
    new_user_button.grid(row=2,column=1)
    
# function for storing user data and information(I could do this using classes)    
def newAccountAdd(user,password):
    user1 = user
    password1 = password
    
    with open('data.txt', 'wt') as file:
        file.write(str(user1))
        file.write(str(password1))
   
# Function for login(?)
def newWindow():
# vaild user namer/password
    if password.get() == 'test' and username.get() == 'cookie':
        good = Toplevel(root)
        good.title("Good")
        good.geometry('200x200')
        welcome_user = ttk.Label(good, text="Welcome "+ username.get() + "," + "How are you today!")
        welcome_user.grid(row=0,column=0)
        checking = ttk.Label(good, text = "you have " + str(checkingAccount(500)))
        checking.grid(row=1,column=1)
# Invalid username/password
    else:
        error = Toplevel(root)
        error.title("test")
        error.geometry('200x200')
        new_account = ttk.Button(error, text='Create Account', command= newAccount,)
        error_exit = ttk.Button(error,text='Exit', command=error.destroy)
        errorm = ttk.Label(error,text="Wrong Password/Username")
        error_exit.grid(row=1,column=0)
        new_account.grid(row=2, column=0)
        errorm.grid(row=0,column=0)
    return 

# Bank funds
savings_account = 500
checkings_account = 15

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
enter = ttk.Button(content, text = "Enter", command= newWindow)
username = ttk.Entry(content,textvariable=StringVar)
password = ttk.Entry(content, show="*",textvariable=StringVar)
new_account = ttk.Button(content, text='Forgot password/E-Mail?', command=newAccount)

# grid config
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# grid placement
content.grid(column=0, row=0, rowspan=5)
header.grid(column=0, row=0)
h1.grid(column=0, row=0)
enter.grid(column=1, row=5)
username.grid(column=1, row=3)
password.grid(column=1, row=4)
user.grid(column=0, row=3)
pw.grid(column=0, row=4)
new_account.grid(column=2,row=5)

# main loop
root.mainloop()