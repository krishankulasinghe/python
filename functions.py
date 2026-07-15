# function has two parts: Function definition and function body. The function definition includes the function name, parameters, and the return type. 
# The function body contains the code that performs the task of the function.

# Function definition and Function body
def greet(name):
    return f"Hello, {name}!"

# function call
print(greet("Alice"))  # Output: Hello, Alice!

# Function definition with multiple parameters
def add_numbers(a, b):
    return a + b

# function call
print(add_numbers(3, 5))  # Output: 8

#-----------------------------------------------------------------------------------------------------------------------#
# Local and Global Variables
# Global variable : Variable that is defined outside of any function and can be accessed from anywhere in the code.
global_variable = "I am a global variable"
global_variable1 = "I am a global variable1"

# Function definition with local variable
def local_variable_example():
	local_variable = "I am a local variable"
	global_variable1 = "I am a modified global variable1"
	print(local_variable)  # Output: I am a local variable

print(global_variable)  # Output: I am a global variable
# print(local_variable)  # this will raise an error because local_variable is not defined in the global scope
print(global_variable1)  # Output: I am a global variable1. why? Because the local variable with the same name inside the function does not affect the global variable. The global variable remains unchanged outside the function.
# if you want to modify the global variable inside the function, you need to use the global keyword.
# eg: 
def modify_global_variable1():
	global global_variable1
	global_variable1 = "I have been modified"
	print(global_variable1)  # Output: I have been modified



# global Keyword: Used to declare a variable as global inside a function, allowing it to be modified.
def modify_global_variable():
	global global_keyword
	global_keyword = "I have been modified"
	print(global_keyword)  # Output: I have been modified

modify_global_variable()  # must call the function first to define global_keyword
print(global_keyword) # Output: I have been modified



# Function Arbitrary Arguments: 

# 1. Arbitrary Positional Arguments: Allows a function to accept any number of positional arguments using *args.
def arbitrary_positional_arguments(*args):
	print("Positional arguments:", args)

# function call
arbitrary_positional_arguments(1, 2, 3) # Output: Positional arguments: (1, 2, 3)
arbitrary_positional_arguments(1) # Output: Positional arguments: (1,)
# Note: *args always packs values into a tuple, shown with (). (*args means "collect any extra values I'm given and pack them into a tuple.")
# Single value -> (1,) the comma marks it as a tuple (without it, (1) is just the number 1).
# Multiple values -> (1, 2, 3) commas between items already show it's a tuple, so no trailing comma needed.

# 2. Arbitrary Keyword Arguments: Allows a function to accept any number of keyword arguments using **kwargs.
def arbitrary_keyword_arguments(**kwargs):
	print("Keyword arguments:", kwargs)
	print(kwargs["name"]) # Output: Alice. Accessing the value of the keyword argument "name" from the kwargs dictionary.

# function call
arbitrary_keyword_arguments(name="Alice", age=30) # Output: Keyword arguments: {'name': 'Alice', 'age': 30}
arbitrary_keyword_arguments(city="New York") # Output: Keyword arguments: {'city': 'New York'}

# Note: **kwargs always packs values into a dictionary, shown with {}. (**kwargs means "collect any extra keyword arguments I'm given and pack them into a dictionary.")

def method(c1, c2, c3):
	print(c1)
	print(c2)
	print(c3)


method(c1="value1",  c3="value3", c2="value2") # Output: value1 value2 value3. The order of the keyword arguments does not matter, as they are matched by name.


# Lambda Functions: Anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have one expression.
#  Lambda functions are good for short, simple functions that are used temporarily and do not require a name.
# Syntax: lambda arguments: expression 
# Example:
num = lambda x: x * 2
print(num(5)) # Output: 10

add = lambda x, y: x + y
print(add(2, 3)) # Output: 5

# Lamda Functions can also be used with higher-order functions like map(), filter(), and reduce().
# Example: 
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared) # Output: [1, 4, 9, 16, 25]

# Lambda Funtions with if-else statement: Lambda functions can also include conditional expressions using the if-else statement.
# Example:
max_num = lambda x, y: x if x > y else y
print(max_num(5, 10)) # Output: 10
