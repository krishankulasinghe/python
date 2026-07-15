#exception handling in Python allows you to handle errors gracefully without crashing the program. The basic structure of exception handling involves using the try and except blocks.
## The try block contains code that may raise an exception, and the except block contains code that handles the exception if it occurs.

#example 1:
try:
    # code that may raise an exception
    print(x) 
except:
    print("An error occurred")

# Example 2:
try:
    # code that may raise an exception
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero") 

#example 3:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong") 



#else block: The else block is optional and can be used to specify code that should run if no exceptions are raised in the try block. if an exception occurs, the else block will be skipped.
#example:
try:
	x = 10 / 2
except ZeroDivisionError:
	print("Cannot divide by zero")
else:
	print("Division successful, result is:", x)  # Output: Division successful, result is: 5.0
      
# finally block: The finally block is also optional and can be used to specify code that should run regardless of whether an exception occurred or not. 
# It is often used for cleanup actions, such as closing files or releasing resources.
#example:
try:
	x = 10 / 0
except ZeroDivisionError:
	print("Cannot divide by zero")
finally:
	print("This will always be executed") 

#output: 
# Cannot divide by zero 
# This will always be executed

# raising exceptions: You can raise exceptions manually using the raise statement. 
# This is useful when you want to enforce certain conditions in your code and signal an error if those conditions are not met.
#example:
x = -1
if x < 0:
    raise Exception("x must be non-negative")


# Execption Hierarchy: Python has a built-in hierarchy of exceptions, with the base class being Exception.
# Some common built-in exceptions include:
# exception types:
# SystemExit: Raised by the sys.exit() function.
# KeyboardInterrupt: Raised when the user interrupts program execution, usually by pressing Ctrl+C.
# ValueError: Raised when a function receives an argument of the right type but an inappropriate value.
# TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# IndexError: Raised when a sequence subscript is out of range.
# KeyError: Raised when a dictionary key is not found.
# AttributeError: Raised when an attribute reference or assignment fails.
