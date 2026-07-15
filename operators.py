num =5
num2 = 10
num3 = 15

result = num + num2
print(result) # Output: 15

result2 = num * num2
print(result2) # Output: 50

result3 = num2 / num
print(result3) # Output: 2.0

result4 = num2 // num # Floor division - devides and returns the largest integer less than or equal to the result
print(result4) # Output: 2 

result5 = num3 // num2 # Floor division - devides and returns the largest integer less than or equal to the result
print(result5) # Output: 1

result6 = num3 % num2 # Modulus - returns the remainder of the division
print(result6) # Output: 5

result7 = num2 ** num # Exponentiation - raises num3 to the power of num
print(result7) # Output: 100000

result8 = num2 + num3 * num # Order of operations - multiplication is performed before addition
print(result8) # Output: 155

num3 =+5
print(num3) # Output: 5 (this is an assignment statement, not an increment operator. It assigns the value of +5 to num3)

num3 += 5
print(num3) # Output: 10 (this is an increment operator. It adds


# and , or , not are logical operators. They are used to combine conditional statements.
x = 5 
y = 10
z = 15
print(x < y and y < z) # Output: True (both conditions are true)
print(x < y or y > z) # Output: True (one of the conditions is true)
print(not(x < y)) # Output: False (the condition is true, so not operator negates it to false)

# is, is not, in, not in are identity operators. They are used to compare the memory locations of two objects.
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # Output: False (a and b are two different objects in memory even though they have the same values)
print(a is not b) # Output: True (a and b are two different objects in memory)
c = a
print(a is c) # Output: True (a and c are the same object in memory)
print(b is c) # Output: False (b and c are two different objects in memory)

x= 5
y= 5
print(x is y) # Output: True (x and y are two different objects in memory but they have the same value, so they are considered equal)
# but a and b are two different objects in memory even though they have the same values, so they are not considered equal. This is because lists are mutable objects, while integers are immutable objects.
#mutable objects are like lists, dictionaries, and sets. They can be changed after they are created. Immutable objects are like integers, floats, strings, and tuples. They cannot be changed after they are created.