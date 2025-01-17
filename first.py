# Advantage of Python:
# On the basis of syntax easy to learn.
# Dynamically typed.
# large number of library supports.
# flexible with other languages.
# platform independent
# Huge number of Community supports. (Check error on Stack Overflow)

# Disadvantage of Python:
# Slow in speed as compare to compiler based. But fast as compared to interpreter because of JIT
# Run-time error due to dynamically typed language(C,C++,JAVA) 
# Not Create Web-app it self. It uses third party packages like django, flask, etc.
# Memory management weak

# print("Hello World!")
# # print(int(input("Enter First Number:")) + int(input("Enter Second Number:")))

# # print(type(input("Enter your name: ")))

# import keyword
# x= keyword.kwlist

# y = keyword.softkwlist

# # print(x)
# # print(y)

# print(len(x))
# print(len(y))

# # punctuation 
# import string
# x=string.punctuation
# print(x)
# print(len(x))          # special keyword 32


# # identifier(name)
# _y=11 # variable(container):right side
# print(_y)
# z=10
# # print(Z)
# _12=13  # correct 
# print(12)
# _12x=111      # correct 
# print(_12x)
# # x y= 10     #space not allowed
# him_8483='himanshu_kushwaha'
# print(him_8483)
# print('hello,', him_8483)
# print(id(him_8483))     #memory address
# _2h11=5
# print(id(_2h11))

# operator  =============
# Arithmatic (Maths operation)
# +, -, *, /(result in point), %(modulus), ||(floor), **(power)
# Comparision (return a boolean value 0 or 1)
# x=[10]
# y=[10]
# x=10
# y=10
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x>=y)
# print(x<y)
# print(x<=y)
# note: python is a call by object reference 
# Assignment (return a value)
# # =,+=,-=,*=,/=,%=,||=,**=
# x=5
# x=x+1
# y=11
# y%=2
# print(x, y)
# logical 
# and, or , not
# x=10
# y=20
# z=30
# print(not(x>y or y>z))
# print(not(x>y or y<z))
# print(x<y and y>z)
# print(x<y or y<z)

# # membership(in, not in)
# str1="Himanshu"     # " ": collection of characters
# print('N' in str1)      # False
# print('N' not in str1)  # True

# # identity(is, is not)
# x=10
# y=20
# print(x is y)       # False
# x=10
# y=10
# print(id(x))        # same because immutable
# print(id(y))
# print(x is y)       # True
# x=[10]
# y=[10]
# print(x is y)       #False
# print(x == y)       #True
# print(id(x))         # different because mutable []
# print(id(y))
# # difference b/w "is" and "=="
# # '==' compare value of an object, and 'is' compare address of an object

# Number System:Collection of Digits types are Binary(0 & 1 digit), Octal(0 to 7), Decimal(0 to 9), Hexadecimal(0 to 9 & 'A' to 'F')
# in built function bin(), oct(), hex()
# x= 10
# y=0b1010
# z= 0xc
# zz=0o20
# print(bin(x))
# print(oct(x))
# print(hex(x))
# print(oct(y))
# print(hex(z))
# print(hex(zz))
# bitwise operator (&(and),|(or),~(not) , ^(x-or), <<(left-shift), >>(right-shift))
# # | pipe symbol, / forward slash, \backward sllash, ~ tilt 
# x=10
# y=20
# print(x&y)
# print(x|y)
# n=10
# print(~n)       # -11 by 2's Compliement
# print(x^y)
# # print(bin(x&y))

# x=11
# y=21
# print(x<<2)     # num*(2^num of bit)
# print(x<<1)     
# print(y<<1)     
# print(x>>1)     # num/++++++++++++++++++++++(2^num of bit)
# print(y>>1)     
# print(x>>2)     # right shift
# literals (constant values)
# (types: Numeric, string, boolean, list, tuple, dict, set , frozenset)
# x=10 # here x is variable, and 10 is constant value
# 1. Numeric (integer, float, complex)
# integer (2, 4, 3, 22...)
# float (2.5, 10.5, 6.5...)
# # complex (x+yj):x is real part, yj:is imaginary part 
# x=10
# print(x)
# print(type(x))
# y=5+3j
# print(y)
# print(type(y))
# 2. String : Collection of characters
# represented in ' ' or " " (single line string) , ''' '''(multi line string)
# Rule of python PEP8 
x='''H'''
print(x)
print(type(x))
y='Hi"ma"n"shu'
z='''
*
**
***
****
'''
print(y)
print(z)