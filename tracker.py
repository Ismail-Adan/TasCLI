# ==================================================================== #
#  File: tracker.py                                                    #       
#  Author: Ismail Adan                                                 #
#  Project: TasCLI                                                     #
#  Description: Core logic layer controlling projects and tasks.       #
#               Manages in-memory state and syncs with JSON storage.   #
#  Created: October 2025                                               #
#  Notes:                                                              #
#      - current_projects and last_project_id are global state.        #
#      - Automatically loads or initializes data.json on import.       #
# ==================================================================== #

from models import Project, Task
from storage import *

current_projects, last_project_id = load_projects()

valid_statuses = ["To do", "In progress", "Completed"]

def create_project(name):
    global last_project_id
    last_project_id += 1
    new_project = Project(name, id=last_project_id)
    current_projects.append(new_project)
    save_projects(current_projects)

def create_task(project, name, status, desc):
    task = Task((project.last_task_id + 1), name, status, 0, desc)
    Project.add_task(project,task)
    save_projects(current_projects)

def change_task_status(project, task_id, status):
    result = False
    for task in project.tasks:
        if(task.id == task_id):
            task.status = status
            result = True 
            break
    if (result): save_projects(current_projects)
    return result  

def delete_task(project, task_id):
    result = False
    for task in project.tasks:
        if(task.id == task_id):
            project.tasks.remove(task)
            result = True 
            break
    if (result): save_projects(current_projects)
    return result  

def delete_project(project_id):
    result = False
    for project in current_projects:
        if(project.id == project_id):
            current_projects.remove(project)    
            result = True 
            break
    if (result): save_projects(current_projects)
    return result  

def list_projects():
    projects_list = []
    for project in current_projects:
        # projects_list.append(project)
        progress = calculate_progress(project)
        projects_list.append({
            "id": project.id,
            "name": project.name,
            "progress": f"{progress:.1f}%"
        })    
    return projects_list

def list_tasks(project):
    tasks_list = []
    for task in project.tasks:
        tasks_list.append({
            "id": task.id,
            "name": task.name,
            "status": task.status,
            "desc": task.desc
        }) 
    return tasks_list
    
def calculate_progress(project):
    total_tasks = 0
    completed_tasks = 0
    for task in project.tasks:
        total_tasks += 1
        if(task.status == "Completed"):
            completed_tasks += 1
    if(total_tasks == 0):
        return 0
    progress = (completed_tasks / total_tasks ) * 100
    project.progress = progress
    return progress

def find_project_by_id(project_id):
    for project in current_projects:
        if(project.id == project_id):
            return (project) 
    return "Project not found"

def find_task_by_id(project, task_id):
    for task in project.tasks:
        if(task.id == task_id):
            return (task) 
    return "Task not found"

# def filter_tasks_by_status()

# def search()

# rename_project()

# rename_task()


    
