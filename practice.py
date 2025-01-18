# 18 Jan 
# python call by Value (not)
# python call by Reference (yes)
# python call by object reference (yes)


# python object type mutable and immutable 
# Immutable Nature  # memory address same 
# integer
10
x=10
y=10
print(id(10))
print(id(x))
print(id(y))

# string 
x="Him"
y="Him"
print(id(x),id(y))

# Tuple 
x=(10,20,30,'Him')
y=(10,20,30,'Him')
print(id(x),id(y))

# mutable Nature     # memory address different 
# list 
l1=[10,20,30,'Him']
l2=[10,20,30,'Him']
print(id(l1),id(l2))
# Dictionary 
d1={'name':'Him', 'age':37}
d2={'name':'Him', 'age':37}
print(id(d1),id(d2))
# Set
s1={10,20,30,'Him'} 
s2={10,20,30,'Him'} 
print(id(s1),id(s2))
print(s1,s2)            # order change

# frozenset 
fx=frozenset({10,20,30,'Him'})
fy=frozenset({10,20,30,'Him'})
print((fx),(fy))
print(id(fx),id(fy))      # order change & nature will be immutable but object will be mutable

# Indexing : In any Collection To fetch Address of Object
# types +ve and -ve Indexing 
# for negitive (it's not in real)
# start from -1
# write direction Left to Right
# read direction Right to Left
# stop point=end+1 
# to findout last object (from -1)

# for positive
# start from 0
# write direction Left to Right
# read direction Left to Right
# stop point = end-1
# to findout first object (from zero)

# # Syntax 
# collection.index('obj')
# collecttion.index('obj',start, stop)
