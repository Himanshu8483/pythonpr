# list (ordered collection), indexing and slicing supported, mutable in nature(different memory address), represented in [] brackets with comma(,) seperated object
x=[10]
y=[10]
print(id(x),id(y))      # different id
my_list=[10, 1.5, 'Him']
print(my_list)
print(type(my_list))

# inbuilt function in python for list:
# max, min, len, sum, id, type() of homogeneous collection
l1 = [1,3,2.5,11]
l2= [10,30,1,2]
print(max(l1))      # 11
print(min(l1))      # 1
print(sum(l1))      # 17.5
print(len(l1))      # 4
print(id(l1), type(l2))    # id and list
print(sum(l1+l2))       # 60.5

# methods of list: append, sort, extend, remove, reverse, clear, pop, insert, copy, count, index
# append: add one object at last position
# sort: arrenge assending form 
# extend: add multiple objects in last position 
# insert: add one object from required position
# pop: remove one object from last position 
# remove: remove one object from required position
# reverse: to arrenge in reverse order
# clear: remove only all object from list not list remove 
# copy: create another object with same content (duplicate with different id)
#count: frequency
# index: object position 
# function(collection) and collection.method() and del collection(use to delete list)
# collection are string, list ,tuple, set, dict, frozenset 
l3=[11,32]          
print(id(l3))           # 2072921763584
print(id(l3.copy))      # 2072921354896
l4 = [10, 10.5, 'Him',2]
x=(10,20,30,40)
l1.append(x)
print(l1)           # [1, 3, 2.5, 11, (10, 20, 30, 40)]

x= 10, 'Him'
l1.append(x)
print(l1)           # [1, 3, 2.5, 11, (10, 20, 30, 40), (10, 'Him')]
x=[10,20,10]
l1.append(x)
print(l1)           # [1, 3, 2.5, 11, (10, 20, 30, 40), (10, 'Him'), [10, 20, 10]]
x= ('Him')
l1.extend(x)
print(l1)           # [1, 3, 2.5, 11, (10, 20, 30, 40), (10, 'Him'), [10, 20, 10], 'H', 'i', 'm']
# l1.insert( position, object)
l1.insert( 0, 'Hello')
print(l1)          # ['Hello', 1, 3, 2.5, 11, (10, 20, 30, 40), (10, 'Him'), [10, 20, 10], 'H', 'i', 'm']