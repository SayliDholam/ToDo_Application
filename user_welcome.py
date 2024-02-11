#WELCOME PAGE

#--------------------------------------------------------------------------------------------------------------------------------

import tkinter as tk
from PIL import Image, ImageTk
import subprocess
  
#--------------------------------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title("Welcome Screen")
root.geometry("780x650")
root.resizable(False,False)

label1 = tk.Label(root, text=" TASK & TICK  : THE TO-DO APPLICATION", font=('Segoe UI', 22))
label1.pack(padx=20,pady=20)

#-----------------------------------------------------------------------------------------------------------------------------------

# Locate and Open the image file and resize it
image_file = "bg_img.png"
image = Image.open(image_file)
resized_image = image.resize((470, 470), Image.LANCZOS)

# Create a PhotoImage object from the resized image
photo = ImageTk.PhotoImage(resized_image)

# Create a label widget to display the image
background_label = tk.Label(root, image=photo)
background_label.pack(fill=tk.BOTH, expand=True)

#----------------------------------------------------------------------------------------------------------------------------------

#Redirect to homepage
def run_homepage():
    subprocess.Popen(['python', 'home.py'])

# Create the home page button 
button1 = tk.Button(root, text="Go to Home Page", bg = "#F0F0F8" , width=40 ,font = "Palatino", relief="groove", bd=5 , command=run_homepage)
button1.pack(side=tk.BOTTOM, padx = 20, pady=20)

root.mainloop()
