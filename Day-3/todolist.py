
FILE_NAME = "tasks.txt"

# Add a new task
def add_task(task):
    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")

    print("Task saved!")


# Show all tasks
def show_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

    except FileNotFoundError:
        print("No task file yet.")


# Delete a task
def delete_task():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to delete.")
            return

        # Show tasks first
        print("\nYour Tasks:")

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        # Ask which task to delete
        task_num = int(input("\nEnter task number to delete: "))

        # Check if number is valid
        if 1 <= task_num <= len(tasks):

            # Remove selected task
            tasks.pop(task_num - 1)

            # Rewrite file
            with open(FILE_NAME, "w") as file:
                file.writelines(tasks)

            print("Task deleted!")

        else:
            print("Invalid task number.")

    except FileNotFoundError:
        print("No task file found.")

    except ValueError:
        print("Please enter a valid number.")


# Main program loop
while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")