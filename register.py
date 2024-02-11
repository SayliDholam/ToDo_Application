
#REGISTER MODULE

from tkinter import *
from pymongo import MongoClient
import tkinter as tk
from tkinter import ttk

#------------------------------------------------------------------

# Connect to MongoDB database
#connection to mongodb
client = MongoClient('mongodb://localhost:27017')
#connection to specified database
db = client['Data_Base1']
#connection to specified table
users = db['users']

#------------------------------------------------------------------

# Create registration window
window = Tk()
window.title("Todo App Registration Window")
window.geometry("400x350")
window.resizable(False,False)

# Create labels and input fields
firstname_label = ttk.Label(window, text="First Name:")
firstname_entry = ttk.Entry(window,width=40)


lastname_label = ttk.Label(window, text="Last Name:")
lastname_entry = ttk.Entry(window, width=40)

gmail_label = ttk.Label(window, text="Gmail:")
gmail_entry = ttk.Entry(window, width=40)

username_label = ttk.Label(window, text="Username:")
username_entry = ttk.Entry(window, width=40)

password_label = ttk.Label(window, text="Password:")
password_entry = ttk.Entry(window, show="*", width=40)

confirm_password_label = ttk.Label(window, text="Confirm Password:")
confirm_password_entry = ttk.Entry(window, show="*", width=40)

#------------------------------------------------------------------

# Create registration function
def register():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    gmail = gmail_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    
    # Check if password and confirm password match
    if password != confirm_password:
        error_label.config(text="Passwords do not match")
        return
    
    # Check if input fields are empty or not
    if not firstname and not lastname and not gmail and not username and not password and not confirm_password  :
        error_label.config(text="Please enter data")
        return
    
    # Check if username already exists
    user = users.find_one({'username': username})
    if user:
        error_label.config(text="Username already exists")
        return
    
    # Insert new user into MongoDB database
    new_user = {
         'firstname': firstname,
        'lastname': lastname,
        'gmail': gmail,
        'username': username,
        'password': password,
        'confirm_password': confirm_password
    }
    result = users.insert_one(new_user)
    if result.inserted_id:
        success_label.config(text="Registration successful")
    else:
        error_label.config(text="Failed to insert user into database")

#-----------------------------------------------------------------------------------

register_button = Button(window, text="Register",command=register, bg="white", fg="blue",padx = 5, pady=5, font = "Palatino", relief="groove", bd=4)

# Create error and success labels
error_label = Label(window, fg="red")
error_label.grid(column=1, row=4)

success_label = Label(window, fg="green")
success_label.grid(column=1, row=5)

# layout the labels and entry fields using grid
firstname_label.grid(row=0, column=0, padx=10, pady=10)
firstname_entry.grid(row=0, column=1, padx=10, pady=10)

lastname_label.grid(row=1, column=0, padx=10, pady=10)
lastname_entry.grid(row=1, column=1, padx=10, pady=10)

gmail_label.grid(row=2, column=0, padx=10, pady=10)
gmail_entry.grid(row=2, column=1, padx=10, pady=10)

username_label.grid(row=3, column=0, padx=10, pady=10)
username_entry.grid(row=3, column=1, padx=10, pady=10)

password_label.grid(row=4, column=0, padx=10, pady=10)
password_entry.grid(row=4, column=1, padx=10, pady=10)

confirm_password_label.grid(row=5, column=0, padx=10, pady=10)
confirm_password_entry.grid(row=5, column=1, padx=10, pady=10)

register_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

error_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

success_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
