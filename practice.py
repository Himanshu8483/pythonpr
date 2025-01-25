# l1=[10,20,11,12.4, 1,3]
# l1.reverse()
# print(l1)           # [3, 1, 12.4, 11, 20, 10]
# (l1.sort())
# print(l1)           # [1, 3, 10, 11, 12.4, 20]

# l1.sort(reverse=True)
# print(l1)           # [20, 12.4, 11, 10, 3, 1]
# l1.pop()
# print(l1)           # [10, 20, 11, 12.4, 1]

# l1.remove(12.4)
# print(l1)           # [10, 20, 11, 1, 3]

# l1.clear()
# print(l1)           # []
# print(id(l1))           # 1789499564416
# del l1          # delete object: it is the python object not only for list
# print(l1)           # NameError: name 'l1' is not defined

# l2=l1.copy()
# print(l2)       # [10, 20, 11, 12.4, 1, 3]
# print(l1)       # [10, 20, 11, 12.4, 1, 3]
# print(id(l1))       # 2095118442880
# print(id(l2))         # 2095118591168

# print(l1.count(20))         # 1

# print(l1.index(3))          # 5
# print(l1[0])            # 10 : index value return

# tuple: collection of elements in single object.
# ordered collection, indexing supported, slicing supported, immutable in nature, represent in () with comma(,) seperated elements.
# tuple is faster as compare to list (due to immutable nature as well as lessrequired space for creation)
# import sys
# x=""
# print(sys.getsizeof(x))         # 41
# y=[]
# print(sys.getsizeof(y))           # 56
# z=()
# print(sys.getsizeof(z))         # 40

t1= (10,20,30,40,15)
# print(t1)           # (10, 20, 30, 40, 15)

# in built function for tuple 
print(max(t1))              # 40
print(min(t1))          # 10
print(sum(t1))          # 115
print(len(t1))          # 5
print(id(t1))           # 1729469192432
print(type(t1))         # <class 'tuple'>

print(t1.index(30))         # 2
print(t1.count(10))         # 1
print(t1[-2])          # 40 : index value