class Project:
    def __init__(self, name, id=None, last_task_id=0):
        self.id = id
        self.name = name
        self.last_task_id = last_task_id
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.last_task_id = task.id

    def to_dict(self):
        tasks = []
        for task in self.tasks:
            tasks.append(task.to_dict())
        return {
            'id': self.id,
            'name': self.name,
            'tasks': tasks
        }   
    
    @classmethod
    def from_dict(cls, dictionary):
        project = cls(dictionary['name'], dictionary['id'])        
        for task in dictionary.get("tasks"):
            task_obj = Task.from_dict(task)    
            project.add_task(task_obj)
        return project
  
        
        
class Task:
    def __init__(self, id, name, status="To Do", progress=0, desc="", comments=None):
        self.name = name
        self.id = id
        self.status = status 
        self.progress = progress
        self.desc = desc
        self.comments = comments if comments else []
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'progress': self.progress,
            'desc': self.desc,
            'comments': self.comments
        }
    
    @classmethod
    def from_dict(cls, dictionary):
        task = cls(dictionary["id"], dictionary["name"], dictionary["status"],
                     dictionary["progress"], dictionary["desc"], dictionary["comments"])
        return task
    
# project = Project("Build MVP", id=7)

# task1 = Task(1, "Download Rich via pip")
# task2 = Task(2, "Start drafting")
# task3 = Task(-1111, "XXXXXXXXXX")

# project.add_task(task1)
# project.add_task(task2)
# project.add_task(task3)

# print(project.to_dict())
# print("\n")
# project_dict = project.to_dict()
# print(project_dict)

# new_project = Project.from_dict(project_dict)
# print(new_project.name)
# print(new_project.id)
# for task in new_project.tasks:
#     print(task.id, task.name)

# print(project.last_task_id)


