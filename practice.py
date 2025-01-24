# Functions work across different collection types but are generic (e.g., len, max, sum).
# Methods are collection-specific and often modify the collection in-place (except for immutable types like string, tuple, frozenset).
# del can delete entire collections or specific elements (if mutable).
# Syntax: 
# Functions: function(collection)
# Methods: collection.method
# `del` : del collection

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
