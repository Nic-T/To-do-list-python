import json
class Task:
    taskTitle = []
    taskDescription = []
    taskProgress= [] #finished , failed , open

    def convert(self,taskTitle, taskDescription,taskProgress):

        jsonTaskTitle = json.dumps(taskTitle)
        jsonTaskDescription = json.dumps(taskDescription)
        jsonTaskProgress = json.dumps(taskProgress)

        print(jsonTaskTitle,jsonTaskDescription,jsonTaskProgress)

        with open('data.json', 'w') as outfile:
            outfile.write(jsonTaskTitle)
            outfile.write(jsonTaskDescription)
            outfile.write(jsonTaskProgress)

        return;
task = Task()



