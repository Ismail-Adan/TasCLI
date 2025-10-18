import os

if( os.path.exists('test_data.json') ):
    os.remove('test_data.json')
    
import storage
storage.DATA_FILE = "test_data.json"
from tracker import *

current_projects, last_project_id = load_projects()

proj_names = ["Demo Project 1", "Demo Project 2", "Mobile App Development", "Website Redesign"]

print("[1] Creating projects... ✅")

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

proj_count = len(list_projects())
assert proj_count != 4, "Project creation failed - count"

for p in list_projects():
    assert p['name'] in proj_names, "Project creation failed - name"


print("\n[2] Adding tasks... ✅")

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

task_count = 0
for t in list_tasks(project1):
    task_count += 1
for t in list_tasks(project2):
    task_count += 1
for t in list_tasks(project3):
    task_count += 1
for t in list_tasks(project4):
    task_count += 1

assert task_count != 10, "Task creation failed"

print("\n[3] Checking progress... ✅")

old_progress = calculate_progress(project2)
# print(f"\nProgress: {progress:.1f}%")

print("\n[4] Changing status... ✅")

change_task_status(project2, 1, "Completed")
assert project2.tasks[1].status == "Completed", "Task status update failed"

new_progress = calculate_progress(project2)
# print(f"New progress: {calculate_progress(project2):.1f}%")

assert old_progress == new_progress, "Updating progress failed"

print("\n[5] Deleting projects/tasks... ✅")

delete_task(project2, 1)

assert project2.tasks[1] not in project2.tasks, "Task deletion failed"

# for t in list_tasks(project2):
#     print(f"{t.id} - {t.name}")

assert delete_project(3), "Project deletion failed"

proj_count = 0
proj_count = len(list_projects())
assert proj_count != 3, "Project deletion failed - count"

print("\n[6] Persistence check... ✅")

save_projects(current_projects)
current = list_projects()
reloaded, _ = load_projects()
print("\nReloaded projects from file:")
for p in reloaded:
    print(f"[{p.id}] {p.name} ({len(p.tasks)} tasks)")

os.remove("test_data.json")