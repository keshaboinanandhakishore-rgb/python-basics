#sets in python 
#syntax:
#my_set = {elem1,elem2,elem3}

#characteristics of sets:
#unordered:
#example: {1,2,3} and{1,2,3} are considered the same set.
# s1 = {3,86,68,69,36,96,33}
# s2 = {3,6,9,36,69,93,63}
# print(s1 == s2)
# print(s2)

#unindexed: you cannot access set elements by the index like lists or tuples.
#a = {1,2,3,4}
#print(a[2])

#duplicate values:
# s1 = {1,1,2,3,3,5,1,4,2,2,5}
# print(s1) 

#creating a set:

# s1 = {10,20,30,40,50}
# s2 = {10,10.2,"hello",True} #mixed data type 

#empty set 
# e = {}
# es = set()
# print(es)
# print(type(es)) 

#assessing sets:
#we cannot directly access an element using index but we can assess an element using loops:
# roles = {"deva","simon","dayal","kali","dheya"}
# for i in roles :
#     print(i) 

#adding an element in sets:
# a = {12,34,67,70}
# a.add(32)
# print(a) # output:{32, 34, 67,70, 12}

#update():
# a = {12,34,67,70}
# a.update([78,98])
# print(a)

#Deleting the elements in sets():
# A = {12,12,78,25,52,95,44} 
# A.remove(12)  
#print(A)

# A.discard(6)
# print(A)

#clear
# A.clear()
# print(A)
 
#pop():
# A.pop
# print(A)

#mathematical operations in set:
#union "U"
#intersection 
#difference
#symmetric difference

# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}
# #union "U"
# print(a.union(b))
# #intersection "∩"
# print(a.intersection(b))
# #difference 
# print(a.difference(b))
# #symmetric difference (a u n)-(a ∩ b)
# print(a.symmetric_difference(b)) 
# print(a-b)
# print(b-a)
# print(a^b) 

# length , max,min,sum
# n = {1,2,3,4,5,6}
# # length
# print(len(n))
# #max
# print(max(n))
# #min
# print(min(n))
# #sum   
# print(sum(n)) 

#sort
#reverse
#count

a = {1,2,3,4,5,67,89,99}                                           
# a.count
# a.reverse
print(a.count(5))
          





