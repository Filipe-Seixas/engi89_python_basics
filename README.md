# Variables Activity

### Create variables: first_name, last_name, age, DoB and prompt user to input above values
```python 
first_name = input("Please enter your first name:   ")
last_name = input("Please enter your last name:   ")
age = input("Please enter your age:   ")
dob = input("Please enter your date of birth:   ")
```

### Print/display the type of each value received from the user
```python 
print(type(first_name))
print(type(last_name))
print(type(age))
print(type(dob))
```

### Display the data back to user with greeting message
```python 
print("Hello! Here are your details:")
print(first_name, last_name, age, dob)
```

# Data types and operators

```python
# What are data types and operators
# Boolean, numbers, strings
# Operators: Arithmetic (- + / * %)

number_1 = 4
number_2 = 2

# print(number_1 + number_2)  # add
# print(number_1 - number_2)  # minus
# print(number_1 * number_2)  # multiply
# print(number_1 / number_2)  # divide
# print(number_1 % number_2)  # remainder
# print(number_1 ** number_2)  # exponential

print(number_1 == number_2)  # is equal
print(number_1 != number_2)  # is not equal
print(number_1 >= number_2)  # greater or equal
print(number_1 <= number_2)  # less or equal
```

# String Casting and Concatenation

```python
# Using and Managing Strings
# string casting
# string concatenation
# casting methods

# single and double quotes
single_quote = 'These\'s are single quotes and working perfectly fine!'
double_quote = "These are double quotes, also working fine"

# print(single_quote)
# print(double_quote)

# Concatenation
first_name = "James"
last_name = "Bond"

# Create an int called age and display age in the same line as James Bond
age = 20

print(first_name + " " + last_name + " " + f"{age}")
print(first_name + " " + last_name, age)
print(first_name + " " + last_name + " " + str(age))

# String slicing and Indexing
greeting = "Hello World!"

# len() method is used to confirm the length of a string
print(len(greeting))

# In python indexing starts with 0
print(greeting[6:])  # slicing the string from index 0 to 4
print(greeting[-6:])  # slicing string right to left

# String built in methods

white_spaces = "Lot's of white spaces                       "
print(str(len(white_spaces)) + " including white spaces")

# strip method removes all white spaces before and after the sentence
print(str(len(white_spaces.strip())) + " excluding white spaces")

# more built in methods that can be used with stings

example_text = "here's some text with some text"

print(example_text.count("text"))  # count() method counts the number of times a word appears in string
print(example_text.lower())  # transforms text to lower case
print(example_text.upper())  # transforms text to upper case
print(example_text.capitalize())  # transforms first letter to upper
print(example_text.replace("with", ","))  # specified value is replaced with a specified value

```