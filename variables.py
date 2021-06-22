# Test installation

# the print function is used to display output provided in the string
# print("Hello Filipe")

# Variables
# Python variables
# Variables work as a placeholder to store data
# string anything between '' or ""
# integers/numbers
# Syntax to create a variable: name of variable = value of variable
# Follow good logical naming convention

# first_name = "Filipe"
# last_name = "Silva"
#
# salary = 10.5  # float
# age = 22  # int
# my_age = "22"

# print(first_name)
# print(last_name)
# print(salary)
# print("Age =", age)
# print(my_age)
#
# # type() helps us find the type of variable
# print(type(age))
# print(type(my_age))

# input() to interact with user
# user_name = input("Please enter your name:   ")
# print("Hello", user_name)

# Activity

# Create variables: first_name, last_name, age, DoB and prompt user to input above values
first_name = input("Please enter your first name:   ")
last_name = input("Please enter your last name:   ")
age = input("Please enter your age:   ")
dob = input("Please enter your date of birth:   ")

# Print/display the type of each value received from the user
print(type(first_name))
print(type(last_name))
print(type(age))
print(type(dob))

# Display the data back to user with greeting message
print("Hello! Here are your details:")
print(first_name, last_name, age, dob)
