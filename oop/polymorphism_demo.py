import math

class Shape:
    """
    Base class for all geometric shapes. Defines the common interface 'area()'.
    """
    def area(self):
        """
        Base method that must be overridden by all derived classes.
        """
        # This error enforces that subclasses must implement their own logic.
        raise NotImplementedError("Subclass must implement abstract method 'area'")

class Rectangle(Shape):
    """
    Derived class representing a rectangle. Overrides the area() method.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle: length * width.
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class representing a circle. Overrides the area() method.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle: π * radius².
        """
        # Use math.pi for accurate calculation
        return math.pi * (self.radius ** 2)