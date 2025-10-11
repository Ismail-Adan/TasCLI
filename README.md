# 🗂️ TasCLI — Python Project & Task Tracker  

A lightweight, terminal-based project tracker built entirely in Python.  
Designed for learning clean architecture, modular design, and data persistence using JSON.  

---

## 🚀 Features  

- 🧱 **Projects & Tasks:** Create, view, and delete projects — each with its own list of tasks.  
- 🔁 **Persistent Storage:** All data is saved to a `data.json` file using `json` serialization.  
- ⚙️ **Dynamic Progress Tracking:** Calculates project progress based on completed tasks.  
- 🧩 **Modular Design:**  
  - `models.py` → defines `Project` and `Task` classes.  
  - `storage.py` → handles JSON saving/loading.  
  - `tracker.py` → main logic layer (create, update, delete, list).  
  - `ui.py` → command-line user interface functions.  
  - `main.py` → program entry point that connects everything.  
- 🧠 **Error-Resilient:** Validates user inputs and gracefully handles missing data.  
- 🎨 *(coming soon)*: Beautiful terminal interface with **Rich** library panels and layout.  

---

## 🧰 Tech Stack  

| Layer | Responsibility | Key Modules |
|--------|----------------|--------------|
| Data Model | Project and Task structures | `models.py` |
| Persistence | Save/load from JSON | `storage.py` |
| Core Logic | Add/edit/delete operations | `tracker.py` |
| User Interface | Command-line screens | `ui.py` |
| Entry Point | App flow control | `main.py` |

---

## 💡 How It Works  

1. When the app starts, it loads saved projects from `data.json` (if it exists).  
2. The user is shown a **Home screen** with all projects and their progress.  
3. Users can:  
   - Add a new project  
   - View an existing project and manage its tasks  
   - Delete projects or tasks  
4. All changes are automatically persisted back to `data.json`.  

---

## 📂 Project Structure  

```
TasCLI/
│
├── models.py        # Defines Project & Task classes
├── storage.py       # JSON saving/loading logic
├── tracker.py       # Core project/task manipulation functions
├── ui.py            # User interaction (CLI)
├── main.py          # App entry point
├── tester.py        # Manual regression testing
└── data.json        # Auto-generated data file
```

---

## 🧭 Planned Enhancements  

- 🎨 **Rich-based Interface:** visually structured panels for projects & tasks.  
- 🔍 **Search & Filtering:** quickly find tasks or projects by name or status.  
- 🧰 **Automated Regression Testing:** verify all core functions after each update.  
- 🕹️ **Keyboard Navigation (optional):** move between “screens” without typing numeric options.  

---

## 🧑‍💻 Author  

**Ismail Jama Adan**  
A computer student building real-world, maintainable projects while learning about architecture, modularity, and UI/UX.  

