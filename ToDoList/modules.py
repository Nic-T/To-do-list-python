import json
class Task:
    taskTitle  = ""
    taskDescription= ""  
    taskProgress="" #finished , failed , open


    def convert(self,taskTitle, taskDescription,taskProgress):
        
        taskDict = json.load(open('data.json'))

        taskDict = [taskDict]

        taskDict.append({
            'taskTitle': taskTitle,
            'taskDescription': taskDescription,
            'taskProgress': taskProgress
        })

        with open('data.json', 'w') as file:
            json.dump(taskDict,file)

        return ;
task = Task()



