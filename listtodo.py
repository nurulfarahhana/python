        ############################
        ##      1. Add Task       ##
        ##      2. Show Tasks     ##
        ##      3. Delete Task    ##
        ##      4. Exit           ##
        ############################

tasks = ["task a","task b","task c"]

while True:
    print("\n############################")
    print("##      1. Add Task       ##")
    print("##      2. Show Tasks     ##")
    print("##      3. Delete Task    ##")
    print("##      4. Exit           ##")
    print("############################")

    choice = int(input("Please choose what to do: "))

    if choice == 1:
        print("Addding task")
        new_task = input("Please enter new task: ")
        tasks.append(new_task)

        print("Successfully added!")

    elif choice == 2:
        print("\nYour task")

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == 3:
        print("Delete task")
        
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        delete_choice = int(input("Please enter which task to delete: "))

        confirm = input(f"Please confirm task to delete (yes/no): {delete_choice}")

        if confirm.lower() == "yes":
            if len(tasks) >= delete_choice >= 1:
                remove_task = tasks.pop(delete_choice - 1)
                # print(f"Succeessfully  remove {delete_choice}")
                print(f"Successfully removed {delete_choice}")
            else:
                print("Invalid choice")
        else:
            print("Cancel delete")

    elif choice == 4:
        print("Have a nice day!")
        break
    else:
        print("Invalid choice")