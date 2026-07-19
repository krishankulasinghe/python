# create a class called Person and a property called x with a value of 5
class Person:
    x =5 
    
# Create an object named p1, and print the value of x:
p1 = Person()
print(p1.x) #5

#delete the property x from the object p1
del p1.x

# after deleting the property x from the object p1, we can create another object named p2 and print the value of x:
p2 = Person()
print(p2.x) # This will still print 5

#delete the property x from the class Person
del Person.x

# after deleting the property x from the class Person, we can create another object named p3 and print the value of x:
p3 = Person()
print(p3.x) # This will raise an AttributeError, because the property x has been deleted from the class Person and is no longer accessible.

# Pass statement : class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

#class Person1: # without pass statement, this will raise an error

class Person:
    pass

#The __init__() Method : All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.

#example:
class Person:
    def __init__(self, name, age): # self refers to the current Person object. self.name means "the name attribute of this object". Without self, Python would not know which object’s data you mean.
        self.name = name
        self.age = age
        
# Create an object named p1, and print the values of name and age:
p1 = Person("John", 36)
print(p1.name) # John
print(p1.age) # 36

# we can also use the __init__() function to set a default value for an attribute. If we do not pass a value for the age parameter, it will default to 0.
# If you do not give a default value like age=0, then age becomes a required parameter.
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        
# Create an object named p1, and print the values of name and age:
p1 = Person("John")
print(p1.name) # John
print(p1.age) # 0

# self Parameter: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class.

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

# class properties : Properties are variables that belong to the class. Class properties are shared by all instances of the class. 
# Instance properties are unique to each instance.

class Dog:
    species = "Canis familiaris"  # class property

    def __init__(self, name, age):
        self.name = name  # instance property
        self.age = age    # instance property

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris

print(dog1.name)  # Buddy
print(dog2.name)  # Max

# add new properties to existing objects:
# Note: Adding properties this way only adds them to that specific object, not to all objects of the class.
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age) # added new property age to existing object p1
print(p1.city) # added new property city to existing object p1

# delete properties from existing objects:
del p1.age
del p1.city 

# print(p1.age) # This will raise an AttributeError, because the property age has been deleted from the object p1 and is no longer accessible.

# __str__() Method : The __str__() method controls what should be returned when the class object is represented as a string.
# If the __str__() method is not set, the string representation of the object will be returned, like <__main__.Person object at 0x000001F4C8B8D9A0>.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} is {self.age} years old."

'''
  def str1(self): # in this way, we can also create a regular method called str1() that returns a formatted string, but unlike __str__(), it is NOT automatically called when the object is converted to string.
    return f"{self.name} ({self.age})"  
'''


p1 = Person("John", 36)
print(p1) # John is 36 years old. 

# delete methods 

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet # this will delete the greet() method from the class Person, and it will no longer be accessible from any object of the class.

# p1.greet() # This will cause an error