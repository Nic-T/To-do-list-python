from tkinter import *
from addTask import *
from modules import *
from sql import *
import threading

task = Task()

def main():
 
    root = Tk()
    root.title("To Do List")
    root.geometry("960x540")

    Menu1= Frame(root, bg="grey")
    Menu1.place(relwidth=0.20 , relheight=1,relx=0,rely=0)

    addTask = Button(Menu1,bg='#37bf60',text='Add Task',font="Bahnschrift 20",fg='#5eefff',bd=1,command= lambda: AddTask(), justify=CENTER)
    addTask.place(relwidth=1,relheight=0.20,relx=0,rely=0)

    completedTasks =Button(Menu1, bg='#37bf60', text='Completed Tasks' ,font="Bahnschrift 20",fg='#5eefff',bd=1, justify=CENTER)
    completedTasks.place(relwidth=1,relheight=0.20,relx=0,rely=0.20)
    
    viewTasks = Button(Menu1,bg='#37bf60',text='View Tasks' ,font="Bahnschrift 20",fg='#5eefff',bd=1, justify=CENTER)
    viewTasks.place(relwidth=1,relheight=0.20,relx=0,rely=0.40)

    expiredTasks= Button(Menu1,bg='#37bf60',text='Expired Tasks' ,font="Bahnschrift 20",fg='#5eefff',bd=1, justify=CENTER)
    expiredTasks.place(relwidth=1,relheight=0.20,relx=0,rely=0.60)

    deleteTask= Button(Menu1,bg='#37bf60',text='Delete Task' ,font="Bahnschrift 20",fg='#5eefff',bd=1, justify=CENTER)
    deleteTask.place(relwidth=1,relheight=0.20,relx=0,rely=0.80)

    
   
    space = Canvas(root,bg='red')
    space.place(relwidth=0.80,relheight=1,relx=0.20,rely=0)
    
    
 
    help=Frame(space,bg='blue')
    help.pack(fill=BOTH,expand=TRUE)
    help.columnconfigure(0,weight=2)

    space.configure(scrollregion=space.bbox("all"))

    print(space.bbox('all'))

    # Also, you do not grid() widgets to the Canvas; those should go into the Frame within the Canvas. http://effbot.org/tkinterbook/canvas.htm


    def updateData():
        myData=pullFromDB()

        if len(task.taskTitle) != len(myData):
            task.taskTitle= [None] *(len(myData))
            task.taskDescription= [None]* (len(myData))
            task.taskProgress= [None]* (len(myData))
            button = [None]*(len(myData))

            for i in range(len(myData)):
                task.taskTitle[i]=myData[i][0]
                task.taskDescription[i]=myData[i][1]
                task.taskProgress[i]=myData[i][2]
                button[i] = Button(help,text=task.taskTitle[i],font="Bahnschrift 20")
                button[i].grid(row=i,column=0,sticky="nesw")
                  
        
        root.after(1000,updateData)
        return;
    
    updateData()





    root.mainloop()





        

