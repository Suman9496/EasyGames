from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def draw(self):
    pass

  @abstractmethod
  def calculate_area(self):
    pass

  @abstractmethod
  def calculate_perimeter(self):
    pass

class Square(Shape):
  def __init__(self, side_length):
    self.side_length = side_length

  def draw(self):
    print(f"Drawing a square with side length {self.side_length}")

  def calculate_area(self):
    return self.side_length * self.side_length

  def calculate_perimeter(self):
    return 4 * self.side_length

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def draw(self):
    print(f"Drawing a circle with radius {self.radius}")

  def calculate_area(self):
    return 3.14 * self.radius * self.radius

  def calculate_perimeter(self):
    return 2 * 3.14 * self.radius

# Create and use the shapes
square = Square(5)
circle = Circle(3)

square.draw()
circle.draw()

print(f"Square area: {square.calculate_area()}")
print(f"Circle area: {circle.calculate_area()}")
