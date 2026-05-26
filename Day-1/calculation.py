
# Calculation

#################################################
#   +   addition                                #
#    -   subtraction                            #
#   *   multiplication                          #
#   /   division                                #
#   //  floor division (whole number result)    #
#   %   remainder (modulus)                     #
#   **  exponent (power)                        #
#################################################

#################################################
#   ==  equal                                   #
#   !=  not equal                               #
#   >   greater than                            #
#   <   less than                               #
#   >=  greater or equal                        #
#   <=  less or equal                           #
#################################################

# Question 1
num_1 = int(input("Please enter your number: "))

if (num_1%2) == 1:
    print("odd")
else:
    print("even")

# Question 2
marks = int(input("Please insert your math mark: "))

if marks >= 50:
    print("Pass!")
else:
    print("Fail")

# Question 3
int_1 = int(input("Please enter first number: "))
int_2 = int(input("Please enter second number: "))

print(f"Total number of both number is {int_1+int_2}")
print(f"The difference between both number is {int_1-int_2}")
print(f"The product of both number is {int_1*int_2}")