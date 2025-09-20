# #collection data types
# #list,tuple, set,dictionary
# list1 = [10,20,30,40,50]
# list2 = []

# #accesing elements in list
# #accessing elements are retriving a value stored a perticular position using index values.
# list1 = [10,20,30,40,50]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# print(list1[-1])
# print(list1[-2])
# print(list1[-3])
# print(list1[-4])
# print(list1[-5])

# kalkicast = ["prabhas","amitha b","DQ","KH","SSR","anudeep"]
# #add new role for prabhas owner
# kalkicast.append("bhramanandham")
# print(kalkicast)
# kalkicast.insert(3,"deepika p")
# print(kalkicast)
# kalkicast.extend(["RGV","vijay d"])
# print(kalkicast)
# #insert new role after kh mt 
#removing elements 
#deleting the  or values
# a = [2,4,6,8,8,10,12,14]
# print(a.count(8))
 
# #sorting: sort()
# st = [25,12,31,2,18,7,45,10,67,50,17,15,99]
#reverse = 99,15,17,50,67,10,45,7,18,2,31,12,25
# st.reverse()
# print(st)

#ao = 2,7,10,12,15,17,18,25,31,45,50,67,99
# st.sort()
#do = 99,67,50,45,31,25,18,17,15,12,10,7,2

# st = [25,12,31,2,18,7,45,10,67,50,17,15,99]
# st.sort(reverse=True)
# print(st)

# it returns the maximum number in the list It returns the minimum number in the list 
#it returns the total sum of lists.

#copying the list:
# frd1 = ["A","C","D","B","A","C","C","D","B","B","C"]
# frd2 = frd1.copy()  
# print(frd2)

# st = [25,12,31,2,18,7,45,10,67,50,17,15,99]
# print(len(st))
# #maximum: max(): 
# print(max(st))
# #minimum: min(): 
# print(min(st))
# # sum():
# print(sum(st))
# #multiple values using input data  to the list:
# b = input 

# cars = ["thar","jaguer","audi","bmw","hhh"]
#index    0       1        2     3     4
#inerating only index of list
# l=len(cars) 
# print(l)
#itering the values in the list using index :
# for i in range(0,2):
#     print(cars[i])

#adding the elements to the list using for loops:
#a = [10,20,30,40,50]
# list1 = []
# n = int(input("Enter the number of items :" ))
# for i in range(n):
#     v = int(input("enter the items:"))
#     list1.append(v)
# print(list1)

#a = 0 1 2 3 4 5 6 7 8 9 10
#i = 0 1 2 3 4 5 6 7 8 9 10
# list1 = []
# n = int(input("Enter the number of items :"))
# for i in range(1,n):
#     #v = int(input("enter the items:"))
#     list1.append(i)
# print(list1)

#sum of list item = 10 20 30 40 50 without using sum().
# a = [10,20,30,40,50]
# sum = 0
# for i in a:
#     sum = sum + i
# print(sum)

# a = [10,20,30,40,50]
# sum = 1
# for i in a:
#     sum = sum * i
# print(sum)

#convert["p","y","t","h","O","n"] to python
# n = ["p","y","t","h","O","n"]
# word = " "
# for i in n:
#     word = word + i
# print(word)

#find the maximum and minimum number from list without using max() and min()
# numbers = [59,200,8,5,219,229,227,54,68,84,58]
# max_n = numbers[0]
# min_n = numbers[0]
# for i in numbers:
#     if i > max_n:
#         max_n = i
#     if i < min_n:
#         min_n = i
# print(max_n)
# print(min_n)

# numbers = [59,200,8,5,219,229,227,54,68,84,58]
# numbers.sort()
# print(numbers)
# print(numbers[0])
# print(numbers[10])                      

# searching for an element in a list
# p_name =["krc","ktr","cbn","pspk","jagan","ysr"]
# searching_name = input("enter the name to be find:")
# found = False
# l = len(p_name)
# for i in range(l):
#      if searching_name == p_name[i]:
#          found =True

# if found:
#       print("yes")
# else:
#       print("no")


#count even and odd numbers
# num =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# even_cnt = 0
# odd_cnt = 0

# for i in range(len(num)):
#      if num[i]%2==0:
#          even_cnt+=1
#      else:
#          odd_cnt+=1
# print("number of even numbers are :",even_cnt)
# print("number of odd numbers are :",odd_cnt)


#reversing a list without reverse.
# num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# #i    0 1 2 3 4 5 6 7 8  9 10 11 12 13 14 15 16 17 18 19 
# l = len(num)
# r_list=[]
# for i in range(l-1,-1,-1):
#     r_list.append(num[i])
# print(r_list)


# removing all negative numbers using loops.
# num = [3,-6,4,-31,30,33,-33,9,25,-99,23,36,-69,69]
# positive_list = []
# for i in range(len(num)):
#     if num[i]> 0:
#         positive_list.append(num[i])
# print(positive_list)

#multiply each element with 2 in the list.
# num = [4,2,3,6,9,63,85,78,52,61,86,69,33,36,39]
# multi =int(input("enter the num to be multipilied:"))
# after_multipication = []
# for i in num: 
#     after_multipication.append(i*multi)
# print(after_multipication)




































