# Dictionary : A dictionary is a collection of key-value pairs. Each key is unique and maps to a value. Dictionaries are mutable, meaning you can change their content without changing their identity.
# Dictionaries are defined using curly braces {} and key-value pairs are separated by colons :.
# Dictionaries can be nested, meaning a dictionary can contain another dictionary as a value. Dictionaries are unordered, meaning the order of the key-value pairs is not guaranteed to be the same as the order in which they were added.
# Values in a dictionary can be of any data type, including lists, tuples, and other dictionaries. Keys must be of an immutable data type, such as strings, numbers, or tuples.
# Dictionaries are useful for storing and retrieving data in a way that is easy to understand and manipulate

dictionary1 = {"name": "John", "age": 30, "city": "New York"}
print(dictionary1) # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(dictionary1["name"]) # Output: John (accessing the value associated with the key "name")
print(dictionary1.get("age")) # Output: 30 (accessing the value associated with the key "age" using the get() method)
print(dictionary1.keys()) # Output: dict_keys(['name', 'age', 'city']) (returns a view object that displays a list of all the keys in the dictionary)
print(dictionary1.values()) # Output: dict_values(['John', 30, 'New York']) (returns a view object that displays a list of all the values in the dictionary)
dictionary1["age"] = 31 # updating the value associated with the key "age"
print(dictionary1["area"]) # throws a KeyError because the key "area" does not exist in the dictionary
print(dictionary1.get("area")) # Output: None (returns None because the key "area" does not exist in the dictionary)
dictionary1["area"] = "Manhattan" # adding a new key-value pair to the dictionary
print(dictionary1) # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'area': 'Manhattan'} (the dictionary now contains the new key-value pair)

dictionary1.update({"age": 32, "city": "Los Angeles"}) # updating multiple key-value pairs in the dictionary
print(dictionary1) # Output: {'name': 'John', 'age': 32, 'city': 'Los Angeles', 'area': 'Manhattan'} (the dictionary now contains the updated key-value pairs)

del dictionary1["area"] # deleting a key-value pair from the dictionary
print(dictionary1) # Output: {'name': 'John', 'age': 32, 'city': 'Los Angeles'} (the dictionary now contains the updated key-value pairs)
dictionary1.pop("city") # removing a key-value pair from the dictionary using the pop() method
print(dictionary1) # Output: {'name': 'John', 'age': 32}
dictionary1.popitem() # removing the last inserted key-value pair from the dictionary using the popitem() method
print(dictionary1) # Output: {'name': 'John'} (the dictionary now contains the updated key-value pairs)


dictionary1.clear() # removing all key-value pairs from the dictionary
print(dictionary1) # Output: {} (the dictionary is now empty)

dictionary2 = {"name": "Alice", "age": 25, "city": "Chicago"}
dictionary3 = {"name": "Bob", "age": 35, "city": "San Francisco"}
merged_dictionary = {**dictionary2, **dictionary3} # merging two dictionaries using the unpacking operator **
print(merged_dictionary) # Output: {'name': 'Bob', 'age': 35, 'city': 'San Francisco'} (the merged dictionary contains the key-value pairs from both dictionaries, with the values from dictionary3 overwriting those from dictionary2 for any duplicate keys)
dictionary4 = {"name1": "Charlie", "age1": 40, "city1": "Seattle"}
print(**dictionary4, **merged_dictionary) # Output: {'name1': 'Charlie', 'age1': 40, 'city1': 'Seattle', 'name': 'Bob', 'age': 35, 'city': 'San Francisco'} (the merged dictionary contains the key-value pairs from both dictionaries, with the values from merged_dictionary overwriting those from dictionary4 for any duplicate keys)
dictionary5 = dictionary2.copy() # creating a shallow copy of dictionary2
print(dictionary5) # Output: {'name': 'Alice', 'age': 25, 'city': 'Chicago'} (the copied dictionary contains the same key-value pairs as dictionary2)