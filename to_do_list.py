import json

# Function to load existing tasks from a JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to display the current to-do list
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to add a new task
def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Added: {new_task}")
    save_tasks(tasks)

# Function to update a task
def update_task(tasks, task_index, updated_task):
    if task_index >= 1 and task_index <= len(tasks):
        tasks[task_index - 1] = updated_task
        print(f"Updated: {updated_task}")
        save_tasks(tasks)
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(tasks, task_index):
    if task_index >= 1 and task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Deleted: {deleted_task}")
        save_tasks(tasks)
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nOptions:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the task to add: ")
            add_task(tasks, new_task)
        elif choice == "3":
            show_tasks(tasks)
            task_index = int(input("Enter the task number to update: "))
            updated_task = input("Enter the updated task: ")
            update_task(tasks, task_index, updated_task)
        elif choice == "4":
            show_tasks(tasks)
            task_index = int(input("Enter the task number to delete: "))
            delete_task(tasks, task_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()