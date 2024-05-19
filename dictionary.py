# # 15April
# # dictionary are used to stored data values in key: value paor
# #they are unorderded mutable & dont allow duplicate keys
# info={
#     "key" : "value" ,
#     "name" : "apnacollege",
#     "learning" : "coding",
#     "age" : 40,
#     "is_adult" :True,
# # in the dictionary we can also stored the tuple and dctionary as well for the same
#        "subject" : ["python", "c", "java"], #list
#     "topics" : ("dict", "set", "sayali" ) # tuple
#     # like this we can stored the  key vaue pair for the same
# #key should be the float ,tuple, int ,tuple
#
# }
# print(info)
# print(type(info))
# # tuple is immutable
# # we dont reprate the value
# print(info["name"])
# print(info["subject"])
# print(info["age"])
#  # changing the value
# info["name"] = "Sayali Pathak"  #reassign the values for the same
# print(info)
#
# # key value pair separated by commas  and vice versa for the same
#
# null_dic ={}
# print(null_dic)
#
# #if-else
#
# student ={
#     "name" : "rahul kumar",
#     #
#     "subjects" : {
#         "python" : 70,
#         "chemistey" : 60,
#         "java" : 100
#
# }
# }
#
#  "teacher" :{"Sayali Pathak",
#                 "Sarthak Pathak",
#                 "Anjali Pathak"
#                 }
# }
# print(student["subjects"])
# print(student["name"])
# print(student["teacher"])

# 1. Dictionary Creation and Basics

info = {
    "key": "value",
    "name": "apnacollege",
    "learning": "coding",
    "age": 40,
    "is_adult": True,
    "subject": ["python", "C", "java"],  # List (corrected capitalization)
    "topics": ("dict", "set", "Sayali")  # Tuple
}

print(info)
print(type(info))  # Output: <class 'dict'>

# 2. Accessing Values

print(info["name"])
print(info["subject"])
print(info["age"])

# 3. Changing Values

info["name"] = "Sayali Pathak"  # Reassign the value

print(info)

# 4. Empty Dictionary

null_dic = {}
print(null_dic)  # Output: {} (empty dictionary)

# 5. Nested Dictionaries and Error Correction

student = {
    "name": "Rahul Kumar",  # Corrected capitalization
    "subjects": {
        "python": 70,
        "chemistry": 60,  # Corrected spelling
        "java": 100
    },
    "teacher": ["Sayali Pathak", "Sarthak Pathak", "Anjali Pathak"]  # List, not a set
}

print(student["subjects"])
print(student["name"])
print(student["teacher"])

# Accessing specific teacher within the teacher list:
# iF i want to print the specific type then i can click on the

print(student["subjects"]["java"])
# only java marks will be print over their
#dictionary methods
#myDict.keys()  # return all the keys for the same

#myDict.values() # returns values

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
#print(student.update(newDict)
# we can also calculate key value pair length () length is a function for the same
print(len(student))
student.update({"city": "Aud" ,"age" :60})
print(student)



#set in python set is immutable in python for the same
# set is the collection of the underderded items each element in the set must be unique &immutable
#in the set there will be the boolean,int,floa, str,tuple [list, dictionary] mutable so we cannot use in the set for the same
num={1,2,3,4,4,5}
print(type(num))

print(num)
collection ={} # this is the dictionary
print(type(collection))
collection = set()
print(type(collection))
# I am just playing with the python for the same
#set ingored the duplicaiate value for the same
#set Methods
#set is mutable changable
#set elemet is Immutable not change

collection.add(1)
collection.add(2)
print(collection)
collection.remove(1)
print(collection)
collection.add("Sayali Pathak")
print(collection)
collection.clear()
print(collection)
set2=(11,23,4,56,566)
collection.add("sayali")
collection.add("sudhir")
collection.add("Anjali")
collection.add("sarthak")
collection.pop()
print(collection)
collection.pop() # remoove the random value for the same
print(collection)
#union & interaction
print(collection.union(set2))

## Prasctice question for the same
dictionary= { "table" :["list of futurnerichires","list of a=facts and figure"] , "cat": "a small cat"}
print(type(dictionary))
print(dictionary)
subject11 ={ "python", "java","c++","c","javascript"}



# important question like a entre the value from the user and stored in into the dictionary and print it

marks ={}
x=int(input("Entre the marks of physics"))
marks.update({"phy":x})

y=int(input("Entre the marks of chemistry"))
marks.update({"chem":y})

z=int(input("Entre the marks of math"))
marks.update({"math":z})

print(marks)








