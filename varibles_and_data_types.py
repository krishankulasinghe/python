str = "Hello, World!"
print(str) # This code snippet defines a string variable `str` with the value "Hello, World!" and then prints it to the console. When executed, it will output: Hello, World!

str1, str2  = "Python is fun!", "Let's learn Python together."
print(str1) # This will print: Python is fun!
print(str2) # This will print: Let's learn Python together.

print(str1 + " " + str2) # This will concatenate str1 and str2 with a space in between and print: Python is fun! Let's learn Python together.
print(str1 , str2) # This will print str1 and str2 separated by a space: Python is fun! Let's learn Python together.
print(str1 * 2) # This will print str1 twice: Python is fun!Python is fun!

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Python has 3 numeric types: int, float, and complex. Here are some examples:
int_num = 10
float_num = 10.5
complex_num = 2 + 3j

# You can perform arithmetic operations with these numeric types:
sum_int_float = int_num + float_num # This will add an integer and a float,	 resulting in a float: 20.5
print(sum_int_float) # This will print: 20.5

# You can also perform arithmetic operations with complex numbers:
sum_complex = complex_num + (1 + 2j) # This will add two complex numbers, resulting in a new complex number: (3+5j)
print(sum_complex) # This will print: (3+5j)

# to check the type of a variable, you can use the `type()` function:
print(type(int_num)) # This will print: <class 'int'>
print(type(float_num)) # This will print: <class 'float'>
print(type(complex_num)) # This will print: <class 'complex'>

# Text sequences in Python are represented by the `str` type. Strings can be defined using single quotes, double quotes, or triple quotes for multi-line strings. Here are some examples:
single_quote_str = 'This is a string in single quotes.'
double_quote_str = "This is a string in double quotes."
multi_line_str = '''This is a multi-line string.
It can span multiple lines.'''

# python also has a `bool` type, which can have one of two values: `True` or `False`. Here are some examples:
bool_true = True
bool_false = False

#python also has a `None` type, which represents the absence of a value or a null value. Here is an example:
none_value = None

# python has sequence types, which include lists, tuples, and ranges. Here are some examples:
# A list is an ordered collection of items that can be changed (mutable). Lists are defined using square brackets []:
my_list = [1, 2, 3, 4, 5]

# A tuple is an ordered collection of items that cannot be changed (immutable). Tuples are defined using parentheses ():
my_tuple = (1, 2, 3, 4, 5)

# why list is mutable and tuple is immutable?
# Lists are mutable because they allow you to modify their contents after they have been created. You can add, remove, or change elements in a list. For example:
my_list[0] = 10 # This will change the first element of the list to 10. Now, my_list will be [10, 2, 3, 4, 5].

#but Tuples are immutable because once they are created, their contents cannot be changed. You cannot add, remove, or change elements in a tuple. For example:
# my_tuple[0] = 10 # This will raise a TypeError because tuples do not support item assignment.


# A range represents a sequence of numbers and is commonly used in for loops:
my_range = range(1, 6)
print(list(my_range)) # This will print: [1, 2, 3, 4, 5]

range1 = range(0, 10, 2) # This will create a range of numbers from 0 to 9 with a step of 2.
print(list(range1)) # This will print: [0, 2, 4, 6, 8]

range2 = range(10, 0, -1) # This will create a range of numbers from 10 to 1 in reverse order.
print(list(range2)) # This will print: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

range3 = range(5) # This will create a range of numbers from 0 to 4.
print(list(range3)) # This will print: [0, 1, 2, 3, 4]


# Mapping types in Python include dictionaries, which are unordered collections of key-value pairs. Dictionaries are defined using curly braces {}:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict) # This will print: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# You can access values in a dictionary using their keys:
print(my_dict["name"]) # This will print: Alice

# You can also add, remove, or change key-value pairs in a dictionary:
my_dict["age"] = 31 # This will change the value associated with the key "age" to 31.
my_dict["country"] = "USA" # This will add a new key-value pair to the dictionary.
print(my_dict) # This will print: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}

# You can remove a key-value pair from a dictionary using the `del` statement:
del my_dict["city"] # This will remove the key-value pair with the key "city" from the dictionary.
print(my_dict) # This will print: {'name': 'Alice', 'age': 31, 'country': 'USA'}

# Python also has a `set` type, which is an unordered collection of unique items. Sets are defined using curly braces {} or the `set()` constructor:
my_set = {1, 7, 3, 6, 5}
print(my_set) # Sets are unordered, so the order is NOT guaranteed. This just happens to print {1, 3, 5, 6, 7}
# because CPython's hash table places small non-negative integers into slots matching their own value,
# which makes them look "sorted" by coincidence. Try it with negative numbers or strings and the order
# looks arbitrary, e.g. print({50, -3, 10, 100}) or print({'banana', 'apple', 'cherry'}).
# Never rely on set order in real code - use sorted(my_set) or a list if you need a specific order.

#Casting can be two types: implicit and explicit. Implicit casting is done automatically by Python when you perform operations between different numeric types. For example:
int_num = 10
float_num = 10.5
result = int_num + float_num # This will implicitly cast the integer to a float and perform the addition, resulting in a float: 20.5
print(result) # This will print: 20.5

complex_num = complex(2, 3) # This will create a complex number with a real part of 2 and an imaginary part of 3.
result_complex = int_num + complex_num # This will implicitly cast the integer to a complex number and perform the addition, resulting in a complex number: (12+3j)
print(result_complex) # This will print: (12+3j)

complex_num2 = complex(int_num, float_num) # This will create a complex number with a real part of 10 and an imaginary part of 10.5.
print(complex_num2) # This will print: (10+10.5j)

complex_num3 = complex(int_num) # This will create a complex number with a real part of 10 and an imaginary part of 0.
print(complex_num3) # This will print: (10+0j)

# Explicit casting is done manually by the programmer using built-in functions like `int()`, `float()`, and `str()`. For example:
float_num = 10.5
int_num = int(float_num) # This will explicitly cast the float to an integer, resulting in 10.
print(int_num) # This will print: 10


# Python also has a `bytes` type, which represents a sequence of bytes. Bytes are immutable and can be defined using the `b` prefix before a string literal:
my_bytes = b"Hello, Bytes!"
print(my_bytes) # This will print: b'Hello, Bytes!'




