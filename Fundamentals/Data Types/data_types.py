# Primitive Data Types

name = "Alice"      # str (immutable sequence of characters)
age = 25           # int (integer number)
big_num = 12345678901234567890  # int (Python handles arbitrary precision integers)
is_student = True   # bool (boolean value)
city = None         # NoneType (represents absence of value)

# Non-Primitive Data Types

person = { 
  "name": "Alice",
  "age": 25 
} # dict 

numbers = [1, 2, 3, 4] # list 

def greet():
    print("Hello!") # function 

# Additional Python collection types
my_tuple = (1, 2, 3)  # tuple (immutable sequence) 
my_set = {1, 2, 3}    # set (mutable, unordered collection of unique elements)

# Special numeric values
import math
try:
    print("Hello" / 2) # Raises TypeError (Python doesn't auto-convert to NaN)
except TypeError:
    print("Cannot divide string by number") 

print(math.nan)  # nan (Not a Number)
print(type(math.nan)) # float (nan is considered float type in Python)

try:
    print(1 / 0) # Raises ZeroDivisionError 
except ZeroDivisionError:
    print("Cannot divide by zero")

print(float('inf'))  # inf (positive infinity)
print(type(float('inf'))) # float

print(float('-inf')) # -inf (negative infinity)
print(type(float('-inf'))) # float

# Checking types using type() function
print(type("Hello"))    # <class 'str'>
print(type(42))         # <class 'int'>
print(type(12345678901234567890)) # <class 'int'>
print(type(True))       # <class 'bool'>
print(type(None))       # <class 'NoneType'>
print(type({"name": "Alice"})) # <class 'dict'>
print(type([1, 2, 3]))  # <class 'list'>
print(type(greet))      # <class 'function'>
print(type(math.nan))   # <class 'float'>
print(type(float('inf'))) # <class 'float'>

# Mutable vs Immutable Data Types
# Immutable types cannot be changed after creation
# Mutable types can be modified after creation

# Immutable example (str)
s = "Hello"
try:
    s[0] = "h" # Raises TypeError
except TypeError:
    print("Strings are immutable in Python")

# Mutable example (list)
lst = [1, 2, 3]
lst[0] = 4 # Works fine
print(lst) # [4, 2, 3]

# Copy behavior
# Immutable types are copied by value
x = 5
y = x
y = 10
print(x) # 5 (unchanged)

# Mutable types are copied by reference
lst1 = [1, 2, 3]
lst2 = lst1
lst2[0] = 4
print(lst1) # [4, 2, 3] (original changed)

# Data Type Conversion

# Explicit Conversion
num = 123
print(str(num)) # "123" (convert to string)

s = "123"
print(int(s))   # 123 (convert to integer)

# Boolean conversion
print(int(True))  # 1
print(int(False)) # 0

# Implicit Conversion 
try:
    print(5 + "10") # Raises TypeError 
except TypeError:
    print("Python requires explicit type conversion")

# Equality comparison
print("5" == 5) # False (Python doesn't coerce types)

# Truthy/Falsy Values
# Falsy values in Python:
print(bool(0))     # False
print(bool(0.0))   # False
print(bool(""))    # False
print(bool(None))  # False
print(bool([]))    # False (empty list)
print(bool(()))    # False (empty tuple)
print(bool({}))    # False (empty dict)
print(bool(set())) # False (empty set)

# Truthy values in Python:
print(bool(1))      # True
print(bool(-1))     # True
print(bool("0"))    # True (non-empty string)
print(bool("False")) # True (non-empty string)
print(bool([1]))    # True (non-empty list)
print(bool((1,)))   # True (non-empty tuple)
print(bool({"a":1})) # True (non-empty dict)
print(bool({1}))    # True (non-empty set)