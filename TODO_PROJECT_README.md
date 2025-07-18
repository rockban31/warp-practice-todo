# To-Do List Application with Functions

A simple Python-based to-do list application that demonstrates proper function organization and structure.

## Project Structure

```
practise/
├── todo_list.py          # Basic to-do list application
├── advanced_todo.py      # Advanced version with persistence
├── test_todo.py          # Test file for basic functionality
├── TODO_PROJECT_README.md # This file
└── tasks.json            # Created automatically to store tasks
```

## Features

### Basic Version (`todo_list.py`)
- ✅ Add new tasks
- ✅ View all tasks
- ✅ Delete tasks
- ✅ Simple menu interface
- ✅ Function-based structure

### Advanced Version (`advanced_todo.py`)
- ✅ All basic features
- ✅ Mark tasks as complete/incomplete
- ✅ View completed tasks separately
- ✅ View pending tasks separately
- ✅ Persistent storage (JSON file)
- ✅ Clear all tasks option
- ✅ Enhanced UI with emojis
- ✅ Input validation

## How to Run

### Basic Version
```bash
python todo_list.py
```

### Advanced Version
```bash
python advanced_todo.py
```

### Run Tests
```bash
python test_todo.py
```

## Function Structure

### Basic Version Functions:
- `display_menu()` - Shows the main menu
- `view_tasks()` - Displays all tasks
- `add_task()` - Adds a new task
- `delete_task()` - Removes a task
- `main()` - Main application loop

### Advanced Version Functions:
- `load_tasks()` - Loads tasks from JSON file
- `save_tasks()` - Saves tasks to JSON file
- `display_menu()` - Shows the enhanced menu
- `view_tasks(filter_type)` - Displays tasks with filtering
- `add_task()` - Adds a new task with persistence
- `mark_task_complete()` - Marks tasks as complete
- `delete_task()` - Removes tasks with persistence
- `clear_all_tasks()` - Clears all tasks with confirmation
- `main()` - Main application loop

## Learning Objectives Achieved

1. **Function Organization**: Code is properly separated into logical functions
2. **Data Management**: Tasks are stored and managed efficiently
3. **User Interface**: Clean, intuitive menu system
4. **Error Handling**: Input validation and error management
5. **File Operations**: Reading and writing data (advanced version)
6. **Code Reusability**: Functions can be imported and tested separately

## Usage Examples

### Adding Tasks
1. Run the application
2. Select option 2 (Add Task)
3. Enter your task description
4. Task is added to the list

### Viewing Tasks
1. Select option 1 (View Tasks)
2. All tasks are displayed with numbers
3. Advanced version shows completion status

### Completing Tasks (Advanced Version)
1. Select option 3 (Mark Complete)
2. Choose the task number to complete
3. Task is marked with ✅ status

## Technical Details

- **Language**: Python 3.x
- **Data Storage**: In-memory list (basic) / JSON file (advanced)
- **Input Validation**: Try-catch blocks for error handling
- **UI**: Console-based with emoji indicators (advanced)

## Next Steps for Enhancement

1. Add due dates for tasks
2. Implement task priorities
3. Add categories/tags
4. Create a GUI version
5. Add task search functionality
6. Implement task editing
7. Add task statistics
8. Create backup/restore functionality

## Testing

The `test_todo.py` file demonstrates:
- Function isolation testing
- Data manipulation testing
- Basic functionality validation

Run the tests to see how the functions work independently of the main application.

---

*This project is part of learning Python function organization and basic application structure.*
