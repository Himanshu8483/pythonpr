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
