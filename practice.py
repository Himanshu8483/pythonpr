# Set :
# Collection of unique elements.
# unordered collection, indexing and slicing not supported. Mutable in nature, represented in {} with comma(,) seperated elements

# my_set={'HIMANSHU', 10, 20, 'Jatin',30,40, 'Yash'}
# print(my_set)       # {'Jatin', 20, 'HIMANSHU', 40, 10, 30, 'Yash'}
# print(type(my_set))     # <class 'set'>

# #  max, min type, id, len, sum 
# s1={'Himanshu', 'Yash', 'Jatin'}
# s2={10, 20, 30, 40.5, 50}
# print(max(s1), max(s2))     # Yash 50
# print(min(s1), min(s2))     # Himanshu 10
# print(type(s1), type(s2))     # 3134673869216 3134673870336
# print(id(s1), id(s2))     # Himanshu 10
# print(len(s1), len(s2))     # 3 5
# print(sum(s2))     # 150.5
# normal operations : 
# copy, clear, add, update, pop, remove, discard 
# s1.copy()       # {'Yash', 'Himanshu', 'Jatin'}
# s1.clear()       # set()
# s1.add(50)      # {50, 'Himanshu', 'Jatin', 'Yash'}       Add single element
# s2.add(50)      # {50, 20, 40.5, 10, 30}
# s2.add(50)      # {50, 20, 40.5, 10, 30}        add only one time 50 because unique elements
# print(s1)       
# print(s2)     
# l1=[2,4,6,8,10]  
# s1.update(l1)       # {2, 4, 6, 8, 10, 'Himanshu', 'Jatin', 'Yash'}     Add multiple elements
# s1.pop()          # {'Yash', 'Himanshu'} random remove element
# s2.remove(50)       # {20, 40.5, 10, 30}
# s2.remove(50)       # {20, 40.5, 10, 30}        error because again try to remove 50 but it's already removed
# s2.discard(30)      # {50, 20, 40.5, 10} remove particular element
# print(s2)  
#      
# mathematical operations: 

A={1,2,3,4,5,6}
B={3,6,7,8}
# print(A.union(B))       # {1, 2, 3, 4, 5, 6, 7, 8}
# print(A.intersection(B))    # {3, 6}
# print(A)        # {1, 2, 3, 4, 5, 6}
# print(B)        # {8, 3, 6, 7}

# A.intersection_update(B)       # Only for Target
# print(A)        # {3, 6} change the original A
# print(B)        # {8, 3, 6, 7} not change B

# Difference
# print(A.difference(B))      # {1, 2, 4, 5}
# print(A)        # {1, 2, 3, 4, 5, 6} not changed A
# A.difference_update(B)      # Only for Target
# print(A)        # {1, 2, 4, 5} changed A

# Symmetric Difference 
# print(A.symmetric_difference(B))        # {1, 2, 4, 5, 7, 8}

B.symmetric_difference_update(A)
print(A)        # {1, 2, 3, 4, 5, 6}    not changed A
print(B)        # {1, 2, 4, 5, 7, 8}    changed B
