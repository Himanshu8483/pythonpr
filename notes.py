# PYTHON NOTES 
# C python Compiler use 
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


# Python: Call by Value vs. Call by Reference vs. Call by Object Reference

# Python does not use "Call by Value" or "Call by Reference" in the traditional sense.
# Instead, it uses "Call by Object Reference," which means:
# - If you pass a mutable object (like list, dict), modifications inside the function will affect the original object.
# - If you pass an immutable object (like int, str, tuple), modifications inside the function will not affect the original object.

# Mutable and Immutable Object Types in Python
# Immutable objects:
# Once created, their memory address (id) does not change, even if assigned to new variables.

# Integer Example:
x = 10
y = 10
print("Integer:")
print(id(10))  # Memory address of literal 10
print(id(x))   # Memory address of variable x (same as 10)
print(id(y))   # Memory address of variable y (same as 10)

# String Example:
x = "Him"
y = "Him"
print("\nString:")
print(id(x), id(y))  # Both x and y point to the same memory address since strings are immutable.

# Tuple Example:
x = (10, 20, 30, 'Him')
y = (10, 20, 30, 'Him')
print("\nTuple:")
print(id(x), id(y))  # Both x and y point to the same memory address since tuples are immutable.

# Mutable objects:
# Their memory address changes for different instances, even if the content is identical.

# List Example:
l1 = [10, 20, 30, 'Him']
l2 = [10, 20, 30, 'Him']
print("\nList:")
print(id(l1), id(l2))  # Different memory addresses because lists are mutable.

# Dictionary Example:
d1 = {'name': 'Him', 'age': 37}
d2 = {'name': 'Him', 'age': 37}
print("\nDictionary:")
print(id(d1), id(d2))  # Different memory addresses because dictionaries are mutable.

# Set Example:
s1 = {10, 20, 30, 'Him'}
s2 = {10, 20, 30, 'Him'}
print("\nSet:")
print(id(s1), id(s2))  # Different memory addresses because sets are mutable.
print(s1, s2)          # Set elements may be displayed in a different order.


The key difference between a set and a frozenset in Python lies in their mutability and usage:

# Set
# Mutable: A set can be modified after its creation (e.g., adding or removing elements).
# Unordered: The order of elements is not guaranteed, and it may change as the set is modified.
# Unique Elements: Sets only allow unique elements (no duplicates).
# Operations: You can perform operations like adding (add()), removing (remove()), and updating elements.
# Use Cases: Use sets when you need a collection of unique items that you may modify (e.g., dynamic membership testing, removing duplicates).

# Frozenset Example:
fx = frozenset({10, 20, 30, 'Him'})
fy = frozenset({10, 20, 30, 'Him'})
print("\nFrozenset:")
print(fx, fy)          # Order remains consistent, but the object is immutable.
print(id(fx), id(fy))  # Memory addresses are different even though frozensets are immutable.

# Frozenset
# Immutable: A frozenset cannot be modified after its creation.
# Unordered: Like sets, the order of elements is not guaranteed.
# Unique Elements: Frozensets also allow only unique elements.
# Operations: Since frozensets are immutable, you cannot add, remove, or modify elements. However, you can perform set operations like union, intersection, and difference.
# Use Cases: Use frozensets when you need a collection of unique items that should remain constant and hashable (e.g., keys in dictionaries or elements in other sets).

# Indexing in Collections
# Used to fetch specific elements in sequences like lists, strings, tuples.

# Positive Indexing:
# - Starts from 0.
# - Write direction: Left to Right.
# - Read direction: Left to Right.
# - Stop point: end - 1.
# - First object is accessed with index 0.

# Negative Indexing:
# - Starts from -1.
# - Write direction: Left to Right.
# - Read direction: Right to Left.
# - Stop point: end + 1.
# - Last object is accessed with index -1.

# Syntax for Indexing:
# collection.index('object')          # Finds the index of the first occurrence.
# collection.index('object', start, stop)  # Searches within a range.

# Example:
lst = [10, 20, 30, 40, 50]
print("\nIndexing Example:")
print("Positive Indexing:", lst[0], lst[1])  # Access using positive indexes.
print("Negative Indexing:", lst[-1], lst[-2])  # Access using negative indexes.

# Indexing and Slicing in Python

# Indexing: It is used to access an element from an ordered collection (string, list, tuple).
# It is not supported by unordered collections (set, frozenset, dictionary).
# Syntax for indexing:
# collection.index('obj')
# collection.index('obj', start_point)
# collection.index('obj', start, end)

# Example with a string:
str1 = 'python'
print(str1.index('h'))  # Output: 3 (index of 'h')
print(str1.index('p', 0, 1))  # Output: 0 (valid range is start to end-1)
# print(str1.index('p', 1))  # Error: 'p' is not found from index 1 to the end
print(str1.index('python'))  # Output: 0 ('python' starts at index 0 as a whole string)

