from tkinter import *
from buttons import *
from modules import *
from sql import *


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

    sb= Scrollbar(root,orient='vertical',command=space.yview)
    
    space.config(yscrollcommand = sb.set)
    sb.pack(side = RIGHT,fill=Y)

    

    help=Frame(space,bg='blue')
    help.pack(fill=BOTH,expand=TRUE)
    help.columnconfigure(0,weight=2)

    space.create_window((1,1),window=help,anchor='nw',width=1320 )

    def updateData():
        myData=pullFromDB()
        
        task.taskTitle= [None] *(len(myData))
        task.taskDescription= [None]* (len(myData))
        task.taskProgress= [None]* (len(myData))
        button = [None]*(len(myData))

        for i in range(len(myData)):
            task.taskTitle[i]=myData[i][0]
            task.taskDescription[i]=myData[i][1]
            task.taskProgress[i]=myData[i][2]
            if(task.taskProgress[i]=='open'):
                button[i] = Button(help,text=task.taskTitle[i],font="Bahnschrift 20",anchor='w',command = lambda: showDescription(task.taskDescription[i],task.taskProgress[i],i))
                button[i].grid(row=i,column=0,sticky="nesw",columnspan=100)
            elif(task.taskProgress[i] =='finished' and button[i] != None):
                print('Yes')
                button[i].grid_forget()
            print(button[i],task.taskProgress[i])

        space.configure(scrollregion=space.bbox("all"))
        root.after(1000,updateData)
        return;
    
    updateData()

   





    root.mainloop()

def showDescription(taskDesc,taskP,i):
    
    scene =Toplevel(height=500, width=800)
    scene.title('Task')

    desc=Text(scene)
    desc.insert(INSERT,taskDesc)
    desc.pack(fill=BOTH,expand=TRUE)

    completeTask=Button(scene,command= lambda :editDB(taskDesc,'finished'),text='Complete Task')
    completeTask.pack(side=RIGHT)
    
    return ;






        

