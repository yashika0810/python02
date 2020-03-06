# x=10
# y=30
# if x<y:
#     print("y is greater than x")
# else:
#     print("x is greater")


# x=int(input("enter value of x"))
# if x<0:
#     if x>-5:
#         print("result is greater than -5")
#     else:
#         print("result is less than -5")
# elif x==0:
#     print("result is zero")
# elif x>0 and x<30:
#     print("result is positive and less than 30")
# else:
#     print("result is greater than 30")


# while True:
#     print("enter a number but -1 will quit the loop and -2 will keep you in a loop")
#     x=int(input("enter value of x"))
#     if x==-1:
#         break
        
#     if x==-2:
#         continue
#         print("I am inside the loop")


# print("I am outside the loop")

avg=0
total=0
count=0
print("Enter the grade(-1 to quit)")
grade=int(input("Enter your grades"))
while grade!=-1:
    total=total+grade
    count=count+1
    print("Enter the grade(-1 to quit)")
    grade=int(input("Enter your grades"))
    if count==5:
        break



avg=total/count
print("avg of subjects",avg)
print("Added a new line")
    
