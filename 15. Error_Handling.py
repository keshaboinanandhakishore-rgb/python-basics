# types of Exceptions:
# 1.zero division error:
# 2.value error:
# 3.type error:
# 4.name error:
# 5.index error:
# 6.key error:
# 7.file not found error:

# to handel an error we use try,except.
# 1.zero division error:
# num = int(input("enter the numerator: "))
# demo = int(input("enter the denominator"))
#     divi = nume/deno
#     print(divi)
# except ZeroDivisionError:
#     print("error")
#     print("invalid") 
 
# 2.value error:
# try:
#     a = int(input("enter a value:" ))
#     print(a)
# except ValueError:
#  print("error: invalid data type g iven for the output") 

# 3.type error:
# x = "hello"
# y = 15
# print(x + y)  

# 4.name error:
# try:
#   print("x:")
# except NameError:
#  print("Variable x is not defined")
# except:
#  print("Something else went wrong")

# # 5.index error:
# x = ["apple", "banana", "cherry"]
# try:
#   print(x[5])
# except IndexError:
#   print("You are trying to access an item that does not exist!")
# except:
#   print("Something else went wrong") 

# 6.key error:
# fruit = {"name": "apple", "color": "red"}
# try:
#   print(fruit["price"])
# except KeyError:
#   print("You are trying to access a dictionary item that does not exist!")
# except:
#   print("Something else went wrong") 

# 7.file not found error:
# <?php
# if(!file_exists("welcome.txt")) {
#   die("File not found");
# } else {
#   $file=fopen("welcome.txt","r");
# }
# ?> 
# 
#    
