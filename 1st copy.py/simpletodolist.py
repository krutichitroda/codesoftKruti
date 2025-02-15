import json
tasks = []

# Function for add a task
def add_task(title, description="", priority="Low", deadline="None"):
    task = {
        "title": title,
        "description": description,
        "deadline": deadline,
        "completed": False,
    }
    tasks.append(task)
    print(f"Task '{title}' added successfully!")

# Function for view tasks
def view_tasks(show_all=True):
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, 1):
        if not show_all and task["completed"]:
            continue
        status = "okay" if task["completed"] else "first done you task first"
        print(f"{idx}. {task['title']} - {status}")
        print(f"   Description: {task.get('description', 'No description provided')}")
        print()

# Function for mark a task as complete
def mark_complete(task_number):
    try:
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as complete.")
    except IndexError:
        print("Invalid task number.")

# Function for delete a task
def delete_task(task_number):
    try:
        task = tasks.pop(task_number - 1)
        print(f"Task '{task['title']}' deleted successfully.")
    except IndexError:
        print("Invalid task number.")

# Function for save tasks to a file
def save_tasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved successfully.")

# Function for load tasks from a file
def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("No saved tasks found. Starting with an empty list.")

# Main Function
def main():
    load_tasks()  
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            deadline = input("Enter task deadline (optional): ")
            add_task(title, description, deadline)
        elif choice == "2":
            show_all = input("View all tasks? (y/n): ").lower() == "y"
            view_tasks(show_all)
        elif choice == "3":
            task_number = int(input("Enter task number to mark complete: "))
            mark_complete(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


