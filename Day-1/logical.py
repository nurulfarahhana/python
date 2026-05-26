
#################################################
# and   → both conditions must be True          #
# or    → at least one condition must be True   #
# not   → reverses True/False                   #
#################################################

# Mini practice

# Question 1
age = int(input("Please enter your age: "))
has_ticket = True

if (age >= 18) and has_ticket:
    print("Allowed!")
else:
    print("Not Allowed")


# Question 2
member = True
has_ticket = True

if member or has_ticket:
    print("Give discount")
else:
    print("No discount")


# Question 3
is_raining = True

if not is_raining:
    print("Go outside")
else:
    print("Stay inside")