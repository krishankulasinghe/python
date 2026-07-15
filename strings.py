# text  = 'I'm learning Python programming!' -   we cant use single quotes inside single quotes, so we can use double quotes to define the string instead.
text = "I'm learning Python programming!"
print(text)

# text2 = "I"m learning Python programming!"  - this will give an error because we are using double quotes to define the string, but we are also using double quotes inside the string. To fix this, we can use single quotes to define the string instead.
text2 = 'I"m learning Python programming!'
print(text2)

#input function is used to take input from the user. It takes a string as an argument, which is displayed as a prompt to the user. The function returns the input as a string.
name = input("Enter your name: ")
print("Hello, " + name + "!") # Output: Hello, [name]!

age = int(input("Enter your age: ")) # input function returns a string, so we need to convert it to an integer using int() function.
print("You are " + str(age) + " years old.") # Output: You are [age] years old. (we need to convert the integer age back to string using str() function to concatenate it with other strings.)

text = "Hello" "World"
print(text) # Output: HelloWorld

# Print Without a New Line
# the end parameter of the print function is used to specify what should be printed at the end of the output. 
#  By default, it is a newline character, but we can change it to a space or any other string.
print("Hello World!", end=" ")
print("I will print on the same line.") # Output: Hello World! I will print on the same line. 

text1 = "Hello World!"
print(text1.upper()) # Output: HELLO WORLD!
print(text1.lower()) # Output: hello world!
print(text1.title()) # Output: Hello World!
print(text1.capitalize()) # Output: Hello world!
print(text1.swapcase()) # Output: hELLO wORLD!
print(text1.replace("World", "Python")) # Output: Hello Python!
print(text1.strip()) # Output: Hello World! (removes leading and trailing whitespace)
print(text1.split()) # Output: ['Hello', 'World!'] (splits the string into a list of words)
print(text1.split("o")) # Output: ['Hell', ' W', 'rld!'] (splits the string into a list of substrings using "o" as the delimiter)
print(text1.find("World")) # Output: 6 (returns the index of the first occurrence of "World")
print(text1.find("Python")) # Output: -1 (returns -1 if the substring is not found)
print(text1.join(["Hi", "Python"])) # Output: HiHello World!Python (joins the list of strings into a single string using "Hello World!" as the separator. in this case, it will join "Hi" and "Python" with "Hello World!" in between them.)
print(text1.join(["Hi", "Python", "Programming"])) # Output: HiHello World!PythonHello World!Programming (joins the list of strings into a single string using "Hello World!" as the separator. in this case, it will join "Hi", "Python" and "Programming" with "Hello World!" in between them.)

print(text1.replace("World", "Python").upper()) # Output: HELLO PYTHON! (replaces "World" with "Python" and converts the string to uppercase)
print(text1.startswith("Hello")) # Output: True (checks if the string starts with "Hello")
print(text1.endswith("!")) # Output: True (checks if the string ends with "!")
print(text1.find("World")) # Output: 6 (returns the index of the first occurrence of "World")
print(text1.count("o")) # Output: 2 (counts the number of occurrences of "o")
print(text1.isalpha()) # Output: False (checks if all characters in the string are alphabetic)
print(text1.isdigit()) # Output: False (checks if all characters in the string are digits)
print(text1.isalnum()) # Output: False (checks if all characters in the string are alphanumeric)
print(text1.isspace()) # Output: False (checks if all characters in the string are whitespace)
print(text1.islower()) # Output: False (checks if all characters in the string are lowercase)
print(text1.isupper()) # Output: False (checks if all characters in the string are uppercase)
print(text1.isprintable()) # Output: True (checks if all characters in the string are printable)
print(len(text1)) # Output: 12 (returns the length of the string )

text3 ="{0} am learning {1} programming!".format("I", "Python")
print(text3) # Output: I am learning Python programming! (replaces the placeholders {0} and {1} with "I" and "Python" respectively)

text3 ="{A} am learning {B} programming!".format(A="I", B="Python")
print(text3) # Output: I am learning Python programming! (replaces the placeholders {A} and {B} with "I" and "Python" respectively)

print(text1.center(20, "*")) # Output: ****Hello World!**** (centers the string in a field of width 20, padding with "*")
print(text1.zfill(20)) # Output: 0000000000Hello World! (pads the string with zeros on the left to make it 20 characters long)