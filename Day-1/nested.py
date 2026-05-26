

    #################################################
    # if condition1:                                #
    #     if condition2:                            #
    #         print("Both conditions are true")     #
    #################################################


    # EXAMPLE
    #################################################
    # username = "admin"                            #
    # password = "1234"                             #
    #                                               #
    # input_user = input("Username: ")              #
    # input_pass = input("Password: ")              #
    #                                               #
    # if input_user == username:                    #
    #     if input_pass == password:                #
    #         print("Login successful")             #
    #     else:                                     #
    #         print("Wrong password")               #
    # else:                                         #
    #     print("User not found")                   #
    #################################################

# Question 1 (Age + ID check)
age = int(input("Please enter your age: "))
has_id = True

if age >= 18:
    if has_id:
        print("Allowed!")
    else:
        print("Need ID!")
else:
    print("Too young!")

# Question 2 (Exam system)
marks = int(input("Please enter your Bahasa Melayu marks: "))

if marks >= 50:
    if marks >= 80:
        print("Excellent!")
    else:
        print("Good")
else:
    print("Succesfully failed!")


# Question 3 (Login system (simple))

username = "farahhana"
password = "farah123"

input_username = input("Please enter your username: ")
input_password = input("Enter you password: ")

if input_username == username:
    if input_password == password:
        print("Successfully login!")
    else:
        print("Wrong password")
else:
    print("User not found")
