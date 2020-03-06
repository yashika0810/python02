# # x=[12,23,4,5,6]
# # for i in x:
# #     print("list elements:", i)
# # print("the list has" , len(x), "elements")

# x=[12,23,4,5,6]

# # range(len(x))--> len(x)--> range(5)
# for i in range(len(x)):
#     x[i]=x[i]**2
# print(x)

# sum=0
# for val in range(1,6):
#     sum=sum+val
# print(sum)



# # {1:1,2:4,3:9,4:16,5:25}
# x=int(input("enter a number"))
# d=dict()
# for i in range(1,x+1):
#     d[i]=i*i
# print(d)



# # s='consultadd7843'

# s=input("enter any sentence")
# d={'DIGITS':0,'LETTERS':0}
# for i in s:
#     if i.isdigit():
#         d['DIGITS']+=1
#     elif i.isalpha():
#         d['LETTERS']+=1
#     else:
#         pass
# print(' No of LETTER',d["LETTERS"])
# print('No of DIGITS', d["DIGITS"])



# x=[1,5,7]
# for elements in x:
#     if elements%2==0:
#         print("List contain an even no")
#         break

#  #the else block will execute when my loop is NOT terminated by a break statement       
# else:
#     print("list does not contain even no")

# for i in range(1,10):
#     if(i%11==0):
#         break
#     print(i)
# else:
#     print("not printed")
    

# numbers=[1,2,3,4,5,6,8]
# new_list=[]
# for i in numbers:
#     if i%2==0:
#         new_list.append(i)
# print(new_list)


my_list=[]
for i in [20,30,60]:
    for j in [2,4,6]:
        my_list.append(i*j)
print(my_list)
