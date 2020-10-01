#in-built methods of list
name = ['Google' , 'Yahoo' , 'Youtube' , 'Rediff' , 'Bing']
print(name[0])
print(nasme[1])
print(name[2])
print(name[3])
print(name[4])
print('**************************************************')
#append() - used to add new value into existing list
print(name)
name.append('Hello')
print(name)
print('**************************************************')
#insert() - used to insert a new value at a defined index
print(name)
name.insert(2,'AICouncil')
print(name)
print('**************************************************')
#count() - count no. of existense
print(name.count('Google'))
print('**************************************************')
#copy() - copy existing list into new varible
engine = name.copy()
print(engine)
print('**************************************************')
#clear() - clears the values in a list
engine.clear()
print(engine)
print('**************************************************')
#index() - returns the index value of any element in a list
i = name.index('AICouncil')
print(i)
print('**************************************************')
#pop() - used to remove any value from existing list using the index
print(name)
name.pop(2)
print(name)
print('**************************************************')
#remove() - used to remove any value from existing list using the value
print(name)
name.remove('Rediff')
print(name)
print('**************************************************')
#reverse() - reverses the existing order of list
print(name)
name.reverse()
print(name)
print('**************************************************')
#extend() - Extends the esisting list with the help of newly defined list
num = [4,8,3,9,2,7]
name.extend(num)
print(name)
print('**************************************************')
#sort() - sorts the values albhabatically or in ascending order
name = ['Google' , 'Yahoo' , 'Youtube' , 'Rediff' , 'Bing']
name.sort()
num.sort()
print(name)
print(num)
print('**************************************************')
#len() , max() , min()
print(len(name))
print(len(num))
print(max(name))
print(max(num))
print(min(name))
print(min(num))
print('**************************************************')
#How to find index of maximum or minimum value in a list








