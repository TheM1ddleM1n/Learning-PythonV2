### ✅ Class:

**A class** in python is a blueprint for creating objects. It groups related data (attributes) and actions (methods) together. Think of a class like a template; where it defines characteristics like color, size, etc...

```Python
class Book:
    pass
```

### ✅ Object:

**An object** is an instance of a class in Python. It represents a specific example of the blueprint defined by class. Now with our Dog; If Dog is a class, then variable `my_dog` could be an object representing a specific dog with it's details or functions, like name or age.

```Python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Object of the Dog class
my_dog = Dog("Schrodinger", 5)
```

### ✅ Inheritance:

**Inheritance** allows you to create a new class that uses the features of an already existing class without necessarily changing it. This lets you build on existing functionality while keeping the original class intact.

```Python
class Animal:
    def __init__(self, name):
        self.name = name

    def spreche(self):
        print(f"{self.name} sagst: Sei zufrienden")

#Derived class
class Dog(Animal):
    def spreche(self):
        print(f"{self.name} bellst")
```

#### Creating an object for the dog class

```Python
my_dog = Dog("Arf")
my_dog.spreche()  # Output: Arf bellst
```

Dog is a derived class which inherits from Animal class. Overrides `spreche(speak)` method to provide a behavior for parsed in `(Animal)`.
'''

### ✅ Encapsulation:

In Python's **Object-Oriented Programming (OOP)**, we can restrict access to methods and variables to prevent direct modification, especially when dealing with multiple lines of codes all performing various functions. This is referred to as **encapsulation**.

```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age  # Accessor method

person = Person("Alice", 30)
print(person.get_age())  # Gives an output of 30
```

It's noted from this example that the `the__age` attribute is private, and can only be accessed by calling the `get_age()` method.

### ✅ Polymorphism:

**Polymorphism** really means "more than one forms." In programming _(python🤧)_, polymorphism allows a single entity (like a method, operator, or object) to take on different forms and behave differently in various scenarios, as needed.

```Python
class Pferd:
    def speak(self):
        print("Neigh")

class Eule:
    def speak(self):
        print("Hoot")

def animal_speak(animal):
    animal.speak()

# Using polymorphism
pferd = Pferd()
eule = Eule()

animal_speak(pferd)  # Neigh
animal_speak(eule)   # Hoot

        ### Try Area
```

#### Basic Functions

Functions are simple, don't include any parameters or return values, and perform a single task, like so...

```Python
def greet_group():
    print("Hallo, Leute!")

def greet_person(name):
    print(f"Hallo, {name}")
```

#### Functions with Return Values

functions return values, used instead of printing, allowing caller to use the result, return ends the code and starts outside the function(def).

```Python
def add(a, b):
    return a + b
result = add(3, 5)
print(result)
```

#### Functions with Default Parameters

: Introducing default parameters makes the function to be more versatile.

```Python
def greet(name= "Welt"):
    print(f"Hallo, {name}!")
greet()
greet("Henify_") # Replaces name="..." value to Henify_
```

#### Functions with Variable Arguments

Using " **\*args** and **\*\*kwargs** in python lets functions to handle variable number arguments.

```Python
def add_all(*args):       # With *args
    return sum(args)
print(add_all(1, 2, 3, 4, 5))

def print_info(**kwargs):  # With **kwargs
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name= "Henry", age= 17)
```

### Intermediate Functions (Higher_Order_Functions, Lambdas, and Decorators)

Higher level functions; these functions take other functions as arguments or return them. **Lambdas**; Anonymous, inline functions.
Decorators: Modifies behavior of other functions

```Python
def apply_functions(func, value):
    return func(value)
print(apply_functions(lambda x: x**2, 5))

def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper()

@decorator  #Decorator
def say_hello():
    print("Hallo ✌🏾")
say_hello()
```
