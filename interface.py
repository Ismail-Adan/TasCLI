# ==================================================================== #
#  File: interface.py                                                  #       
#  Author: Ismail Adan                                                 #
#  Project: TasCLI                                                     #
#  Description: Console-based user interface for TasCLI.               #
#               Displays menus, captures user input,                   #
#               and delegates logic to tracker.py.                     #
#  Created: October 2025                                               #
#  Notes:                                                              #
#                                                                      #
# ==================================================================== #

from tracker import list_projects, list_tasks, valid_statuses
import time
from rich.live import Live
from rich import print
from console import console
from rich.panel import Panel
from rich.table import Table

# Helper methods
def print_header(title):
    console.print(f"[bold blue]{title}[/bold blue]")

def print_divider():
    console.rule()

def print_success(msg):
    console.print(f"[green]{msg}[/green]")

def print_error(msg):
    console.print(f"[red]{msg}[/red]")

def run_interface(current_projects):
    table = Table(show_footer=True)
    print(Panel.fit("[A] Add Project                  [S] Search                 [Q] Quit"))

    with Live(table, auto_refresh=True, refresh_per_second=4):
        # Clear table before each update to avoid stacking tables
        table.columns.clear()
        table.rows.clear()

        # Setting up data
        table.add_column("Projects", footer="[N] Next  [P] Previous [E] Edit", style="cyan", no_wrap=True)
        table.add_column("Tasks", footer="[T] Add Task  [C] Change Status", style="green", no_wrap=True)

        # Populate the table
        for p in list_projects():
            table.add_row(f"[{p['id']}] {p['name']} - {p['progress']}")
        if table.rows: 
            console.print(table)
        else:
            console.print("[i]No data...[/i]")

def show_home_screen(current_projects):
    print(Panel.fit("[A] Add Project                  [S] Search                 [Q] Quit"))
    # print_header("Current projects:")
    # List projects and associated tasks in a simplified manner
    table = Table(show_footer=True)
    table.add_column("Projects", footer="[N] Next  [P] Previous [E] Edit", style="cyan", no_wrap=True)
    table.add_column("Tasks", footer="[T] Add Task  [C] Change Status", style="green", no_wrap=True)
    for p in list_projects():
        # console.print(f"[blue][{p['id']}] {p['name']} - {p['progress']}")
        table.add_row(f"[{p['id']}] {p['name']} - {p['progress']}")
        # for t in list_tasks(find_project_by_id(p['id'])):
        #     print((" "*4+f"{t['id']} {t['name']} - {t['status']}"))
    if table.rows: 
        console.print(table)
    else:
        console.print("[i]No data...[/i]")
    print_divider()
    print("\n")
    console.print("Enter in a number from the following options")
    user_input = input("\n[1] View Project Details \n[2] Add New Project \n[3] Delete Project \n[4] Exit \n")
    return user_input

def show_project_screen(project):
    # console.print(f"[{project.id}] {project.name}")
    console.print(f"Project: {project.name}")
    console.print(f"ID: {project.id}")
    for t in list_tasks(project):
        console.print("[green]"*4+f"    {t['id']} {t['name']} - {t['status']}")
    print_divider()
    print("\n")
    print_header("Enter in a number from the following options")
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
        console.print(f"{p['id']} {p['name']}")
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
        console.print(f"{t['id']} {t['name']} - {t['status']}")
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
