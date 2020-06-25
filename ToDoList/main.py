from tkinter import *
from addTask import *
from modules import *

def main():


    root = Tk()
    root.title("To Do List")
    root.geometry("1920x1080")

    Menu1= Frame(root, bg="grey")
    Menu1.place(relwidth=0.20 , relheight=1,relx=0,rely=0)

    addTask = Button(Menu1,bg='#37bf60',text='Add Task',font="Bahnschrift 20",fg='#5eefff',bd=1,command= lambda: AddTask(), justify=CENTER)
    addTask.place(relwidth=1,relheight=0.20,relx=0,rely=0)

    completedTasks =Button(Menu1, bg='#37bf60', text='Completed Tasks' ,font="Bahnschrift 20",fg='#5eefff',bd=1, justify=CENTER)
    completedTasks.place(relwidth=1,relheight=0.20,relx=0,rely=0.20)
    
    viewTasks = Button(Menu1,bg='#37bf60',text='View Tasks' ,font="Bahnschrift 20",fg='#5eefff',bd=1, justify=CENTER)
    viewTasks.place(relwidth=1,relheight=0.20,relx=0,rely=0.40)
   
    space = Message(root, bg= "brown")
    space.place(relwidth=0.80,relheight=1,relx=0.20,rely=0)
    

    root.mainloop()