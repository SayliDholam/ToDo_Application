#LOGIN MODULE

from tkinter import *
import subprocess
from pymongo import MongoClient

#-----------------------------------------------------------------------------

# Connect to MongoDB database
client = MongoClient('mongodb://localhost:27017')
db = client['Data_Base1']
users = db['users']

#---------------------------------------------------------------------------------

# Create login window
window = Tk()
window.title("Todo App Login")
window.geometry("300x190")

# Create labels and input fields
username_label = Label(window, text="Username:")
username_label.grid(column=0, row=0, padx=10, pady=10)
username_entry = Entry(window, width=30)
username_entry.grid(column=1, row=0, padx=10, pady=10)

password_label = Label(window, text="Password:")
password_label.grid(column=0, row=1, padx=10, pady=10)
password_entry = Entry(window, width=30, show="*")
password_entry.grid(column=1, row=1, padx=10, pady=10)

#--------------------------------------------------------------------------------------------

# Create login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if input fields are empty or not
    if not username and not password  :
        error_label.config(text="Please enter data")
        return
    
    # Check if username and password are correct
    user = users.find_one({'username': username, 'password': password})
    if user:
        # Redirect to next page
        window.destroy()
        # Insert code for next page here
        subprocess.Popen(['python', 'taskupdate_with_speechcommands.py'])
        
    else:
        error_label.config(text="Invalid username or password")

#----------------------------------------------------------------------------------------------
        
# Create buttons
login_button = Button(window, text="Login", command=login, bg="white", fg="blue",padx = 3, pady=3, font = "Palatino", relief="groove", bd=4)
login_button.grid(column=1, row=2, padx=10, pady=10)

# Create error label
error_label = Label(window, fg="red")
error_label.grid(column=1, row=3)

window.mainloop()
