def display_menu():
    print("To-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")


to_do_list = []


def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
        return
    
    print("Your To-Do List:")
    for index, task in enumerate(to_do_list, start=1):
        print(f"{index}. {task}")


def add_task():
    task = input("Enter a new task: ")
    to_do_list.append(task)
    print(f"Added task: {task}")


def delete_task():
    if not to_do_list:
        print("Your to-do list is empty.")
        return
    
    view_tasks()
    try:
        task_index = int(input("Enter the number of the task to delete: ")) - 1
        removed_task = to_do_list.pop(task_index)
        print(f"Removed task: {removed_task}")
    except (IndexError, ValueError):
        print("Invalid choice. Please select a valid task number.")


def main():
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
