import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "[Done]" if task["done"] else "[Pending]"
            print(f"{idx}. {status} {task['task']}")

def mark_done(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    else:
        print("Invalid task number!")

def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' deleted!")
    else:
        print("Invalid task number!")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks)
            try:
                task_index = int(input("Enter task number to mark as done: ")) - 1
                mark_done(tasks, task_index)
            except ValueError:
                print("Invalid input!")
        elif choice == "4":
            list_tasks(tasks)
            try:
                task_index = int(input("Enter task number to delete: ")) - 1
                delete_task(tasks, task_index)
            except ValueError:
                print("Invalid input!")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
