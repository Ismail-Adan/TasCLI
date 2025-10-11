import os

if( os.path.exists('data.json') ):
    os.remove('data.json')

from models import *
from tracker import *

print("Creating a new project...")
create_project("Demo Project 1")
create_project("Demo Project 2")
create_project("Mobile App Development")
create_project("Website Redesign")

print("\n Current projects:")
for p in list_projects():
    print(f"[{p['id']}] {p['name']} - {p['progress']}")

project1 = find_project_by_id(1)
project2 = find_project_by_id(2)
project3 = find_project_by_id(3)
project4 = find_project_by_id(4)
print("\nFound project:", project1.name)

print("\nAdding tasks...")
create_task(project1, "Set up repo", "Incomplete", "Initialize version control")
create_task(project1, "Write tracker functions", "Completed", "Finish core logic")

create_task(project2, "Lorem", "Incomplete", "Ipsum")
create_task(project2, "Computer", "Completed", "Graphics training")

create_task(project3, "Setup frontend framework", "Incomplete", "Choose React or Vue.js")
create_task(project3, "Implement navigation menu", "Incomplete", "Create responsive navigation bar")
create_task(project3, "Add SEO optimization", "Completed", "Ensure proper metadata and keywords")

create_task(project4, "Update portfolio content", "Completed", "Add latest projects and skills")
create_task(project4, "Improve UI/UX", "Completed", "Redesign homepage and optimize for mobile")
create_task(project4, "Fix broken links", "Completed", "Test and repair all broken links across the site")

print("\nTasks in project1:")
for t in list_tasks(project1):
    print(f"{t.id} - {t.name} ({t.status})")

print("\nTasks in project2:")
for t in list_tasks(project2):
    print(f"{t.id} - {t.name} ({t.status})")

progress = calculate_progress(project2)
print(f"\nProgress: {progress:.1f}%")

print("\nChanging task 0 to 'Completed'...")
change_task_status(project2, 1, "Completed")

print(f"New progress: {calculate_progress(project2):.1f}%")

print("\nDeleting task 1 on project2")
delete_task(project2, 1)

for t in list_tasks(project2):
    print(f"{t.id} - {t.name}")

print("\nDeleting project 3...")
if(delete_project(3)):
    print("\nProject 3 deleted")
else:
    print("\nDeletion failed")

print("\nRemaining projects:")
for p in list_projects():
    print(f"[{p['id']}] {p['name']} - {p['progress']}")

print(Task.to_dict(find_task_by_id(project3, 3)))