#a function is a block of code that performs a specific task.
#syntax
# def greet():
#     print("hello world")
# greet()
#parametrices:
#example
# def greet(name):
#     print("hello",name)
# greet("nandhu") 

#b.keyword arguments:
# def greet(rollno,name):
#     print("hello",name, "Your rollno is",rollno)
# greet(name="nandhu",rollno="30")

#c.default arguments
# def greet(rollno,name="student"):
#     print("hello",name,"your rollno is",rollno)
# greet(rollno="30")
# greet(name="nandhu",rollno="30")

#d.variable 
# l = [10,20,30,40,50] 
# def summ(*l):
#     print(summ(l))
# sum(10,20,30,40,50)
# ex
# def data(**info):
#     for key,value in info.items():
#      print(key,":",value)
# data(name="nandhu",rollno="30",branch="csc",) 
#scope of the variable
#local variable:
#global variable
# x = 10
# print("x=10 is global")
# print("y=5 is local") 
# def test():
#    y = 5 
#    print("inside function:",x,y)
# test()
# print("outside function:",x)      

#lambda functions
# def sqe(x):
#    print(x*x)
# sqe(5)
# # lambda function for squaring a number   
# sqe = lambda x: x*x
# print(sqe(5)) #25

#recursive function
#5!=5*4*3*2*1 = 120
# def factorial():
#    fact = 1
#    for i in range(5,0,-1): 
#        fact = fact * i
#    print(fact)
# factorial()
 
# def rfactorial(n):
#     if n == 0:
#         return 1
#     else:
#          return n * rfactorial(n-1)
# print(rfactorial(5))

#map
#filter
#reduce

#map
# numbers = [1,2,3,4,5]
# squ = list(map(lambda x :x*x,numbers))
# print(squ) 

#filter
# numbers = [1,2,3,4,5]
# squ = list(filter(lambda x:x%2 == 0, numbers))
# print(squ)  

#reduce 
# from functools import reduce
# numbers = [1,2,3,4,5]
# squ = reduce(lambda x,y:x+y , numbers) 
# print(squ) 

#even or odd 
# def check(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# check(1)
# check(2)
# check(3)
# check(4)
# check(5)
# check(6)
# check(7)
# check(8)
# check(9)     
# check(10) 

#positive or negative
# def check(n):
#     if n<0:
#         print("negative")
#     elif n==0:
#         print("zero")
#     elif n>0:
#          print("positive")
# check(-3)
# check(-2)
# check(-1)
# check(3)
# check(2)
# check(1)
# check(0)   

#write a function to check the largest number amoung three numbers:
# a b c = 7 18 45
                             
