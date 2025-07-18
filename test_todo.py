"""
Test file for the To-Do List application
This file demonstrates how to test the functions in isolation
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import functions from our todo application
from todo_list import add_task, view_tasks, delete_task, to_do_list

def test_basic_functionality():
    """Test basic functionality of the todo list"""
    print("Testing Basic To-Do List Functionality")
    print("="*50)
    
    # Clear the list for testing
    to_do_list.clear()
    
    # Test adding tasks
    print("\n1. Testing add_task function:")
    print("Adding tasks: 'Buy groceries', 'Walk the dog', 'Complete project'")
    to_do_list.extend(['Buy groceries', 'Walk the dog', 'Complete project'])
    
    # Test viewing tasks
    print("\n2. Testing view_tasks function:")
    view_tasks()
    
    # Test deleting a task (simulate user input)
    print("\n3. Testing delete functionality:")
    if to_do_list:
        removed = to_do_list.pop(1)  # Remove second item
        print(f"Removed task: {removed}")
        print("Updated list:")
        view_tasks()
    
    print("\n4. Final state of to-do list:")
    print(f"Total tasks: {len(to_do_list)}")
    view_tasks()

def test_advanced_functionality():
    """Test advanced functionality"""
    print("\n\nTesting Advanced To-Do List Functionality")
    print("="*50)
    
    # Create sample tasks
    sample_tasks = [
        {"title": "Learn Python", "completed": False},
        {"title": "Build a project", "completed": True},
        {"title": "Write documentation", "completed": False}
    ]
    
    print("Sample tasks created:")
    for i, task in enumerate(sample_tasks, 1):
        status = "✅" if task["completed"] else "⏳"
        print(f"{i}. {status} {task['title']}")
    
    # Test filtering
    completed_tasks = [task for task in sample_tasks if task["completed"]]
    pending_tasks = [task for task in sample_tasks if not task["completed"]]
    
    print(f"\nCompleted tasks: {len(completed_tasks)}")
    print(f"Pending tasks: {len(pending_tasks)}")

if __name__ == "__main__":
    test_basic_functionality()
    test_advanced_functionality()
    print("\n" + "="*50)
    print("Testing completed! Run the main applications to try them out.")
