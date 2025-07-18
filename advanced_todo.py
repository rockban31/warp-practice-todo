import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file if it exists"""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("📝 ADVANCED TO-DO LIST APPLICATION")
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

def view_tasks(tasks, filter_type="all"):
    """View tasks based on filter type"""
    if not tasks:
        print("No tasks found.")
        return
    
    filtered_tasks = []
    if filter_type == "completed":
        filtered_tasks = [task for task in tasks if task["completed"]]
        print("\n✅ COMPLETED TASKS:")
    elif filter_type == "pending":
        filtered_tasks = [task for task in tasks if not task["completed"]]
        print("\n⏳ PENDING TASKS:")
    else:
        filtered_tasks = tasks
        print("\n📋 ALL TASKS:")
    
    if not filtered_tasks:
        print(f"No {filter_type} tasks found.")
        return
    
    for index, task in enumerate(filtered_tasks, start=1):
        status = "✅" if task["completed"] else "⏳"
        print(f"{index}. {status} {task['title']}")

def add_task(tasks):
    """Add a new task"""
    title = input("Enter task title: ").strip()
    if title:
        new_task = {
            "title": title,
            "completed": False
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"✅ Task added: {title}")
    else:
        print("❌ Task title cannot be empty.")

def mark_task_complete(tasks):
    """Mark a task as complete"""
    pending_tasks = [task for task in tasks if not task["completed"]]
    
    if not pending_tasks:
        print("No pending tasks to complete.")
        return
    
    print("\n⏳ PENDING TASKS:")
    for index, task in enumerate(pending_tasks, start=1):
        print(f"{index}. {task['title']}")
    
    try:
        choice = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= choice < len(pending_tasks):
            # Find the task in the main list and mark it complete
            for task in tasks:
                if task["title"] == pending_tasks[choice]["title"] and not task["completed"]:
                    task["completed"] = True
                    save_tasks(tasks)
                    print(f"✅ Task completed: {task['title']}")
                    break
        else:
            print("❌ Invalid task number.")
    except (ValueError, IndexError):
        print("❌ Invalid input. Please enter a valid number.")

def delete_task(tasks):
    """Delete a task"""
    if not tasks:
        print("No tasks to delete.")
        return
    
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: ")) - 1
        if 0 <= choice < len(tasks):
            removed_task = tasks.pop(choice)
            save_tasks(tasks)
            print(f"🗑️ Task deleted: {removed_task['title']}")
        else:
            print("❌ Invalid task number.")
    except (ValueError, IndexError):
        print("❌ Invalid input. Please enter a valid number.")

def clear_all_tasks(tasks):
    """Clear all tasks"""
    if not tasks:
        print("No tasks to clear.")
        return
    
    confirm = input("Are you sure you want to delete all tasks? (y/N): ")
    if confirm.lower() == 'y':
        tasks.clear()
        save_tasks(tasks)
        print("🗑️ All tasks cleared.")
    else:
        print("Operation cancelled.")

def main():
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
            print("👋 Goodbye! Thanks for using the To-Do List app!")
            break
        else:
            print("❌ Invalid choice. Please select a number between 1-8.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
