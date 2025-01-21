# Indexing of only ordered collection (string, list, tuple) not of (set, frozenset, dict)
# syntax: 
# collection.index('obj')
# collection.index('obj', startpoint)
# collection.index('obj' start, end)
str1='python'
print(str1.index('h'))      # 3
print(str1.index('p',0, 1))     # stop/end= (n-1)
# print(str1.index('p',1))        #error:because 1st index to last index not find p 
print(str1.index('python'))     # 0
print(str1[0])      # p
print(str1[-1])     # n
print(max(str1))

l1 =[10,20,'Him',-1,'and',40]
print(l1.index('Him'))
print(l1.index(10,0))
print(l1.index('Him',1,4))
tup =(10,20,'Him',-1,'and',40)
print(tup.index('Him'))
print(tup.index(10,0))
print(tup.index('Him',1,4))

# slicing :
# Slyntax: collection[start: stop: step/ Jump/ Direction]
# stop-1 for +ve indexing
# stop+1 for -ve indexing
# Collection[start:stop]
# Rules: 
# 1. check dirction of step 
# if direction is empty by default it's one (+ve direction)
# if start and stop index same output will be empty 
# + number (+ve direction )
# - number (-ve direction )
# 2. check start / stop direction
# 3. if both direction(of step and start/stop) are matched then we get output otherwise we get empty output.
# depend on direction of step where to start if not given start point 
str1='python'
print(str1[::-1])       # nohtyp because of step direction minus start from -1 to all
print(str1[0::-1])       # p
print(str1[0::1])       # python
print(str1[::])       # python
print(str1[0:-1])       # pytho (-1-1)
print(str1[5:5])       # empty >>
print(str1[-3:5])       # ho
print(str1[5:-3])       # empty >>
print(str1[1:5:3])       # yo
print(str1[-1:0])       # pytho (-1-1)
l1=[1,2,3,4,5,6,7,8,9]
print(l1[-8:-1:2])      # [2, 4, 6, 8]

