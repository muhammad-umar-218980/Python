# ======================
# Python Variable Declarations
# ======================
# Python has one way to declare variables 
# All variables follow the same scoping rules

# ======================
# Variable Scope in Python
# ======================
# The only scopes in Python are:
# 1. Local (inside function)
# 2. Enclosing (for nested functions)
# 3. Global (module-level)
# 4. Built-in (Python's predefined names)

# ----------------------
# 1. No Block Scope 
# ----------------------
if True:
    x = 8  # Not block-scoped - accessible outside
print(x)  # 8 

for i in range(3):
    loop_var = i * 2
    
print(loop_var)  # 4 (accessible after loop ends)

# ----------------------
# 2. Function Scope (creates new scope)
# ----------------------
def test():
    y = 10  # Function-scoped variable
    print("Inside function:", y)  # Works

test()
try:
    print(y)  # ❌ NameError
except NameError:
    print("Cannot access function-scoped 'y' outside function")

# ----------------------
# 3. Global Scope
# ----------------------
global_var = "I'm global"

def show_global():
    print(global_var)  # Can access globals
    
show_global()

def modify_global():
    global global_var  # Need 'global' keyword to modify
    global_var = "Modified"
    
modify_global()
print(global_var)  # Shows "Modified"

# ----------------------
# 4. Enclosing Scope (for nested functions)
# ----------------------
def outer():
    outer_var = "I'm in outer function"
    
    def inner():
        print(outer_var)  # Can access enclosing scope
        # nonlocal outer_var  # Needed if we want to modify it
    
    inner()

outer()

# ======================
# Constants in Python
# ======================
# Python doesn't have true constants - convention is to use ALL_CAPS
PI = 3.14  # By convention, shouldn't be changed
PI = 3.14159  # But this actually works (no error)

# To create real immutability:
# Option 1: Use enum
from enum import Enum
class Constants(Enum):
    PI = 3.14159
    GRAVITY = 9.8

# Option 2: Use namedtuple
from collections import namedtuple
Constants = namedtuple('Constants', ['PI', 'GRAVITY'])
const = Constants(3.14159, 9.8)

# ======================
# Variable Characteristics
# ======================
# 1. Dynamic Typing
var = 10      # Starts as integer
var = "Hello" # Becomes string
var = [1,2,3] # Now a list

# 2. No Declaration Needed
# Variables are created when first assigned
new_var = "I'm created when assigned"

# 3. Reference System
# Variables store references to objects
a = [1,2,3]
b = a  # Both point to same list
b.append(4)
print(a)  # [1,2,3,4]

# ======================
# Best Practices
# ======================
# 1. Naming:
#    - Use snake_case for variables
#    - Use ALL_CAPS for "constants"
#    - Avoid single-letter names (except in loops)
#    - Be descriptive (e.g., 'user_count' vs 'uc')

# 2. Scoping:
#    - Prefer local variables
#    - Minimize use of global variables
#    - Use nonlocal for nested function communication

# 3. Initialization:
#    - Initialize variables before use
#    - None is useful for placeholder values

# 4. Type Hints (Python 3.5+):
#    - Optional but recommended for larger projects
def calculate(total: float, count: int) -> float:
    return total / count

# ======================
# Practical Scoping Example
# ======================
def counter():
    count = 0
    
    def increment():
        nonlocal count  # Needed to modify enclosing scope
        count += 1
        return count
    
    return increment

counter1 = counter()
print(counter1())  # 1
print(counter1())  # 2

# ==============
# LEGB Rule 
# ==============
# Python looks for variables in this order:
# 1. Local (L)
# 2. Enclosing (E)
# 3. Global (G)
# 4. Built-in (B)

name = "Global Name"  # Global

def greet():
    name = "Enclosing Name"  # Enclosing
    
    def hello():
        name = "Local Name"  # Local
        print(name)  # Uses local
        
    hello()

greet()  # Prints "Local Name"