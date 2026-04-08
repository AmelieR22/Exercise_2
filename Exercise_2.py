#Exercise_2

#1
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __repr__(self):
        return f"{self.real} + {self.imag}j"

c1 = Complex(1, 2)
c2 = Complex(3, 4)
c3 = c1 + c2
c4 = c1 - c2

print(c3) # 4 + 6j
print(c4) # -2 - 2j

#2
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def __gt__(self, other):
        return self.age > other.age
    
p1 = Person("John", 30, "Male")
p2 = Person("Jane", 25, "Female")

print(p1 > p2) # True

#3
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
v1 = Vector(1, 2, 3)
v2 = Vector(3, 2, 1)

print(v1 * v2) # 

#5
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def __lt__(self, other):
        return self.radius < other.radius
        
    def __le__(self, other):
        return self.radius <= other.radius
        
    def __eq__(self, other):
        return self.radius == other.radius
        
    def __ne__(self, other):
        return self.radius != other.radius
        
    def __gt__(self, other):
        return self.radius > other.radius
        
    def __ge__(self, other):
        return self.radius >= other.radius
        
c1 = Circle(5)
c2 = Circle(6)
print(c1 < c2) # Output: True
print(c1 > c2) # Output: False
print(c1 == c2) # Output: False


#6
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __lt__(self, other):
        return self.distance() < other.distance()

    def __le__(self, other):
        return self.distance() <= other.distance()

    def __eq__(self, other):
        return self.distance() == other.distance()

    def __ne__(self, other):
        return self.distance() != other.distance()

    def __gt__(self, other):
        return self.distance() > other.distance()

    def __ge__(self, other):
        return self.distance() >= other.distance()

p1 = Point(1, 1)
p2 = Point(2, 2)

print(p1 < p2) # True
print(p1 == p2) # False


#7
\class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __mul__(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                sum = 0
                for k in range(len(other.matrix)):
                    sum += self.matrix[i][k] * other.matrix[k][j]
                row.append(sum)
            result.append(row)
        return Matrix(result)
        
    def __str__(self):
        return str(self.matrix)
        
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
m3 = m1 * m2
print(m3) # Output: [[19, 22], [43, 50]]

#Inheritance
#I1
class Vehicle:
    def drive(self):
        return "Driving a vehicle"

class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"