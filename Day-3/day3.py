
# Day-3


# 1. Function (def)
def greet():
    name = input("Please enter your name: ")
    print(f"Hallo, morning {name}!")

    print("Morning", name)
greet()
greet("Alex")
greet("Lokman")

def adding(a, b):
    return a / b

result = adding(5,8)
print(result)




# 2. List
# Lists store many values in one variable.

fruits = ["tembikai","pisang","durian","rambutan"]
# print(fruits[2])

fruits.append("anggur")

for fruit in fruits:
    print(fruit)

numbers = [1, 2, 3]

print(len(numbers))     # length
print(sum(numbers))     # total
print(max(numbers))     # biggest

shoppinglist = ["bawang","susu","kicap"]
print(shoppinglist[1])

# Add 3 items and print them using a loop.
shoppinglist.append("garam")

for shoppinglists in shoppinglist:
    print(shoppinglists)




# 3. Dictionaries
# Dictionaries store data using key : value pairs

# student = {
#     "name": "Alex",
#     "age": 20,
#     "course": "Python"
# }

# student["school"] = "SMKKJ"
# student["city"] = "KL"

# print(student["city"])

# for key, value in student.items():
#     print(key, value)




# 4. File Handling
# This makes programs feel “real.”

file = open("notes.txt", "w")
# file.write("Hello world!")
# file.close()

file.write("Python is fun!")
file.write("\nNew line added") 

with open("notes.txt", "r") as file:   
    content = file.read()

print(content)