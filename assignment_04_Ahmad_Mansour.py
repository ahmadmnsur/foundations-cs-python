class Task:
    task_id_counter = 0

    def __init__(self, description, priority):
        Task.task_id_counter += 1
        self.__task_id = Task.task_id_counter
        self.__description = description
        self.__priority = priority
        self.__completed = False

    def get_task_id(self):
        return self.__task_id

    def get_description(self):
        return self.__description

    def get_priority(self):
        return self.__priority

    def get_completed(self):
        return self.__completed

    def set_completed(self, value):
            self.__completed = value
            
    def mark_completed(self):
        self.__completed = True


class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.tasks.sort(x=lambda y: y.get_priority(), reverse=True)

    def get_highest_priority_task(self):
        if self.tasks:
            return self.tasks[0]
        return None

    def mark_highest_priority_completed(self):
        if self.tasks:
            task = self.tasks.pop(0)
            task.mark_completed()
            return task
        return None


class Stack:
    def __init__(self):
        self.tasks = []

    def push(self, task):
        self.tasks.append(task)

    def pop(self):
        if self.tasks:
            return self.tasks.pop()
        return None


class TaskManager:
    def __init__(self):
        self.task_queue = PriorityQueue()
        self.task_history = Stack()

    def add_task(self, description, priority):
        new_task = Task(description, priority)
        self.task_queue.add_task(new_task)

    def get_task_by_id(self, task_id):
        for task in self.task_queue.tasks:
            if task.get_task_id() == task_id:
                return task
        return None

    def display_all_tasks(self):
        for task in self.task_queue.tasks:
            print(f"Task {task.get_task_id()}: {task.get_description()} (Priority: {task.get_priority()}, Completed: {task.get_completed()})")

    def display_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.task_queue.tasks if not task.get_completed()]
        for task in incomplete_tasks:
            print(f"Task {task.get_task_id()}: {task.get_description()} (Priority: {task.get_priority()})")

    def display_last_completed_task(self):
        last_completed_task = self.task_history.pop()
        if last_completed_task:
            print(f"Last Completed Task: {last_completed_task.get_description()}")
        else:
            print("No completed tasks in history.")

task_manager = TaskManager()

while True:
    print("\nTask Manager Menu:")
    print("1. Add a new task")
    print("2. Get a task by ID")
    print("3. Mark highest priority task as completed")
    print("4. Display all tasks in order of priority")
    print("5. Display only incomplete tasks")
    print("6. Display last completed task")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        description = input("Enter task description: ")
        priority = int(input("Enter task priority: "))
        task_manager.add_task(description, priority)

    elif choice == "2":
        task_id = int(input("Enter task ID: "))
        task = task_manager.get_task_by_id(task_id)
        if task:
            print(f"Task {task_id}: {task.get_description()} (Priority: {task.get_priority()}, Completed: {task.get_completed()})")
        else:
            print("Task not found.")

    elif choice == "3":
        completed_task = task_manager.task_queue.mark_highest_priority_completed()
        if completed_task:
            task_manager.task_history.push(completed_task)
            print(f"Marked task {completed_task.get_task_id()} as completed.")
        else:
            print("No tasks to mark as completed.")

    elif choice == "4":
        task_manager.display_all_tasks()

    elif choice == "5":
        task_manager.display_incomplete_tasks()

    elif choice == "6":
        task_manager.display_last_completed_task()

    elif choice == "7":
        print("Exiting Task Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
