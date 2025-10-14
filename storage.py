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

DATA_FILE = "data.json"

def save_projects(projects, filename=None):
    filename = filename or DATA_FILE
    last_project_id = 0
    with open(filename, 'w') as file:
        Project_Dicts = []
        for project in projects:
            Project_Dicts.append(project.to_dict())
            last_project_id = project.id
        data = {'last_project_id': last_project_id, 'projects': Project_Dicts}
        json.dump(data, file, indent=4) 

def load_projects(filename=None):
    filename = filename or DATA_FILE
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
