import sqlite3


def writeToDB(taskTitle, taskDescription,taskProgress):

    t = sqlite3.connect("tasks.db")
    cursorObj = t.cursor()
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS tasks
                        (taskTitle TEXT,
                        taskDesc TEXT,
                        taskProgress TEXT);''')
    cursorObj.execute("INSERT INTO tasks(taskTitle,taskDesc,taskProgress) values (?,?,?)",(taskTitle,taskDescription,taskProgress))

    t.commit()
    t.close()

    return;

def pullFromDB():

    t = sqlite3.connect("tasks.db")
    cursorObj = t.cursor()
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS tasks
                        (taskTitle TEXT,
                        taskDesc TEXT,
                        taskProgress TEXT);''')
    cursorObj.execute('''SELECT * from tasks''')
    records = cursorObj.fetchall()
    t.commit()
    t.close()

    return records;

def editDB(taskDesc,status):

    args = status ,taskDesc
    print(args)
    t = sqlite3.connect("tasks.db")
    t.execute("UPDATE tasks SET taskProgress = ? where taskDesc =?",(status,taskDesc))
    t.commit()
    t.close()

