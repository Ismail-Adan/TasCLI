import os

if os.path.exists("test_data.json"):
    os.remove("test_data.json")

import storage
storage.DATA_FILE = "test_data.json"
from tracker import *

proj_names = ["Demo Project 1", "Demo Project 2", "Mobile App Development", "Website Redesign"]

print("[1] Creating projects... ✅")

for name in proj_names:
    create_project(name)

projects = list_projects()
assert len(projects) == 4, "❌ Project creation failed — count mismatch"
for p in projects:
    assert p["name"] in proj_names, f"❌ Project name mismatch: {p['name']}"

print("\n[2] Adding tasks... ✅")

create_task(find_project_by_id(1), "Set up repo", "Incomplete", "Initialize version control")
create_task(find_project_by_id(1), "Write tracker functions", "Completed", "Finish core logic")

create_task(find_project_by_id(2), "Lorem", "Incomplete", "Ipsum")
create_task(find_project_by_id(2), "Computer", "Completed", "Graphics training")

create_task(find_project_by_id(3), "Setup frontend framework", "Incomplete", "Choose React or Vue.js")
create_task(find_project_by_id(3), "Implement navigation menu", "Incomplete", "Create responsive navigation bar")
create_task(find_project_by_id(3), "Add SEO optimization", "Completed", "Ensure proper metadata and keywords")

create_task(find_project_by_id(4), "Update portfolio content", "Completed", "Add latest projects and skills")
create_task(find_project_by_id(4), "Improve UI/UX", "Completed", "Redesign homepage and optimize for mobile")
create_task(find_project_by_id(4), "Fix broken links", "Completed", "Test and repair all broken links across the site")

# ✅ Check task count and details
total_tasks = sum(len(list_tasks(find_project_by_id(i))) for i in range(1, 5))
assert total_tasks == 10, f"❌ Task creation failed — found {total_tasks}, expected 10"

# 🔍 Check names/status/descriptions match
expected_task = ("Set up repo", "Incomplete", "Initialize version control")
p1_tasks = list_tasks(find_project_by_id(1))
first_task = (p1_tasks[0]["name"], p1_tasks[0]["status"], p1_tasks[0]["desc"])
assert first_task == expected_task, f"❌ Task data mismatch: {first_task} != {expected_task}"

print("\n[3] Checking progress... ✅")
project2 = find_project_by_id(2)
old_progress = calculate_progress(project2)

print("\n[4] Changing status... ✅")
change_task_status(project2, 1, "Completed")
assert project2.tasks[0].status == "Completed", "❌ Task status update failed"

new_progress = calculate_progress(project2)
assert new_progress > old_progress, "❌ Progress did not increase after completion"

print("\n[5] Deleting projects/tasks... ✅")
delete_task(project2, 1)
assert len(list_tasks(project2)) == 1, "❌ Task deletion failed"

delete_project(3)
remaining = list_projects()
assert len(remaining) == 3, "❌ Project deletion failed — count mismatch"

print("\n[6] Persistence check... ✅")
count = 0
save_projects(current_projects)
reloaded, _ = load_projects("test_data.json")

assert len(reloaded) == len(remaining), "❌ Persistence check failed — project count mismatch"
for orig, re in zip(remaining, reloaded):
    assert orig["name"] == re.name, f"❌ Persistence mismatch: {orig.name} != {re.name}"
    count += 1

print("\n✅ All tests passed successfully — system stable.")

os.remove("test_data.json")