# Accessing elements by index:
print(str1[0])  # Output: 'p' (first element)
print(str1[-1])  # Output: 'n' (last element using negative indexing)

# Using max() function:
print(max(str1))  # Output: 'y' (max based on ASCII value)

# Example with a list:
l1 = [10, 20, 'Him', -1, 'and', 40]
print(l1.index('Him'))  # Output: 2
print(l1.index(10, 0))  # Output: 0
print(l1.index('Him', 1, 4))  # Output: 2

# Example with a tuple:
tup = (10, 20, 'Him', -1, 'and', 40)
print(tup.index('Him'))  # Output: 2
print(tup.index(10, 0))  # Output: 0
print(tup.index('Him', 1, 4))  # Output: 2

# Slicing: Used to extract a portion of a collection.
# Syntax: collection[start:stop:step/Jump/Direction]

#  for Positive Step:
# start: Starting index (inclusive, defaults to 0 if not provided).
# stop: Ending index (exclusive, defaults to the end of the collection if not provided).
# step: The interval or direction (defaults to +1 if not provided).

#  for Negative Step:
# start: Starting index (inclusive, defaults to -1 if not provided, i.e., the last element of the collection).
# stop: Ending index (exclusive, defaults to one before the first element of the collection, i.e., -len(collection) - 1).
# step: The interval or direction (negative, must be explicitly provided, e.g., -1).
# - For a collection of length n, it means -n - 1.
# - Going one before the first means an index of -n - 1.

# Rules for slicing:
# 1. Check the direction of the step.
#    - If empty, step defaults to +1 (positive direction).
#    - If step is positive, slicing works from left to right.
#    - If step is negative, slicing works from right to left.
# 2. Check the start to stop direction:
#    - If step and start to stop directions match, slicing produces output.
#    - If they don’t match, slicing returns an empty result.

# Examples of slicing with a string:
str1 = 'python'
print(str1[::-1])  # Output: 'nohtyp' (reverse string because step is -1)
print(str1[0::-1])  # Output: 'p' (start at 0, step is -1, so only one element)
print(str1[0::1])  # Output: 'python' (start from 0, step is +1)
print(str1[::])  # Output: 'python' (default start, stop, and step)
print(str1[0:-1])  # Output: 'pytho' (stop at -1, exclusive)
print(str1[5:5])  # Output: '' (empty because start and stop are the same)
print(str1[-3:5])  # Output: 'ho' (start at -3, stop at 5, step defaults to +1)
print(str1[5:-3])  # Output: '' (empty because step direction conflicts)
print(str1[1:5:3])  # Output: 'yo' (start at 1, stop at 5, step is +3)
print(str1[-1:0])  # Output: '' (empty because step defaults to +1 but direction conflicts)

# Examples of slicing with a list:
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l1[-8:-1:2])  # Output: [2, 4, 6, 8] (start at -8, stop at -1, step is +2)

# Notes:
# - Always consider the direction of slicing (step and start/stop).
# - Positive step works left to right; negative step works right to left.
# - Stop index is exclusive.
# - If start == stop, the slice is always empty because the slicing operation doesn't include the stop index.

# Summary Table: If start and stop indices are empty, slicing works based on the step's direction:
# Parameter	Default for step > 0	Default for step < 0
# start	      0 (beginning)	         -1 (last element)
# stop	   len(collection) (end)	-len(collection) - 1
# step	          +1	                   -1

# Data Types in Python

# Numeric Types: Integer, Float, Complex
x = 10            # Integer
y = 20.           # Float (due to the decimal point)
print(type(x))    # Output: <class 'int'>
print(type(y))    # Output: <class 'float'>
print(type(x / y)) # Division always results in float -> <class 'float'>
z = x * y
print(type(z))    # Multiplication of int and float gives float -> <class 'float'>

# Complex Numbers
x = 10 + 3j       # Complex number (10 is real, 3j is imaginary)
y = 20.01 + 3j    # Another complex number
print(type(x / y)) # Output: <class 'complex'> (complex division)

# String Data Type
# Strings in Python are immutable and can use single or double quotes
x = 'Him'         # Single-quoted string
y = "ANSHU"       # Double-quoted string
print(x + y)      # String concatenation: Output -> 'HimANSHU'
print(type(x + y))# Output: <class 'str'>

# Inbuilt Functions in Python
x = 'python'      # String for demonstration
print(x)          # Output: python
# input()          # Used to take user input (commented to avoid interruption)
# print(input("Enter Name: ")) # Takes input from the user and displays it
print(type(x))    # Output: <class 'str'> (type of the variable)
print(id(x))      # Returns unique memory address of the variable
print(type('10')) # Output: <class 'str'> ('10' as string)
print(max(x))     # Finds the max character ('y' in 'python')
print(len(x))     # Finds the length of the string: Output -> 6
print(x.index('y')) # Finds the index of 'y' in 'python': Output -> 1

