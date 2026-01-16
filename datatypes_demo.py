# datatypes_demo.py
# Task 2: Variables, Data Types & Type Conversion

# Declaring variables of different data types
age = 21              # int
height = 5.8          # float
name = "Rahul"        # string
is_student = True     # boolean

# Printing the type of each variable
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))

print("\n--- Arithmetic Operations ---")

# Arithmetic operations
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("\n--- Type Conversion ---")

# Converting string to int and float
num_str = "50"
num_int = int(num_str)       # string to int
num_float = float(num_str)   # string to float

print("Integer value:", num_int)
print("Float value:", num_float)

print("\n--- Error Handling Example ---")

# Handling invalid input
invalid_input = "abc"

try:
    value = int(invalid_input)
except ValueError:
    print("Error: Cannot convert string to integer")

print("\n--- String Concatenation ---")

# Concatenating string and number
print("My age is " + str(age))

print("\n--- Dynamic Typing ---")

# Demonstrating dynamic typing
x = 100
print("x =", x, "Type:", type(x))

x = "Python"
print("x =", x, "Type:", type(x))
