from tkinter import *
from addTask import *
from modules import *

def main():


    root = Tk()
    root.title("To Do List")
    root.geometry("1920x1080")

    Menu1= Frame(root, bg="grey")
    Menu1.place(relwidth=0.15 , relheight=1,relx=0,rely=0)

    addTask = Button(Menu1,bg='#37bf60',text='Add Task',font="Bahnschrift 20",fg='#5eefff',bd=1,command= lambda: AddTask())
    addTask.place(relwidth=1,relheight=0.15,relx=0,rely=0 )

    completedTasks =Button(Menu1, bg='#37bf60', text='Completed Tasks' ,font="Bahnschrift 20",fg='#5eefff',bd=1)
    completedTasks.place(relwidth=1,relheight=0.15,relx=0,rely=0.15)
    
    viewTasks = Button(Menu1,bg='#37bf60',text='View Tasks' ,font="Bahnschrift 20",fg='#5eefff',bd=1)
    viewTasks.place(relwidth=1,relheight=0.15,relx=0,rely=0.30)
   
    space = Message(root, bg= "brown")
    space.place(relwidth=0.85,relheight=1,relx=0.15,rely=0)
    

    root.mainloop()