from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def eat(self):
    pass

  @abstractmethod
  def move(self):
    pass

  @abstractmethod
  def reproduce(self):
    pass

class Cat(Animal):
  def eat(self):
    print("Cat eats mouse")

  def move(self):
    print("Cat walks silently")

  def reproduce(self):
    print("Cat gives birth to kittens")

class Dog(Animal):
  def eat(self):
    print("Dog eats kibble")

  def move(self):
    print("Dog wags tail and barks")

  def reproduce(self):
    print("Dog gives birth to puppies")

# Create and use the animals
cat = Cat()
dog = Dog()

cat.eat()
dog.move()
