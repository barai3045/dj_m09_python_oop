# https://www.w3resource.com/python-exercises/oop/index.php


"""
1. Write a  Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
"""

from datetime import date
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return 2*math.pi*self.radius
    
#radius = float(input("Input radius: "))

"""circle = Circle(radius)
area = circle.area()
perimeter = circle.perimeter()"""


"""
2. Write a  Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
"""

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
        
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            
            age -=1
    
        return age
    
    
person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))


"""print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.age())

print("\nPerson 2:")
print("Name:", person2.name)
print("Country:", person2.country)
print("Date of Birth:", person2.date_of_birth)
print("Age:", person2.age())

print("\nPerson 3:")
print("Name:", person3.name)
print("Country:", person3.country)
print("Date of Birth:", person3.date_of_birth)
print("Age:", person3.age())"""


"""3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
"""

class Calculator:
    def add(self,x,y):
        return x + y
    
    def subtract(self, x, y):
        return x -y
    
    def multiply(self, x, y):
        return x*y
    
    def divide(self, x, y):
        if y != 0:
            return x/y
        else: 
            return ("Can't divide by zero.")
        
"""calculator = Calculator()
result = calculator.add(7, 5)
print("7 + 5 =", result)

# Perform subtraction and print the result
result = calculator.subtract(34, 21)
print("34 - 21 =", result)

# Perform multiplication and print the result
result = calculator.multiply(54, 2)
print("54 * 2 =", result)

# Perform division and print the result
result = calculator.divide(144, 2)
print("144 / 2 =", result)

# Attempt to perform division by zero, which raises an error, and print the error message
result = calculator.divide(45, 0)
print("45 / 0 =", result)"""


"""
4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
"""
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return 2*math.pi*self.radius
    
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length *self.width
    
    def parimeter(self):
        return 2*(self.length+self.width) 
    
    
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def area(self):
        return 0.5*self.base* self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    

"""
# Create a Rectangle object with given length and width and calculate its area and perimeter
l = 5
w = 7
rectangle = Rectangle(l, w)
rectangle_area = rectangle.area()
rectangle_perimeter = rectangle.perimeter()

# Print the results for the Rectangle
print("\nRectangle: Length =", l, " Width =", w)
print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)

# Create a Triangle object with a base, height, and three side lengths, and calculate its area and perimeter
base = 5
height = 4
s1 = 4
s2 = 3
s3 = 5

# Print the results for the Triangle
print("\nTriangle: Base =", base, " Height =", height, " side1 =", s1, " side2 =", s2, " side3 =", s3)
triangle = Triangle(base, height, s1, s2, s3)
triangle_area = triangle.area()
triangle_perimeter = triangle.perimeter()
print("Triangle Area:", triangle_area)
print("Triangle Perimeter:", triangle_perimeter)



r = 7
circle = Circle(r)
circle_area = circle.area()
circle_perimeter = circle.perimeter()

# Print the results for the Circle
print("Radius of the circle:", r)
print("Circle Area:", circle_area)
print("Circle Perimeter:", circle_perimeter)"""


"""
5. Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
"""

class Node:
    # Initialize the Node object with a value, and set the left and right child pointers to None
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Define a custom __str__ method to convert the node's value to a string
    def __str__(self):
        return str(self.value)

# Define a class called BinarySearchTree to represent a binary search tree
class BinarySearchTree:
    # Initialize the BST with an empty root node
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        # If the root is None, create a new node with the given value as the root
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Helper method to recursively insert a value into the BST
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Helper method to recursively search for a value in the BST and return the node if found
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

# Example usage
# Create an instance of BinarySearchTree
bst = BinarySearchTree()

# Insert values into the BST
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Search for elements in the BST and print the results
print("Searching for elements:")
print(bst.search(7))  # Found, returns the node (4)
print(bst.search(9))  # Not found, returns None 