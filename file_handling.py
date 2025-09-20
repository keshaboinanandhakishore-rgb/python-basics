# file handling:
# open()

# file = open("students.txt","w")           #w = write
# file.write("hello nandha kishore\n")
# line = ["nandha kishore\n","nandhu\n","keshaboina\n"]
# file.writelines(line) 
# print("data is changed")
# file.close()            

# file = open("students.txt","r") 
# print(file.read())
# print(file.readline())         
# print(file.readline())
# print(file.readline()) 
# print(file.readlines())  
# print("data is changed")
# file.close()                        

file = open("students.txt","r") 
for line in file:
    print(line)
print("data is changed")
file.close()
import numpy as np
with open("studens.txt","r") as file1: 
    for line in file1:
        print(line)
    print("data is changed")       

   
 

 
