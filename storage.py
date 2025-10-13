# ==================================================================== #
#  File: storage.py                                                    #       
#  Author: Ismail Adan                                                 #
#  Project: TasCLI                                                     #
#  Description: Handles reading and writing of data                    #
#               between files and persistent storage (JSON file).      #
#               Includes functions for loading, saving,                #
#               and ensuring data consistency.                         #
#  Created: October 2025                                               #
#  Notes:                                                              #
#      - Used explicitly by tracker.py.                                #
# ==================================================================== #

import json
import os
from models import Project, Task

def save_projects(projects, filename="data.json"):
    last_project_id = 0
    with open(filename, 'w') as file:
        Project_Dicts = []
        for project in projects:
            Project_Dicts.append(project.to_dict())
            last_project_id = project.id
        data = {'last_project_id': last_project_id, 'projects': Project_Dicts}
        json.dump(data, file, indent=4) 

def load_projects(filename="data.json"):
    if( os.path.exists(filename) ):
        with open(filename, 'r') as file:
            Project_list = []
            data = json.load(file)
            last_project_id = data.get("last_project_id", 0)
            Projects = data.get("projects", [])
            for project in Projects:
                Project_list.append(Project.from_dict(project))
            return Project_list, last_project_id
    return [], 0



# project1 = Project("Build MVP", id=1)
# task1 = Task(1, "Download Rich via pip")
# task2 = Task(2, "Start drafting")
# project1.add_task(task1)
# project1.add_task(task2)

# # Project 2
# project2 = Project("Finish Assignment", id=2)
# project2.add_task(Task(1, "Write introduction"))
# project2.add_task(Task(2, "Add diagrams"))
# project2.add_task(Task(3, "Proofread and submit"))

# # Project 3
# project3 = Project("Learn Python CLI", id=3)
# project3.add_task(Task(1, "Set up virtualenv"))
# project3.add_task(Task(2, "Try argparse for commands"))
# project3.add_task(Task(3, "Experiment with rich tables"))

# project4 = Project("Learn Python CLI", id=9000)

# projects = [project1, project2, project3, project4]
# save_projects(projects)

# projects = []
# projects, last_project_id = load_projects()
# for project in projects:
#     print(Project.to_dict(project))
# print(last_project_id)