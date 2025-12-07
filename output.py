name = "Prabhu"   # string
age = 25          # integer
height = 5.9      # float
is_student = True # boolean

print(name, age, height, is_student)
# Conditionals
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loops
for i in range(5):
    print("Loop iteration:", i)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1
    # Function
def add(num1,num2):
    return num1 + num2

print(add(4,7))

# Importing a module
import math
print(math.sqrt(16))  # square root

try:
    num = int("abc")  # invalid conversion
except ValueError as e:
    print("Error occurred:", e)

#Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, file!")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
class Car:
    # 1. The Constructor (The Setup)
    def __init__(self, brand, color):
        self.brand = brand  # Attribute
        self.color = color  # Attribute

    # 2. A Method (An Action)
    def honk(self):
        print(f"The {self.color} {self.brand} says Beep Beep!")

# --- Creating Objects ---

# Create 'my_car' (Object 1)
my_car = Car("Toyota", "Red")

# Create 'your_car' (Object 2)
your_car = Car("Ferrari", "Blue")

# Accessing data and actions
print(my_car.brand)  # Output: Toyota
your_car.honk() 
     # Output: The Blue Ford says Beep Beep!
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hi, I am {self.name} and I am {self.age} years old."

# Create object
user1 = User("Prabhu", 25)
print(user1.greet())

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Woof!

#1. The Parent Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print("Vroom! The engine is roaring.")

# 2. The Child Class
# We put 'Car' in parentheses to say: "ElectricCar IS A Car"
class ElectricCar(Car):
    def charge(self):
        print("Plugging in to charge...")

# --- Using Inheritance ---

my_tesla = ElectricCar("Tesla", "Model 3")

# It has access to its OWN methods
my_tesla.charge()   # Output: Plugging in to charge...

# It ALSO has access to the PARENT'S methods automatically
my_tesla.drive()    # Output: Vroom! The engine is roaring.
print(my_tesla.brand)
#polymorphism
class Car:
    def drive(self):
        print("Vroom! The engine is roaring.")

class ElectricCar(Car):
    def drive(self): # Overridden method
        print("Whoosh! Moving silently.")

class Motorcycle: # A completely different, non-inherited class
    def drive(self):
        print("Roar! The bike is accelerating.")   
        
def start_trip(vehicle):
    # This function works for Car, ElectricCar, or Motorcycle!
    print(f"Starting trip...")
    vehicle.drive()
    print("Trip started.")

# --- Creating Instances ---
gas_car = Car()
electric_car = ElectricCar()
bike = Motorcycle()

# --- Calling the function with different objects ---
start_trip(gas_car)
print("-" * 15)
start_trip(electric_car)
print("-" * 15)
start_trip(bike)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance()) 