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

# Inheritance : Inheritance allows us to define a class that inherits all the methods and properties from another class. 
# The parent class is the class being inherited from, also called base class.
#  The child class is the class that inherits from another class, also called derived class.

#base class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello!")

# child class
class Student(Person):
   pass # pass means that the Student class inherits all the properties and methods from the Person class, but does not add any new properties or methods of its own.
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

x = Student("Mike", 21)
print(x.name) # Mike
print(x.greet()) # Hello!

# add __init__() function to the child class : When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

class Student(Person):
  def __init__(self, name, age, student_id):
     Person.__init__(self, name, age) # we have to call the parent's __init__() function explicitly to initialize the inherited properties.
     self.student_id = student_id

# The super() Function : Python also has a super() function that will make the child class inherit all the methods and properties from its parent.
# super() lets you call the parent class's methods (like __init__) WITHOUT typing the parent class's name directly.
# It does the exact same job as "Person.__init__(self, name, age)" above, but it's the recommended/cleaner way to do it.

class Student(Person):
  def __init__(self, name, age, student_id):
     super().__init__(name, age) # same as Person.__init__(self, name, age), but we don't need to mention "Person" or pass "self" manually.
     self.student_id = student_id

s1 = Student("Anna", 20, "S123")
print(s1.name)        # Anna       (comes from Person, set up via super())
print(s1.age)          # 20         (comes from Person, set up via super())
print(s1.student_id)   # S123       (comes from Student itself)

# Why use super() instead of Person.__init__(self, ...) ?
# 1. You don't have to repeat the parent class's name.
# 2. If you later rename the parent class (e.g. Person -> Human), you only need to update it in one place (the "class Student(Person)" line),
#    instead of also updating every "Person.__init__(...)" call.

# Beginner rule of thumb: whatever parameters the parent's __init__() requires, the child's __init__() must also accept them,
# so it can hand them over (forward them) to super().__init__().

# Below are 3 common exceptions/variations to that rule:

# Exception 1: The parent has a default value, so the child does not have to accept/pass it.
class Person:
    def __init__(self, name, age=0): # age has a default value
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, student_id): # no "age" here, that's okay
        super().__init__(name) # age will just default to 0
        self.student_id = student_id

s2 = Student("Liam", "S200")
print(s2.name)        # Liam
print(s2.age)          # 0 (default value, since we never passed one)
print(s2.student_id)   # S200

# Exception 2: The child can hardcode/fix a value instead of asking for it as a parameter.
class Student(Person):
    def __init__(self, student_id): # notice: no "name" parameter at all
        super().__init__("Unknown", 0) # fixed values, not passed in from outside
        self.student_id = student_id

s3 = Student("S300")
print(s3.name)        # Unknown
print(s3.age)          # 0
print(s3.student_id)   # S300

# Exception 3: The child doesn't define __init__() at all, so it just inherits the parent's constructor as-is.
class Student(Person):
    pass # no __init__ here, so Student uses Person's __init__ automatically

s4 = Student("Noah") # uses Person's __init__(self, name, age=0)
print(s4.name)        # Noah
print(s4.age)          # 0

# Note: super().__init__() is only needed for attributes (self.name, self.age), NOT for methods.
# Methods (like greet()) are always inherited automatically, even without calling super().

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello!")

class Student(Person):
    def __init__(self, name, age, student_id):
        # no super().__init__() here
        self.student_id = student_id

s5 = Student("Mike", 21, "S100")
s5.greet()   # Hello!  -> works fine, methods don't need super()
# s5.name    # AttributeError -> attributes need super().__init__() to be set



# Overriding a method: if the child defines a method with the SAME name as the parent, the child's version is used instead.
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):              # this overrides Person's greet()
        super().greet()           # optional: still call the parent's version too
        print(f"I'm a student with ID {self.student_id}")

s6 = Student("Anne", 20, "S123")
s6.greet()
# Hello!
# I'm a student with ID S123

# Polymorphism : "Poly" = many, "morph" = forms. It means the SAME method name can behave differently depending on which class's object is calling it.
# In practice, this usually happens through method overriding (like greet() overriding earlier) - each child class gives its own version of a method,
# but you can still call that method the same way on every object, without caring which exact class it is.

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass # no __init__ or move() override, so Car uses Vehicle's move() as-is

class Boat(Vehicle):
  def move(self):        # overrides Vehicle's move()
    print("Sail!")

class Plane(Vehicle):
  def move(self):        # overrides Vehicle's move()
    print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# Even though car1, boat1, plane1 are different classes, we can call x.move() on all of them the same way.
# Python automatically picks the correct version of move() for each object - that's polymorphism.
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
  # Car  -> Move!  (inherited from Vehicle, not overridden)
  # Boat -> Sail!  (Boat's own version)
  # Plane -> Fly!  (Plane's own version)

# Encapsulation : Keeping data (properties) and methods together inside a class, while controlling how that data
# can be accessed/changed from outside the class. This protects data from accidental changes.

# Private properties: add a double underscore "__" prefix to make a property private.
# Private properties CANNOT be accessed directly from outside the class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private property

p1 = Person("Emil", 25)
print(p1.name)      # Emil (works fine, public property)
# print(p1.__age)   # AttributeError -> can't access a private property directly from outside

# Getter method: a normal method used to safely READ a private property's value from outside the class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

p2 = Person("Tobias", 25)
print(p2.get_age())  # 25

# Setter method: a normal method used to safely CHANGE a private property's value, usually with validation.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p3 = Person("Tobias", 25)
print(p3.get_age())  # 25
p3.set_age(26)        # allowed, 26 is positive
print(p3.get_age())  # 26
p3.set_age(-5)        # rejected by the setter's validation
print(p3.get_age())  # 26 (unchanged)

# Why use encapsulation ?
# 1. Data protection - prevents code outside the class from accidentally overwriting data with a bad value.
# 2. Validation - the setter method can check a value is valid BEFORE saving it.
# 3. Flexibility - you can change how something works internally without breaking code that uses the class.
# 4. Control - you decide exactly how properties can be read or changed from outside.

# Protected properties: use a single underscore "_" prefix. This is just a naming convention/hint for other
# programmers ("this is for internal use"), Python does NOT actually block access to it.
class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # protected property (convention only)

p4 = Person("Linus", 50000)
print(p4.name)      # Linus
print(p4._salary)   # 50000 -> still accessible, but shouldn't be accessed directly from outside

# Private methods: same "__" prefix rule also works on methods, not just properties.
# A private method can only be called from other methods INSIDE the same class.
class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):  # private method
        return isinstance(num, (int, float))

    def add(self, num):
        if self.__validate(num):  # ok to call from inside the class
            self.result += num
        else:
            print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)   # 15
# calc.__validate(5) # AttributeError -> can't call a private method from outside the class

# Name mangling: this is HOW Python actually implements "__" privacy behind the scenes.
# Python renames __age internally to _ClassName__age (e.g. __age -> _Person__age).
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p5 = Person("Emil", 30)
print(p5._Person__age)  # 30 -> technically works, but NOT recommended (it defeats the point of encapsulation)

