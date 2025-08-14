import json
import os
from typing import List, Dict, Union

# Configuration
TASKS_FILE = "tasks.json"
DEFAULT_ENCODING = "utf-8"

# Type aliases
Task = Dict[str, Union[str, bool]]
TaskList = List[Task]

def load_tasks() -> TaskList:
    """Load tasks from file if it exists"""
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r', encoding=DEFAULT_ENCODING) as file:
                tasks = json.load(file)
                # Validate task structure
                for task in tasks:
                    if not isinstance(task, dict) or 'title' not in task or 'completed' not in task:
                        print("Warning: Corrupted task data found. Starting fresh.")
                        return []
                return tasks
        return []  # Return empty list if file doesn't exist
    except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
        print(f"Error loading tasks: {str(e)}")
        print("Starting with empty task list.")
        return []

def save_tasks(tasks: TaskList) -> bool:
    """Save tasks to file"""
    try:
        with open(TASKS_FILE, 'w', encoding=DEFAULT_ENCODING) as file:
            json.dump(tasks, file, indent=2)
        return True
    except IOError as e:
        print(f"Error saving tasks: {str(e)}")
        return False

def display_menu() -> None:
    """Display the main menu"""
    print("\n" + "="*50)
    print("ADVANCED TO-DO LIST APPLICATION")
    print("="*50)
    print("1. View All Tasks")
    print("2. Add New Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. View Completed Tasks")
    print("6. View Pending Tasks")
    print("7. Clear All Tasks")
    print("8. Exit")
    print("="*50)

def view_tasks(tasks: TaskList, filter_type: str = "all") -> None:
    """View tasks based on filter type"""
    if not tasks:
        print("No tasks found.")
        return
    
    filtered_tasks = []
    if filter_type == "completed":
        filtered_tasks = [task for task in tasks if task["completed"]]
        print("\nCOMPLETED TASKS:")
    elif filter_type == "pending":
        filtered_tasks = [task for task in tasks if not task["completed"]]
        print("\nPENDING TASKS:")
    else:
        filtered_tasks = tasks
        print("\nALL TASKS:")
    
    if not filtered_tasks:
        print(f"No {filter_type} tasks found.")
        return
    
    task_map = [(i, task) for i, task in enumerate(tasks) if task in filtered_tasks]
    for i, (orig_index, task) in enumerate(task_map, 1):
        status = "[Completed]" if task["completed"] else "[Pending]"
        print(f"{i}. {status} {task['title']} (#{orig_index + 1})")

def add_task(tasks: TaskList) -> None:
    """Add a new task"""
    title = input("Enter task title: ").strip()
    if title:
        new_task = {
            "title": title,
            "completed": False
        }
        tasks.append(new_task)
        if save_tasks(tasks):
            print(f"Task added: {title}")
        else:
            tasks.pop()  # Remove task if save failed
            print("Failed to save task.")
    else:
        print("Task title cannot be empty.")

def mark_task_complete(tasks: TaskList) -> None:
    """Mark a task as complete"""
    if not tasks:
        print("No tasks found.")
        return
        
    pending_tasks = [(i, task) for i, task in enumerate(tasks) if not task["completed"]]
    
    if not pending_tasks:
        print("No pending tasks to complete.")
        return
    
    print("\nPENDING TASKS:")
    for i, (orig_index, task) in enumerate(pending_tasks, 1):
        print(f"{i}. {task['title']} (#{orig_index + 1})")
    
    try:
        choice = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= choice < len(pending_tasks):
            task_index = pending_tasks[choice][0]
            tasks[task_index]["completed"] = True
            if save_tasks(tasks):
                print(f"Task completed: {tasks[task_index]['title']}")
            else:
                tasks[task_index]["completed"] = False
                print("Failed to save task status.")
        else:
            print("Invalid task number.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")

def delete_task(tasks: TaskList) -> None:
    """Delete a task"""
    if not tasks:
        print("No tasks to delete.")
        return
    
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: ")) - 1
        if 0 <= choice < len(tasks):
            removed_task = tasks.pop(choice)
            if save_tasks(tasks):
                print(f"Task deleted: {removed_task['title']}")
            else:
                tasks.append(removed_task)  # Restore task if save failed
                print("Failed to delete task.")
        else:
            print("Invalid task number.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")

def clear_all_tasks(tasks: TaskList) -> None:
    """Clear all tasks"""
    if not tasks:
        print("No tasks to clear.")
        return
    
    confirm = input("Are you sure you want to delete all tasks? (y/N): ")
    if confirm.lower() == 'y':
        old_tasks = tasks.copy()
        tasks.clear()
        if save_tasks(tasks):
            print("All tasks cleared.")
        else:
            tasks.extend(old_tasks)  # Restore tasks if save failed
            print("Failed to clear tasks.")
    else:
        print("Operation cancelled.")

def main() -> None:
    """Main application loop"""
    print("Loading tasks...")
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("Select an option (1-8): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            view_tasks(tasks, "completed")
        elif choice == '6':
            view_tasks(tasks, "pending")
        elif choice == '7':
            clear_all_tasks(tasks)
        elif choice == '8':
            print("Goodbye! Thanks for using the To-Do List app!")
            break
        else:
            print("Invalid choice. Please select a number between 1-8.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()