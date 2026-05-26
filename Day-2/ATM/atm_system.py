
import os

file_name = "account.txt"

# Load data
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        data = file.read().split(",")
        pin = data[0]
        balance = int(data[1])
else:
    pin = "1234"
    balance = 1000

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    input_pin = input("Enter PIN: ")

    if input_pin == pin:
        print("Login successful!")

        while True:
            print("\n====== ATM MENU ======")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Exit")

            try:
                choice = int(input("Choose option: "))
            except:
                print("Invalid input!")
                continue

            if choice == 1:
                print(f"Balance: {balance}")

            elif choice == 2:
                try:
                    amount = int(input("Enter deposit amount: "))
                    if amount > 0:
                        balance += amount
                        print(f"New balance: {balance}")
                    else:
                        print("Invalid amount!")
                except:
                    print("Invalid input!")

            elif choice == 3:
                try:
                    amount = int(input("Enter withdraw amount: "))
                    if amount > balance:
                        print("Insufficient balance!")
                    elif amount <= 0:
                        print("Invalid amount!")
                    else:
                        confirm = input("Confirm? (yes/no): ")
                        if confirm.lower() == "yes":
                            balance -= amount
                            print(f"Remaining balance: {balance}")
                        else:
                            print("Cancelled.")
                except:
                    print("Invalid input!")

            elif choice == 4:
                old_pin = input("Enter current PIN: ")
                if old_pin == pin:
                    new_pin = input("Enter new PIN: ")
                    if len(new_pin) == 4 and new_pin.isdigit():
                        pin = new_pin
                        print("PIN changed successfully!")
                    else:
                        print("PIN must be 4 digits!")
                else:
                    print("Wrong PIN!")

            elif choice == 5:
                with open(file_name, "w") as file:
                    file.write(f"{pin},{balance}")
                print("Thank you! Data saved.")
                break

            else:
                print("Invalid choice!")

        break

    else:
        print("Wrong PIN!")
        attempts += 1

if attempts == max_attempts:
    print("Too many attempts. Try later.")