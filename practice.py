# Methods :
# lower, upper, title, capitalize, swapcase,find, index,join,split, count()
str1= 'I Love python'
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.capitalize())
print(str1.swapcase())
print(str1.find('p'))       # 7
print(str1.find('x'))       # -1 if not in string
# print(str1.index('x'))      # error
print(str1.index('L'))      # 2
print(str1.split())         # ['I', 'Love', 'python'] return in list and split basis of space
print(str1.split('o'))      # ['I L', 've pyth', 'n']
print(str1.split('o', 1))      # ['I L', 've python']
l1=['Himanshu','Kushwaha','in Python']
p=print(type(' '.join(l1)) )        # Himanshu Kushwaha in Python
print(str1.count('o'))      # 2
