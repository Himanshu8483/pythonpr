# PYTHON NOTES 

# ADVANTAGES OF PYTHON:
# 1. Easy to learn due to simple syntax.
# 2. Dynamically typed language: No need to define variable types.
# 3. Extensive library support (e.g., NumPy, Pandas, Flask).
# 4. Compatible with other programming languages.
# 5. Platform-independent: Write once, run anywhere.
# 6. Strong community support (e.g., Stack Overflow).

# DISADVANTAGES OF PYTHON:
# 1. Slower than compiled languages (e.g., C++).
# 2. Prone to runtime errors due to dynamic typing.
# 3. Cannot create web applications directly; requires third-party frameworks like Django or Flask.
#    Explanation: Python itself lacks built-in web development capabilities. 
#    To create web applications, developers use frameworks like Django (full-stack) or Flask (lightweight).
# 4. Relatively weak in memory management compared to lower-level languages.

# TOKENS IN PYTHON:
# A token is the smallest unit in a program. Examples include:
# 1. Keywords (e.g., if, else, while).
# 2. Identifiers (e.g., variable names).
# 3. Literals (e.g., numbers, strings).
# 4. Operators (e.g., +, -, *, /).
# 5. Delimiters (e.g., :, {}, []).

# COMMONLY USED FUNCTIONS:
# print(): Outputs data to the console.
print("Hello, World!")  # Output: Hello, World!

# input(): Takes user input as a string.
name = "John"  # Simulating input for understanding
print("Hello,", name)  # Output: Hello, John

# type(): Returns the data type of a variable.
x = 10
print(type(x))  # Output: <class 'int'>

# id(): Returns the memory address of an object.
print(id(x))  # Example Output: 140718351963152 (unique memory address)

# max(), min(), sum(), len():
numbers = [5, 10, 15, 20]
print(max(numbers))  # Output: 20
print(min(numbers))  # Output: 5
print(sum(numbers))  # Output: 50
print(len(numbers))  # Output: 4

# CONVERTING PYTHON SOURCE CODE TO BYTECODE AND EXECUTABLE:
# 1. Python source code (.py) -> Bytecode (.pyc) -> Machine code (via PVM and JIT).

# Example of creating bytecode:
# Command: py -m py_compile yourfile.py
# This generates a compiled .pyc file in the __pycache__ folder.

# 2. Creating an executable file:
# Command: pyinstaller --onefile yourfile.py
# Steps:
# a) Install PyInstaller: `pip install pyinstaller`.
# b) Run: `pyinstaller --onefile yourfile.py`.
# c) Find the executable in the `dist` folder.

# WORKING WITH PICKLING AND UNPICKLING:
# Pickling: Converting Python objects to byte streams (used for saving data).
# Unpickling: Loading data from byte streams back into Python objects.

# BASIC COMMANDS AND USAGE:
# 1. Open terminal: Press Ctrl + Backtick (`) in most IDEs like VS Code.
# 2. Execute Python file: `python filename.py` or `py filename.py`.
# 3. Change directory in terminal: `cd path_to_directory`.
# 4. Check Python version: `python --version`.

# PYTHON'S INTERNAL WORKINGS:
# 1. Python is an interpreted + compiled language:
#    - Source code (.py) is first compiled to Bytecode (.pyc).
#    - The Bytecode is interpreted by the Python Virtual Machine (PVM) and executed.
# 2. JIT (Just-In-Time Compiler):
#    - Part of some Python implementations (e.g., PyPy).
#    - Converts Bytecode to machine code during runtime for better performance.

# PYTHON AS AN OPEN-SOURCE BACKEND LANGUAGE:
# 1. Open-source: Freely available with a strong community.
# 2. Backend development: Used for APIs, databases, and server-side logic.
#    Frameworks include Flask, Django, and FastAPI.

# PYTHON FILE EXECUTION SUMMARY:
# 1. Source Code (.py) -> Compiled to Bytecode (.pyc) -> Interpreted by PVM.
# 2. Use `pyinstaller` to create a standalone executable from a Python script.
#    This allows you to run Python programs on systems without Python installed.


# CONCLUSION:
# 1. Python is versatile and widely used for web development, data science, and automation.
# 2. Understanding Python's internal workflow (Source Code -> Bytecode -> Machine Code) is crucial for interviews.
# 3. Practice the commands, frameworks, and functions above to strengthen your knowledge.


# COMMONLY USED FUNCTIONS:
# print(): Outputs data to the console.
print("Hello, World!")  # Output: Hello, World!

# input(): Takes user input.
# Uncomment the next line to test:
# name = input("Enter your name: ")  # Enter: John
name = "John"  # Simulated input
print("Hello,", name)  # Output: Hello, John

# type(): Shows the data type of a variable.
x = 10
print(type(x))  # Output: <class 'int'>

