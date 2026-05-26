
# Mini Project

# Project 1 = Login system

username = "siti"
password = "123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    input_username = input("Username: ").lower
    input_password = input("Password: ")

    if input_username == username:
        if input_password == password:
            # print("Successfully login!")

            # Show message: “Welcome back, Farah!”
            print(f"Welcome back, {input_username.capitalize()}!")
            break
        else:
            print("Wrong password")
            
            attempts += 1
            print(f"Attempts left: {max_attempts - attempts}")
    else:
        print("User not found")
        attempts += 1
        print(f"Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Acoount Lock!")
