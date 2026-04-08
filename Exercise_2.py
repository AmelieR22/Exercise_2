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

print(v1 * v2) # 10