# Dict: Collection of key-value(elements) pairs.
# Indexing and slicing not supported 
# key must be a unique and value may be a duplicate.
# mutable in nature, represented in {} with comma(,) seperated elements.
# sequential collection
# syntax: d1={'key1':'value','key2':'value','key3':'value'}
# in-built function for dict:
d1={'name':'Him', 'age':22,'quali':'B.Tech'}  
# print(d1)       # {'name': 'Him', 'age': 22, 'quali': 'B.Tech'}
# print(max(d1)) # in bases of real dictionary keys
# print(min(d1))
# print(len(d1))      # 3
# print(type(d1))     # <class 'dict'>
# print(id(d1))       # 2517969919616

# in-built methods 
# d1.clear()
# print(d1)       # {}
# d2= d1.copy ()
# print(d2)       # {'name': 'Him', 'age': 22, 'quali': 'B.Tech'}

# l1=['name', 'email', 'contact']
# d2=dict.fromkeys(l1) # to create dictionary 

# print(d2)       # {'name': None, 'email': None, 'contact': None}
# d3= dict.fromkeys(l1, 100)
# print(d3)       # {'name': 100, 'email': 100, 'contact': 100}
# print(d1['name'])       # Him       why this failed for web develop?
# # d1.get() :print(d1.get('key'))
# print(d1.get('name'))       # Him
# d1.item()
# print(d1.items())       # dict_items([('name', 'Him'), ('age', 22), ('quali', 'B.Tech')])
# # d1.values ()
# print(d1.values())      # dict_values(['Him', 22, 'B.Tech'])
# # d1.key ()
# print(d1.keys())        # dict_keys(['name', 'age', 'quali'])
# # d1.pop()
# print(d1.pop('name'))       # Him (name removed)
# print(d1)       # {'age': 22, 'quali': 'B.Tech'}

# # d1.popitem ()     
# print(d1.popitem())     # ('quali', 'B.Tech')
# print(d1)           # after popitem: {'name': 'Him', 'age': 22}
# d1.setdefault()
# d1.setdefault('place','Rewa')       # because of attribute we use comma(,)
# print(d1)
# d1.update ()
d2={'course': 'FSD'}
d1.update(d2)
print(d1)       # {'name': 'Him', 'age': 22, 'quali': 'B.Tech', 'course': 'FSD'}