# Functions vs. Methods

# Functions: General-purpose and work on inputs
print(len("hello")) # Function directly called, returns length of string

# Methods: Called on objects (associated with specific data types)
x = "hello"        # String object
print(x.upper())   # Converts string to uppercase: Output -> 'HELLO'
# Note: Methods use dot (.) notation and depend on the data type

# Summary:
# 1. Functions like len(), print(), input() are called directly.
# 2. Methods like str.upper(), list.append() are called on specific objects.

# Key Data Types:
# - Numeric: int, float, complex
# - String: str (no char type; single character is also a string)
# - Collection types: list, tuple, dict, set, frozenset
# - Boolean: bool (True/False)

# Examples to explore more:
# - List: Mutable collection: [1, 2, 3]
# - Tuple: Immutable collection: (1, 2, 3)
# - Dictionary: Key-value pairs: {"key": "value"}
# - Set: Unique, unordered collection: {1, 2, 3}
# - Frozenset: Immutable set: frozenset({1, 2, 3})

# String Methods
str1 = 'I Love python'  # Sample string to apply methods

# Convert the string to lowercase
print(str1.lower())  # Output: 'i love python'

# Convert the string to uppercase
print(str1.upper())  # Output: 'I LOVE PYTHON'

# Capitalize the first letter of each word
print(str1.title())  # Output: 'I Love Python'

# Capitalize only the first letter of the string
print(str1.capitalize())  # Output: 'I love python'

# Swap uppercase to lowercase and vice versa
print(str1.swapcase())  # Output: 'i lOVE PYTHON'

# Find the index of the first occurrence of 'p'
print(str1.find('p'))  # Output: 7 (index of 'p' in the string)

# Find the index of 'x' (not found, returns -1)
print(str1.find('x'))  # Output: -1 (not found in the string)

# Find the index of the first occurrence of 'L'
print(str1.index('L'))  # Output: 2 (index of 'L')
# Uncomment the next line to test when substring is not found
# print(str1.index('x'))  # Raises ValueError (substring not found)

# Split the string into a list of words (default split on spaces)
print(str1.split())  # Output: ['I', 'Love', 'python']

# Split the string into parts based on 'o'
print(str1.split('o'))  # Output: ['I L', 've pyth', 'n']

# Split the string into only 1 part based on 'o'
print(str1.split('o', 1))  # Output: ['I L', 've python']

# Count how many times 'o' appears in the string
print(str1.count('o'))  # Output: 2 (there are 2 'o' in the string)

# List example
l1 = ['Himanshu', 'Kushwaha', 'in Python']  # List of strings

# Join the list elements with a space in between
print(' '.join(l1))  # Output: 'Himanshu Kushwaha in Python'

# Check the type of the joined result (it becomes a string)
print(type(' '.join(l1)))  # Output: <class 'str'>

# List is a collection that can store homogeneous or heterogeneous data
# Example of homogeneous list:
homogeneous_list = [1, 2, 3, 4]  # All integers
print(homogeneous_list)  # Output: [1, 2, 3, 4]

# Example of heterogeneous list:
heterogeneous_list = [1, 'Python', 3.14, True]  # Mixed data types
print(heterogeneous_list)  # Output: [1, 'Python', 3.14, True]

# Functions (e.g., len(), max(), sum()):
# Standalone utilities that work on collections or other objects.
# Called with the collection as an argument: function(collection).

# Methods (e.g., .append(), .remove(), .update()):
# Specific to a particular type of collection (e.g., list, set).
# Called directly on the collection object: collection.method().

# del Statement:
# Deletes a collection or specific elements from a collection.

# Functions
s = "hello"
print(len(s))  # Function: Length of the string => 5

# Methods
print(s.upper())  # Method: Converts to uppercase => "HELLO"
print(s.replace("h", "H"))  # Method: Replace 'h' with 'H' => "Hello"

# `del`
# Strings are immutable; you cannot delete a part of them directly.
del s  # Deletes the entire string object
# print(s)  # Raises an error because 's' is deleted

# Functions
l = [1, 2, 3]
print(len(l))  # Length of the list => 3
print(max(l))  # Maximum value => 3
print(sum(l))  # Sum of elements => 6

# Methods
l.append(4)  # Adds 4 to the end of the list
print(l)  # Output: [1, 2, 3, 4]
l.remove(2)  # Removes the first occurrence of 2
print(l)  # Output: [1, 3, 4]

# `del`
del l[0]  # Deletes the first element
print(l)  # Output: [3, 4]
del l  # Deletes the entire list

# List: An ordered, mutable collection in Python.
# It supports indexing, slicing, and can hold heterogeneous elements (e.g., int, float, str).
# Lists are represented using square brackets [] with comma-separated values.

