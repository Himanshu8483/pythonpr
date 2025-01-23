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
print(type(str1.split('s')))  # Output: ['I L', 've pyth', 'n']

# Split the string into only 1 part based on 'o'
print(str1.split('o', 1))  # Output: ['I L', 've python']

# Count how many times 'o' appears in the string
print(str1.count('o'))  # Output: 2 (there are 2 'o' in the string)

# List example
l1 = ['Himanshu',            'Kushwaha','in Python']  # List of strings

# Join the list elements with a space in between
print('$'.join(l1))  # Output: 'Himanshu Kushwaha in Python'

# Check the type of the joined result (it becomes a string)
print(type(' '.join(l1)))  # Output: <class 'str'>

# List is a collection that can store homogeneous or heterogeneous data
# Example of homogeneous list:
homogeneous_list = [1, 2, 3, 4]  # All integers
print(homogeneous_list)  # Output: [1, 2, 3, 4]

# Example of heterogeneous list:
heterogeneous_list = [1, 'Python', 3.14, True]  # Mixed data types
print(heterogeneous_list)  # Output: [1, 'Python', 3.14, True]
