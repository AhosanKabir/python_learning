print("hello world")

"""
	Data type of python 
	1) Integers 
	2) String
	3) Boolean 
	4) Float 
	5) None
"""

# for AND , OR Logic -------------------------------------->
val1 = True
val2 =  False
val3 = True

print(f"AND operator: {val1 and val2}")
print(f"AND operator: {val1 and val3}")

print(f"OR operator: {val1 or val2}")
print(f"OR operator: {val1 or val3}")


# for input values --------------------------------------->

# result for input always a string 
# name = input("write your name :")
# print(f"welcome {name} , Have a nice day!")
# print(type(name))

# age = int(input("write your Age :"))
# print(f"ypur age is now {age}!")
# print(type(age))

# number1 = float(input("write first number: "))
# number2 = float(input("write second number: "))

# sum = number1 + number2
# print(sum)


# for random number -------------------------------------->
import random
print(random.randrange(1, 10))