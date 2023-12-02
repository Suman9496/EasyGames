# Parent class
class Animal:
    def sound(self):
        return "Some generic sound"

# Child class inheriting from Animal
class Dog(Animal):
    def sound(self):
        return "Woof!"

# Child class inheriting from Animal
class Cat(Animal):
    def sound(self):
        return "Meow!"

# Creating instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the methods
print(animal.sound())  # Output: Some generic sound
print(dog.sound())     # Output: Woof!
print(cat.sound())     # Output: Meow!
method_overriding