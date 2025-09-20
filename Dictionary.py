#dictionary in python 
#syntax 
# My_dic = {
#     "key1":"value1",
#     "key2":"value2",
#     "key3":"value3",
#     "key4":"value4",
# }
# print(My_dic)

#creating a dictionary
#normal dictionary
# biodata = {
#     "name":"nandhu",
#     "rollno":"30",
#     "branch":"csc",
#     "place":"suryapet"
# }
# print(biodata)

#dictionary using constructor
# biodata1 = dict(name = "nandhu",Roll_no = 30,Branch = "csc")
# print(biodata1)

#empty dictionary
# E_D = {}

# biodata = {
# "name":"nandhu",
# "rollno":"30",
# "branch":"csc",
# "place":"suryapet"
# }

#square brackets [] 
# print(biodata["name"])
# print(biodata["rollno"])
# print(biodata["branch"])
# print(biodata["place"])

#using get method
# print(biodata.get("name"))
# print(biodata.get("rollno"))
# print(biodata.get("branch"))
# print(biodata.get("place"))

# biodata = {
# "name":"nandhu",
# "rollno":"30",
# "branch":"csc",
# "place":"suryapet"
# }
#update
# biodata["rollno"] = 16
# biodata["name"] = "kishore"
# print(biodata)
#add
# biodata["place"]= "hyd"
# biodata["branch"]= "ai&ml"
# print(biodata)

#pop(),popitem(),clear(),del(delete)

# biodata ={
# "name":"nandhu",
# "rollno":"30",
# "blood grp":"o+",
# "branch":"csc", 
# "place":"suryapet",
# "Role":"ABCD",
# }
# print(biodata)
# #pop
# biodata.pop("blood grp")
# print(biodata) 
# #popitem
# biodata.popitem()
# print(biodata )
# biodata.popitem()
# print(biodata )
# biodata.popitem()
# print(biodata )
# biodata.popitem()
# print(biodata )
# #clear
# biodata.clear()
# print(biodata)
#del(delete)
# del biodata["place"]
# print(biodata)  

# biodata = {
#     "name":"nandhu",
#     "roll no ":30,
#     "blood grp":"o+",
#     "branch":"csc",
#     "place":"suryapet",
#     "role":"python",
# }

# #keys
# print(biodata.key())
# #update
# biodata.update({"place":"hyd","branch":"ai&ml"})
# print(biodata)
# #loops
# for i in biodata:
#     print(i)
#     for i in biodata.keys():
#         print(biodata)
        