# id(): Displays the memory address of a variable.
print(id(x))  # Example Output: 140718351963152

# max(), min(), sum(), len():
numbers = [5, 10, 15, 20]
print(max(numbers))  # Output: 20
print(min(numbers))  # Output: 5
print(sum(numbers))  # Output: 50
print(len(numbers))  # Output: 4

# WORKING WITH KEYWORDS
import keyword

# Lists of Python keywords and soft keywords
x = keyword.kwlist
y = keyword.softkwlist

# Uncomment to view keywords
# print(x)
# print(y)

# Count of keywords
print("Number of keywords:", len(x))
print("Number of soft keywords:", len(y))

# PUNCTUATIONS:
# Punctuations in Python are used as delimiters, operators, etc.
import string
print(string.punctuation)  
# Output: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(len(string.punctuation))  # Output: 32

# IDENTIFIERS:
# Rules for naming:
# 1. Must begin with a letter or an underscore.
# 2. Cannot start with a number.
# 3. Can contain letters, numbers, and underscores.
# 4. Case-sensitive (e.g., "Name" and "name" are different).

_x = 10  # Valid
print(_x)  # Output: 10

# Invalid identifier example:
# x y = 10  # Space not allowed in identifiers

him_8483 = 'himanshu_kushwaha'
print("Identifier him_8483:", him_8483)
print("Memory address of him_8483:", id(him_8483))

# OPERATORS:
# 1. Arithmetic Operators:
# +, -, *, /, %, // (floor division), ** (exponent)
a, b = 10, 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a // b)  # Output: 3
print(a ** b)  # Output: 1000

# 2. Comparison Operators:
# ==, !=, >, <, >=, <=
x, y = 10, 20
print(x == y)  # Output: False
print(x != y)  # Output: True

# 3. Logical Operators:
# and, or, not
print(x < y and y > 15)  # Output: True
print(not (x > y))       # Output: True

# 4. Bitwise Operators:
# &, |, ~, ^, <<, >>
x, y = 5, 3  # Binary: x=101, y=011
print(x & y)  # Output: 1 (binary AND)
print(x | y)  # Output: 7 (binary OR)
# Applying the bitwise NOT operator '~' (to get the 2's complement)
# The ~ operator inverts the bits, and then adding 1 gives the negative version (2's complement).
# ~num is equivalent to -num - 1
print(~x)     # Output: -6 (bitwise NOT)
print(x << 1) # Output: 10 (left shift)     num*2^no. of shift
print(x >> 1) # Output: 2 (right shift)     num/2^no. of shift

# Comparing addresses using 'is' and comparing values using '=='

x = [10]  # A list with one element 10
y = [10]  # Another list with the same element 10

# '==' compares the values inside the objects, so both lists have the same value
print(x == y)  # True: because the values inside both lists are equal (10)

# 'is' compares the memory addresses (i.e., if both variables point to the same object in memory)
print(x is y)  # False: because they are two different objects in memory, even though their values are same.

# NUMBER SYSTEMS:
# Types: Binary (0b), Octal (0o), Decimal, Hexadecimal (0x)
x = 10
print(bin(x))  # Output: 0b1010
print(oct(x))  # Output: 0o12
print(hex(x))  # Output: 0xa

# DATA TYPES AND LITERALS:
# 1. Numeric Types: int, float, complex
x = 10
y = 3.14
z = 1 + 2j
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'complex'>

# 2. String:
string = "Hello, Python!"
print(type(string))  # Output: <class 'str'>

# 3. List:
my_list = [1, 2, 3, "Python"]
print(my_list)       # Output: [1, 2, 3, 'Python']
print(type(my_list)) # Output: <class 'list'>

# 4. Tuple:
my_tuple = (1, 2, 3, "Python")
print(my_tuple)       # Output: (1, 2, 3, 'Python')
print(type(my_tuple)) # Output: <class 'tuple'>

# 5. Dictionary:
my_dict = {"name": "John", "age": 30}
print(my_dict)       # Output: {'name': 'John', 'age': 30}
print(type(my_dict)) # Output: <class 'dict'>

# 6. Set:
my_set = {1, 2, 3, 2, "Python"}
print(my_set)       # Output: {1, 2, 3, 'Python'} (unique values only)
print(type(my_set)) # Output: <class 'set'>

# 7. Frozenset:
my_frozenset = frozenset([1, 2, 3, "Python"])
print(my_frozenset)       # Output: frozenset({1, 2, 3, 'Python'})
print(type(my_frozenset)) # Output: <class 'frozenset'}

# Set: A set is mutable, meaning you can add or remove elements from a set after it is created.
# Frozenset: A frozenset is immutable, meaning once it's created, you cannot modify it (i.e., no adding or removing elements).
