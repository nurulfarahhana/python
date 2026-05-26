
######################
##  1. Add Note     ##
##  2. View Notes   ##
##  3. Delete Note  ##
##  4. Exit         ##
######################

# for i, task in enumerate(tasks, start=1):
#             print(f"{i}. {task}")

FILE_NAME = "notes.txt"

notes = ["note 1","note b","note c"]

while True:

    print("\n######################")
    print("##  1. Add Note     ##")
    print("##  2. View Notes   ##")
    print("##  3. Delete Note  ##")
    print("##  4. Exit         ##")
    print("######################")

    try:
        choice = int(input("What to do: "))
    except ValueError:
        print("Please enter a number.")
        continue
    
    # ADDNOTE
    if choice == 1:
        print("Add note")
        new_notes = input("Please insert new notes: ")
        # notes.append(new_notes)

        with open(FILE_NAME, "a") as file:
            file.write(new_notes + "\n")

        print("Successfully added!")

    # VIEW NOTES
    elif choice == 2:

        print("\nView Notes")

        try:
            with open(FILE_NAME, "r") as file:
                notes = file.readlines()

            if not notes:
                print("No notes found.")

            else:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")

        except FileNotFoundError:
            print("No notes file found.")  

    # DELETE NOTE
    elif choice == 3:

        print("\nDelete Note")

        try:
            with open(FILE_NAME, "r") as file:
                notes = file.readlines()

            if not notes:
                print("No notes to delete.")
                continue

            # Show notes first
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")

            delete_note = int(input("\nWhich note to delete?: "))

            # Validate number
            if 1 <= delete_note <= len(notes):

                confirm = input("Confirm delete? (yes/no): ")

                if confirm.lower() == "yes":

                    removed_note = notes.pop(delete_note - 1)

                    # Rewrite updated notes
                    with open(FILE_NAME, "w") as file:
                        file.writelines(notes)

                    print(f"{removed_note.strip()} has been removed.")

                else:
                    print("Delete canceled.")

            else:
                print("Invalid note number.")

        except FileNotFoundError:
            print("No notes file found.")

        except ValueError:
            print("Please enter a valid number.")

    # EXIT
    elif choice == 4:
        print("Thank you.")
        break
    
    # INVALIDOPTION
    else:
        print("Invalid choice.")

