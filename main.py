# ==================================================================== #
#  File: main.py                                                       #       
#  Author: Ismail Adan                                                 #
#  Project: TasCLI                                                     #
#  Description: Entry point for TasCLI,                                #
#               controls the flow between the different programs.      #
#               Connects UI with tracker functions                     #
#  Created: October 2025                                               #
#  Notes:                                                              #
#      - Imports all logic from tracker and ui                         #
#      - Ensure projects are saved before exit                         #
# ==================================================================== #

from tracker import *
from ui import *

while True:
    choice = show_home_screen(current_projects)
    # 1 = View Project Details
    if(choice == 1):
        project_id = ask_for_project_id(current_projects)
        project = find_project_by_id(project_id)
        choice2 = show_project_screen(project)
        # 1 = Create task
        if(choice2 == 1):
            name, status, desc = ask_for_task_info()
            create_task(project, name, status, desc)
        # 2 = Change status
        elif(choice2 == 2):
            task_id, status = ask_for_status_change(project)
            change_task_status(project, task_id, status)
        # 3 = Delete task
        elif(choice2 == 3):
            task_id = ask_for_task_id(project)
            delete_task(project, task_id)
        # 4 = Back
        elif(choice2 == 4):
            show_home_screen(current_projects)  
    # 2 = Add New Project                   
    elif(choice == 2):
        project_name = ask_for_project_name()
        create_project(project_name)
    # 3 = Delete Project             
    elif(choice == 3):
        project_id = ask_for_project_id(current_projects)
        delete_project(project_id)
    # 4 = Exit             
    elif(choice == 4):
        save_projects(current_projects)
        break




        




