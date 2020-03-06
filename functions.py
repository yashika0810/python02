# #with return with arguments
# def add(a,b):          #Formal parameters    #generating memory location for add
#     result=a*b
#     return result




# print(add(54,33))  #function calling--> actual parameters
#with return with no arguments
# def add():
#     print("this is second type")
#     a=int(input("enter value of a"))
#     b=int(input("enter value of b"))
#     print( a*b)
# x=add()
# print(x)

#with arguments with no return
# def add(a,b):
#     print("third type")
#     print(a+b)
# x=add(2,4)
# print(type(x))



# def is_even(l):
#     list1=[]
#     for i in l:
#         if i%2==0:
#             list1.append(i)
#     return list1
# print(is_even([1,2,3,4,5,6,7,8]))

def reverse(str1):
    new=''
    index=len(str1)
    while index>0:
        new+=str1[index-1]
        index=index-1
    return new
print(reverse("consultadd"))

#consultadd--> 8
#index=8--> 7=6
#str1[8]=d-->d-->a
#index-1=7=6
