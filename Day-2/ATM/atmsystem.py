
# pin = "1234"
# balance = 1000

# input_pin = input("Enter your PIN: ")

# if input_pin == pin:
#     print("Login successful!\n")

#     while True:
#         print("\n--- ATM MENU ---")
#         print("1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")

#         choice = input("Choose option: ")

#         if choice == "1":
#             print(f"Your balance is RM{balance}")

#         elif choice == "2":
#             deposit = int(input("Enter amount to deposit: "))
#             balance += deposit
#             print(f"Deposited RM{deposit}")

#         elif choice == "3":
#             withdraw = int(input("Enter amount to withdraw: "))

#             if withdraw <= balance:
#                 balance -= withdraw
#                 print(f"Withdrawn RM{withdraw}")
#             else:
#                 print("Not enough balance ❌")

#         elif choice == "4":
#             print("Thank you for using ATM 👋")
#             break

#         else:
#             print("Invalid option ❌")

# else:
#     print("Wrong PIN ❌")


        ##################################
        # ATM System (Mini Project)      #
        #                                #
        # Features:                      #
        # Check balance                  #
        # Deposit money                  #
        # Withdraw money                 #
        # Exit system                    #
        # PIN login (basic security)     #
        ##################################

        ##################################
        # Try improving your ATM:        #
        #                                #
        # Level 1:                       #
        # Add 3 wrong PIN attempts limit #
        # Level 2:                       #
        # Add “transaction history”      #
        # Level 3:                       #
        # Add “transfer money” option    #
        #                                #
        # ATM v2 (with transaction       #
        # history + better structure)    #
        ##################################

pin = "1234"
balance = 1000

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    input_pin = input("Please enter your pin number: ")

    if input_pin == pin:
        print("Successfully login!")

        while True:
            print("##################################")
            print("##   1. Check balance           ##")
            print("##   2. Deposit money           ##")
            print("##   3. Withdraw money          ##")
            print("##   4. Exit system             ##")
            print("##################################")

            choice = int(input("Please choose the service required: "))

            if choice == 1:
                print(f"Account balance: {balance}")
            elif choice == 2:
                print(f"Deposit money")

                deposit_amount = int(input("Please enter deposit amount: "))
                balance = deposit_amount + balance

                print(f"Current balance: RM {balance}")
            elif choice == 3:
                print(f"Withdraw money")
                
                withdraw = int(input("Enter amount: "))
                confirm = input(f"Please confirm withdraw amount: RM{withdraw}, yes/no: ")
                
                if confirm.lower() == "yes":
                    if withdraw > balance:
                        print("Insufficient balance.")
                    else:
                        balance = balance - withdraw
                        print(f"Succesfully withdraw, account balance: RM{balance}")
                else:
                    print("Transaction failed!")
            elif choice == 4:
                print(f"Thank for choosing us.")
                break
            
            else:
                print("Invalid choice.")

            again = input("Do you want to continue? (yes/no): ")
            if again.lower() != "yes":
                print("Thank you for choosing us!")
                break

        break  # exit login 

    else:
        print("Wrong Password!")
        attempts += 1

if attempts == max_attempts:
    print("Please try again later.")