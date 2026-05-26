
            ##############################################     
            ##           START                          ##
            ##             ↓                            ##
            ## Computer picks number (1–10)             ##
            ##             ↓                            ##
            ##         User guesses                     ##
            ##             ↓                            ##
            ##     Is guess correct?                    ##
            ##     ├── YES → WIN → END                  ##
            ##     └── NO                               ##
            ##             ↓                            ##
            ##     Too high or too low                  ##
            ##             ↓                            ##
            ##         Try again                        ##
            ##             ↓                            ##
            ## (loop until correct / attempts finish)   ##
            ##############################################

import random

while True:
    secret = random.randint(1,10)

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:

            guess = int(input("Enter number: "))

            if secret == guess:
                print(f"Perfect! The number was {secret}")
                break

            elif guess > secret:
                print("Smaller")

            else:
                print("Higher")

            attempts += 1
            print(f"Attempts left: {max_attempts - attempts}") 

    if attempts == max_attempts:
        print("Try again.")

    again = input("Do you want to play again? (yes/no): ")
    if again.lower() == "yes":
        continue   # 🔁 restart game
    else:
        print("Thank you for playing!")
        break      # 🛑 exit game