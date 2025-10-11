from tracker import list_projects, list_tasks, valid_statuses

def show_home_screen(current_projects):
    valid_ids = [ p.id for p in current_projects ]
    print("Current projects:")
    # List projects and associated tasks in a simplified manner
    for p in list_projects():
        print(f"[{p['id']}] {p['name']} - {p['progress']}")
        # for t in list_tasks(find_project_by_id(p['id'])):
        #     print((" "*4+f"{t['id']} {t['name']} - {t['status']}"))
    # projects_list = []
    # task_list = []
    # for project in current_projects:
    #     progress = calculate_progress(project)
    #     for t in list_tasks(project):
    #         task_list.append(f"{t['id']} {t['name']} - {t['status']}")
    #     projects_list.append({
    #         "id": project.id,
    #         "name": project.name,
    #         "progress": f"{progress:.1f}%",
    #         "tasks": task_list
    #     })    
    # print(projects_list)
    print("\n")
    print("Enter in a number from the following options")
    user_input = input("\n[1] View Project Details \n[2] Add New Project \n[3] Delete Project \n[4] Exit \n")
    try: 
        user_input = int(user_input)
        if( user_input in valid_ids ):
            return int(user_input)
    except ValueError:
        pass
    return None


def show_project_screen(project):
    print(f"[{project.id}] {project.name}")
    for t in list_tasks(project):
        print(" "*4+f"{t['id']} {t['name']} - {t['status']}")
    print("\n")
    print("Enter in a number from the following options")
    user_input = input("\n[1] Add Task \n[2] Change Status \n[3] Delete Task \n[4] Back \n")
    try: 
        user_input = int(user_input)
        if(1 <= user_input <= 4):
            return int(user_input)
    except ValueError:
        pass
    return None

def ask_for_project_name():
    project_name = input("Enter the project's name\n")
    return project_name

def ask_for_project_id(current_projects):
    valid_ids = [ p.id for p in current_projects ]
    for p in list_projects():
        print(f"[{p['id']}] {p['name']}")
    user_input = input("\nSelect a project id from the list above\n")
    try: 
        user_input = int(user_input)
        if( user_input in valid_ids ):
            return int(user_input)
    except ValueError:
        pass
    return None    

def ask_for_task_id(project):
    task_id = input("Enter a task id\n")
    try: 
        task_id = int(task_id)
        if(1 <= task_id <= project.last_task_id):
            return task_id
    except ValueError:
        pass
    return None
    
def ask_for_task_info():
    user_input_1 = input("Enter in the task name\n")
    user_input_2 = input("Enter in the task status\n")
    user_input_3 = input("Enter in the task desc\n")
    return user_input_1, user_input_2, user_input_3

# This function needs to provide the user with a dropdown of predefined statuses
def ask_for_status_change(project):
    for t in list_tasks(project):
        print(f"[{t['id']}] {t['name']} - {t['status']}")
    task_id = input("Enter the task id you wish to change status of\n")
    status = input("Enter the new status\n")
    try: 
        task_id = int(task_id)
        if(1 <= task_id <= project.last_task_id):
            if(status in valid_statuses):
                return task_id, status
    except ValueError:
        pass
    return None   

# print(show_home_screen())

# print(show_project_screen())

# print(ask_for_project_name())

# print(ask_for_project_id())

# print(ask_for_status_change(find_project_by_id(1)))
# print(show_project_screen(find_project_by_id(1)))
