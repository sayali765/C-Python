# WAP to check if a number entred by user is odd or even
# list ,tuple, and their methods for the same

# num1=int( input("Entred a number "))
# if(num1%2==0):
#     print("The number is even ")
# else:
#     print("The entred number is odd")
#  # WAP for the greastest of 3 numbers  entred by the user
#
# num2 = int(input("Entred  the num2"))
# num3 = int(input("Entred  the num3"))
# num4 = int(input("Entred  the num4"))
# if (num2>num3 & num2>num4):
#     print("the  num1 is greater",num2)
# elif  ( num3>num4):
#     print("the num3  is greater ",num3)
# else:
#     print("the num4 is greater",num4)

# x = int (input("Entred the number by youre choice"))
# if (x % 7 ==0):
#     print("this is a multiple of  7 ")
# else:
#     print("the number is not multiple of 7 ")

#list in python

# marks = [94.4,87.4,95.2,66.4,45.1]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(len(marks))
#
# # different types together for the same
#
# student =["karan",56.7,"Aurangad"]
# print(student)
# print(type(student))
# print(len(student))
# student[0]="sayali"  # example of mutable in python for the same
# print(student)
#
# # str ="hello"
# # print(str[0])
# # str[0]="y"
# # # string is immutable measn not changes possiable
#
# #list slicling in the list
#
# student.append("Sarthak ")
# print(student)
#
# student.append(4)
# print(student)
# list =[766.,456,55,34,5,5678,543,652]
# list.sort() # print in the ascesnding order of the same
# print(list)
# list.reverse()
# # I want to print in the decendading order i can simply do the =true
# print(list.sort(reverse=True))
# print(list)
# list.insert(0 , "sayali")
# print(list)
# list.pop(0)
# print(list)
# #list [] tuple ()
# tup =()
# print(tup)
# print(type(tup))
# tup1=("Hello", 1, 2,3 ,1,1,1,)
# print(tup1)
# tup2=("Sayali", "sarthak", 1,2,3,4,5,6,)
# print(tup2)
#
# # tuple methods in python
#
# print(tup1.index(1))
# print(tup1.count(1))

# WAP to ask the user to entre names of their 3 favourotie movie & store them in a list
# movie1=input("Entre the movie name 1")
# movie2=input("Entre the movie name 2")
# movie3=input("Entre the movie name 3")
# movielist=[movie1,movie2,movie3]
# print(movielist)

# WAP to check if list  contains a palindrom of elements (Hint : use copy ()method
#[1,2,3,2,1] [1,"abc",'abc', 1]

# list11=[1,2,1]
# list12=[1,2,3]
# copy_list11=list11.copy()
# copy_list11.reverse()
#
# if (copy_list11 ==list11):
#     print("palindrom")
# else:
#     print("not palindrom")

#WAP to count number of students with The grade "A" grade in the following
t=("c","D","A","A","B","B","A")
print(t.count("A"))
t=["c","D","A","A","B","B","A"]
print(t.sort())
print(t)