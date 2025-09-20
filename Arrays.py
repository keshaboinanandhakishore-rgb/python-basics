#arrays in python
#importing the array module.

import array as arr 
#creting a array
numbers = arr.array('i',[1,2,3,4,5])
# print(numbers) 
# print(type(numbers))

# #adding an element
# #append():
# numbers.append(6)
# print(numbers) 
# #insert(3,7):
# numbers.insert(3,7)
# print(numbers)
# #extend([8,9])
# numbers.extend([8,9])
# print(numbers)

#deletind an elements
#remove
numbers.remove(2)
print(numbers)
#pop
numbers.pop(3)
print(numbers)
#clear
numbers.clear()
print(numbers) 