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
    
    #I2
    class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def introduce(self):
        return "Hi, my name is {} and I am {} years old.".format(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        Person.__init__(self, name, age, address)
        self.field_of_study = field_of_study
    
    def introduce(self):
        introduction = Person.introduce(self)
        return "{} I am a student studying {}.".format(introduction, self.field_of_study)

class Employee(Person):
    def __init__(self, name, age, address, company):
        Person.__init__(self, name, age, address)
        self.company = company
    
    def introduce(self):
        introduction = Person.introduce(self)
        return "{} I work at {}.".format(introduction, self.company)

person = Person("John Doe", 30, "123 Main St.")
student = Student("Jane Doe", 20, "456 Elm St.", "Computer Science")
employee = Employee("Jim Smith", 40, "789 Oak St.", "Acme Inc.")

people = [person, student, employee]
for person in people:
    print(person.introduce())

# Output:
# Hi, my name is John Doe and I am 30 years old.
# Hi, my name is Jane Doe and I am 20 years old. I am a student studying Computer Science.
# Hi, my name is Jim Smith and I am 40 years old. I work at Acme Inc.
    
    #I3
    class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
    
    def transfer(self, destination_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            destination_account.deposit(amount)
            return True
        else:
            return False

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        BankAccount.__init__(self, account_number, balance)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        
    def check_balance(self):
        return self.balance

# create two savings accounts
savings_account1 = SavingsAccount(account_number="12345", balance=1000, interest_rate=0.05)
savings_account2 = SavingsAccount(account_number="67890", balance=500, interest_rate=0.03)

# transfer money from one account to another
if savings_account1.transfer(destination_account=savings_account2, amount=100):
    print("Transfer successful")
else:
    print("Transfer failed")

# check the balance of both accounts
print("Savings Account 1 Balance:", savings_account1.check_balance())