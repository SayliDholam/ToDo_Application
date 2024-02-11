#TASK ENTRIES with SPEECH APPROPRIATE SPEECH COMMANDS and PROGRESS BAR
 
from  tkinter import * 
import tkinter.messagebox
import pyttsx3
from pymongo import MongoClient
import subprocess
import tkinter as tk
from tkinter import ttk

#--------------------------------------------------------------------------------------------------------------

# Connect to MongoDB database
client = MongoClient('mongodb://localhost:27017')
db = client['Data_Base1']
tasks = db['To_Do_Tasks']

#---------------------------------------------------------------------------------------------------------------

#Initialize the Text-to-speech engine
engine = pyttsx3.init()

#Set the rate of speech
#rate = engine.getProperty('rate')

# Set properties (optional)
engine.setProperty("rate", 150)  # Speed of speech (words per minute)
engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

#----------------------------------------------------------------------------------------------------------------------

#function to enter the task in the Listbox
def entertask():
    #A new window to pop up to take input
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            db_entry_task = input_text
            #close the root1 window
            root1.destroy()

            # Speak the command
            engine.say("Task Successfully Entered.")
            # Run the engine and wait for speech to complete
            engine.runAndWait()
            
            #Print the message
            print("ENTER Speech Command executed")

            # Insert data into MongoDB
            tasks.insert_one({
                'Entered ': db_entry_task
                })
            
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=50,height=5)
    entry_task.pack()
    button_temp=Button(root1,text="Add task" ,command=add)
    button_temp.pack()
    root1.mainloop()

#--------------------------------------------------------------------------------------------------------------------------
    
#function to facilitate the delete task from the Listbox
def deletetask():
    #selects the slected item and then deletes it 
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])

   #Executes this to mark completed
    # Speak the command
    engine.say("Task Successfully Deleted.")
    # Run the engine and wait for speech to complete
    engine.runAndWait()
    
    #Print the message
    print("DELETE Speech Command executed")

#----------------------------------------------------------------------------------------------------

 #function to facilitate the checked task from the Listbox   
def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    #store the text of selected item in a string
    temp_marked=listbox_task.get(marked)
    db_delete_task = temp_marked
    #update it 
    temp_marked=temp_marked+" ✔ "

    #delete it then insert it 
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)
    db_marked_task = temp_marked
    
    # Speak the command
    engine.say("Task Successfully Checked.")
    # Run the engine and wait for speech to complete
    engine.runAndWait()
    
    #Print the message
    print("CHECK Speech Command executed")

    # Insert data into MongoDB
    tasks.insert_one({
        'Mark Checked ': db_marked_task
        })
      # Insert data into MongoDB
    tasks.insert_one({
        'Deleted ': db_delete_task
        })

#--------------------------------------------------------------------------------------------------------------------------------

#creating the initial window
window=Tk()
#giving a title
window.title("To_Do_APP main screen")
window.geometry("800x750")
window.resizable(False,False)

#----------------------------------------------------------------------------------------------------------------------------------

#Frame widget to hold the listbox and the scrollbar
frame_task=Frame(window)
frame_task.pack()

#to hold items in a listbox
listbox_task=Listbox(frame_task,bg="black",fg="white",height=20,width=50,font = "Helvetica")  
listbox_task.pack(side=tkinter.LEFT)

#Scrolldown in case the total list exceeds the size of the given window 
#scrollbar_task=Scrollbar(frame_task)
#scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
#listbox_task.config(yscrollcommand=scrollbar_task.set)
#scrollbar_task.config(command=listbox_task.yview)

#---------------------------------------------------------------------------------------------------------------------------------------

class ProgressbarApp:
    def __init__(self, master):
        self.master = master
        self.progress = tk.DoubleVar()
        self.progress.set(0)
        self.progressbar = ttk.Progressbar(self.master, variable=self.progress, orient="horizontal", length=480)
        self.progressbar.pack(pady=10)

    def update_progress(self,arg):
        self.progress.set(self.progress.get()+10)

#----------------------------------------------------------------------------------------------------------------------------------------

#Button widget 
entry_button=Button(window,text="Add a task", bg = "#FFFFEB" , width=55,font = "Palatino", relief="groove", bd=2, command=entertask)
entry_button.pack(padx = 13, pady=13)

delete_button=Button(window,text="Delete selected task" , bg = "#C1C1FF" ,width=55, font = "Palatino", relief="groove" , bd=2, command=deletetask)
delete_button.pack(padx = 13, pady=13)

mark_button=Button(window,text="Mark task as completed " , bg = "#FFFF6E" ,width=55, font = "Palatino", relief="groove", bd=2, command=markcompleted)
mark_button.pack(padx = 13, pady=13)

frame = tk.Frame(window)
frame.pack()
app = ProgressbarApp(frame)

#mclick = ProgressbarApp(frame)
mark_button.bind("<Button-1>",app.update_progress)


window.mainloop()

