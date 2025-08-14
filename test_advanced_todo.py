import unittest
from unittest import mock
import os
import json
from advanced_todo import (
    load_tasks,
    save_tasks,
    add_task,
    delete_task,
    mark_task_complete,
    clear_all_tasks,
    view_tasks,
)

class TestAdvancedTodo(unittest.TestCase):
    def setUp(self):
        self.tasks_file = "test_tasks.json"
        self.tasks = []
        # Ensure the tasks file is clean before each test
        if os.path.exists(self.tasks_file):
            os.remove(self.tasks_file)

    def tearDown(self):
        # Clean up the tasks file after each test
        if os.path.exists(self.tasks_file):
            os.remove(self.tasks_file)

    def test_load_save_tasks(self):
        # 1. Test saving tasks
        self.tasks = [{"title": "Test Task", "completed": False}]
        save_tasks(self.tasks)
        self.assertTrue(os.path.exists(self.tasks_file))

        # 2. Test loading tasks
        loaded_tasks = load_tasks()
        self.assertEqual(self.tasks, loaded_tasks)

    def test_add_task(self):
        with mock.patch('builtins.input', return_value='New Task'):
            add_task(self.tasks)
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["title"], "New Task")

    def test_delete_task(self):
        self.tasks = [{"title": "Task 1", "completed": False}, {"title": "Task 2", "completed": False}]
        # Simulate user input '1' to delete the first task
        with mock.patch('builtins.input', return_value='1'):
            delete_task(self.tasks)
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["title"], "Task 2")

    def test_mark_task_complete(self):
        self.tasks = [{"title": "Incomplete Task", "completed": False}]
        # Simulate user input '1' to mark the first task as complete
        with mock.patch('builtins.input', return_value='1'):
            mark_task_complete(self.tasks)
        self.assertTrue(self.tasks[0]["completed"])

    def test_clear_all_tasks(self):
        self.tasks = [{"title": "Task 1", "completed": True}, {"title": "Task 2", "completed": False}]
        # Simulate user input 'y' to confirm clearing all tasks
        with mock.patch('builtins.input', return_value='y'):
            clear_all_tasks(self.tasks)
        self.assertEqual(len(self.tasks), 0)

    def test_view_tasks(self):
        # This test will just check if the function runs without errors
        # A more comprehensive test would require capturing stdout
        self.tasks = [{"title": "Task 1", "completed": True}, {"title": "Task 2", "completed": False}]
        view_tasks(self.tasks, "all")
        view_tasks(self.tasks, "completed")
        view_tasks(self.tasks, "pending")

if __name__ == "__main__":
    # Temporarily modify the TASKS_FILE constant in advanced_todo
    # to avoid overwriting the user's tasks.json during tests.
    import advanced_todo
    advanced_todo.TASKS_FILE = "test_tasks.json"
    unittest.main()