from tkinter import *
import json
from modules import *


def AddTask() :

    addTaskWindow = Toplevel(height=500, width=800)
    addTaskWindow.maxsize(800,500)
    addTaskWindow.minsize(800,500)
    addTaskWindow.title('Add Task')

    taskTitle = Label(addTaskWindow,text="Task Title", font ="Bahnschrift 10")
    taskTitle.place( relx= 0.1, rely=0.1 )
    
    taskTitleField = Entry(addTaskWindow)
    taskTitleField.place(relx= 0.14,rely=0.1,width="300")
    

    taskDescribe = Label(addTaskWindow,text="Describe or add notes to your task",font="Bahnschrift 10")
    taskDescribe.place(relx= 0.1,rely=0.15)

    taskDescribeField = Text(addTaskWindow, height="20")
    taskDescribeField.place(relx=0.1,rely=0.20)

    submitButton= Button(addTaskWindow, text="Submit",bd=1, command =lambda  : Submit(taskTitleField.get(),taskDescribeField.get("1.0",END),addTaskWindow))
    submitButton.place(relx=0.8,rely=0.9,width=70)

    addTaskWindow.mainloop()

    
    return ""

def Submit(taskName,taskDescribe,addTaskWindow):

    task.taskTitle.append(taskName)
    task.taskDescription.append(taskDescribe)
    task.taskProgress.append("open")
    task.convert(task.taskTitle,task.taskDescription,task.taskProgress)
    
    

    return addTaskWindow.destroy() ;

