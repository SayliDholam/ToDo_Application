#HOME PAGE 

import tkinter as tk 
import random
import subprocess

#------------------------------------------------------------

root= tk.Tk()
#window configuration
root.title("Home Page")
root.geometry("500x380")
root.resizable(False,False)

#--------------------------------------------------------------

#Redirect to login page
def run_loginpage():
    subprocess.Popen(['python', 'login.py'])

 #Redirect to register page
def run_registerpage():
    subprocess.Popen(['python', 'register.py'])

#---------------------------------------------------------------------------------------------------------------------------
    
# Add a label
label1 = tk.Label(root, text=" HOME PAGE ", font=('Segoe UI', 18))
label1.pack(padx=20,pady=20)

# Add a login button
login_button = tk.Button(root, text=" Login ",  font=('Lucida Calligraphy', 12),width=16, height=2, relief=tk.RIDGE, bd=5,bg="#CDCDC0", fg="black", command=run_loginpage)
login_button.pack(padx=18, pady=18)

# Add a register button
register_button = tk.Button(root, text="Register", font=('Lucida Calligraphy', 12) , width=16, height=2, relief=tk.RIDGE, bd=5, bg="#CDCDC0", fg="black", command=run_registerpage)
register_button.pack(padx=18, pady=18)

#-------------------------------------------------------------------------------------------------------------------------

# Define function for changing background color
def change_bg():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = f'#{r:02x}{g:02x}{b:02x}'
    root.config(bg=color)

# Add a button to change the background color
color_button = tk.Button(root, text="Change Background", command=change_bg)
color_button.pack(padx= 14, pady=14)

# Set the initial background color
change_bg()

# Run the application
root.mainloop()