# Example of list creation
x = [10]  # Single element list
y = [10]  # Another single element list
print(id(x), id(y))  # Different memory addresses (mutable objects have different IDs)

# Example of a heterogeneous list
my_list = [10, 1.5, 'Him']
print(my_list)  # Output: [10, 1.5, 'Him']
print(type(my_list))  # Output: <class 'list'>

# Inbuilt functions for lists
# Works for homogeneous lists (elements of the same type like all integers or floats)
l1 = [1, 3, 2.5, 11]
l2 = [10, 30, 1, 2]

print(max(l1))  # Max value: 11
print(min(l1))  # Min value: 1
print(sum(l1))  # Sum: 17.5
print(len(l1))  # Length: 4
print(id(l1), type(l2))  # Memory ID of l1 and type of l2
print(sum(l1 + l2))  # Sum of combined lists: 60.5

# Common methods of lists
# append(): Add one item to the end of the list
# sort(): Sort the list in ascending order
# extend(): Add multiple items to the end of the list
# insert(): Add one item at a specified position
# pop(): Remove and return the last item
# remove(): Remove a specific item
# reverse(): Reverse the list order
# clear(): Remove all items but keep the list object
# copy(): Create a shallow copy of the list (different memory address)
# count(): Count occurrences of an item
# index(): Find the index of the first occurrence of an item

# Example usage of methods
l3 = [11, 32]
print(id(l3))  # Memory ID of the list
print(id(l3.copy))  # Memory ID of the copy method (not a copied list, just the method)

# List operations
l4 = [10, 10.5, 'Him', 2]
x = (10, 20, 30, 40)  # Tuple
l1.append(x)  # Append tuple to the list
print(l1)  # Output: [1, 3, 2.5, 11, (10, 20, 30, 40)]

x = 10, 'Him'  # Another tuple
l1.append(x)  # Append tuple
print(l1)  # Output: [1, 3, 2.5, 11, (10, 20, 30, 40), (10, 'Him')]

x = [10, 20, 10]  # Another list
l1.append(x)  # Append list
print(l1)  # Output: [1, 3, 2.5, 11, (10, 20, 30, 40), (10, 'Him'), [10, 20, 10]]

x = 'Him'  # String
l1.extend(x)  # Extend the list by iterating through the string
print(l1)  # Output: [1, 3, 2.5, 11, (10, 20, 30, 40), (10, 'Him'), [10, 20, 10], 'H', 'i', 'm']

# Insert: Add an item at a specific position
l1.insert(0, 'Hello')  # Insert 'Hello' at the beginning
print(l1)  # Output: ['Hello', 1, 3, 2.5, 11, (10, 20, 30, 40), (10, 'Him'), [10, 20, 10], 'H', 'i', 'm']

# List: collection of elements in a single object.
# Lists are mutable, ordered collections, support indexing and slicing.
l1 = [10, 20, 11, 12.4, 1, 3]
print(l1)  # [10, 20, 11, 12.4, 1, 3]

# Reverse the list
l1.reverse()
print(l1)  # [3, 1, 12.4, 11, 20, 10]

# Sort the list in ascending order
l1.sort()
print(l1)  # [1, 3, 10, 11, 12.4, 20]

# Sort the list in descending order
l1.sort(reverse=True)
print(l1)  # [20, 12.4, 11, 10, 3, 1]

# Remove the last element
l1.pop()
print(l1)  # [20, 12.4, 11, 10, 3]

# Remove a specific element (12.4)
l1.remove(12.4)
print(l1)  # [20, 11, 10, 3]

# Clear all elements in the list
l1.clear()
print(l1)  # []

# Copy a list
l1 = [10, 20, 11, 12.4, 1, 3]
l2 = l1.copy()
print(l2)  # [10, 20, 11, 12.4, 1, 3]

# Count occurrences of an element
print(l1.count(20))  # 1

# Find the index of an element
print(l1.index(3))  # 5

# Tuple: collection of elements in a single object.
# Ordered collection, indexing and slicing supported, immutable.
# Represented with () and comma-separated elements.
t1 = (10, 20, 30, 40, 15)
print(t1)  # (10, 20, 30, 40, 15)

# Tuples are faster than lists due to immutability and require less memory.
import sys
x = ""
print(sys.getsizeof(x))  # 41
y = []
print(sys.getsizeof(y))  # 56
z = ()
print(sys.getsizeof(z))  # 40

# Built-in tuple functions
print(max(t1))  # 40
print(min(t1))  # 10
print(sum(t1))  # 115
print(len(t1))  # 5
print(id(t1))           # 1729469192432
print(type(t1))         # <class 'tuple'>

# Tuple indexing and counting
print(t1.index(30))  # 2
print(t1.count(10))  # 1
print(t1[-2])  # 40
