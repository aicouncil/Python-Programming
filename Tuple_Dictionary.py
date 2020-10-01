#Inbuilt Methods of Tuple....................................
'''
count() - Returns repetetion of specipic value
index() - Returns index of specific value
'''

t = (3,5,6,3,7,2)  #immutable
print(t)
print(t.count(3))
print(t.index(7))
print(len(t))
print('*****************************************************************')
#In Built Methods in Dictionary...............................
'''
clear() - Removes all value within a Dictionary
copy() - Returns a copy of dictionary
keys() - Returns Keys of Existing Dictionary
values() - Returns values of Existing Dictionary
get() - Returns value of specified key
pop() - Remove element of a specific key
popitem() - Remove the last inserted element
fromkeys() - Creates and returns a dictionary with specified key value pair
items() - Returns a list containing tuple of each key value pair
setdefault() - Returns value of specified key, insert the key with defined value
                #if it is not existing
update() - Update and exisiting dictionary with new dictionary containing key-value pair
'''
d1 = {'k1':1 , 'k2':2 , 'k3':3}
print(d1)
d2 = d1.copy()
print(d2)
print('**************************************************************')
d1.clear()
print(d1)
print(d2)
print('**************************************************************')
print(d1.keys())
print(d2.keys())
print('**************************************************************')
print(d1.values())
print(d2.values())
print('**************************************************************')
print(d2['k1'])
print(d2['k2'])
print(d2['k3'])
print('**************************************************************')
k = d2.get('k2')
print(k)
print('**************************************************************')
print(d2)
d2.pop('k3')
print(d2)
print('**************************************************************')
print(d2)
d2.popitem()
print(d2)
print('**************************************************************')
x = ('a','b','c')
y = 2
newdict = dict.fromkeys(x,y)
print(newdict)
print('**************************************************************')
print(d2)
d3 = {'k4':2 , 'k5':7 , 'k6':9}
print(d3)
d2.update(d3)
print(d2)
print('**************************************************************')
print(d2.items())
print('**************************************************************')
print(d2)
d2.setdefault('k7',89)
print(d2)
print('**************************************************************')
print(d2)
d2['k5'] = 45
print(d2)







