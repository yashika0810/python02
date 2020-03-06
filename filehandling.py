# with open('data.txt','r') as file:
#     data=file.readline()
#     for i in data:
#         word=i.split()
#         print(word)

# try:
        
#     filehanlder=open('test.txt','r')
#     content=filehanlder.read()
#     print(content)

# except:
#     print("Enter the correct name of the file")

# finally:
#     filehanlder.close()


# from sys import argv



# nameofprogram , filename = argv
# print("Name of program is",nameofprogram)
# print("Nmae of file is", filename)

# while True:

#     try:
    
#         fh=open(filename,'r')
#         content=fh.read()
#         print(content)
#         fh.close()
#         break
#     except:
#         print("The name entered is wrong, please provide the correct name")
#         try_again=input("Do you want to try again? Press Y for yes or N for no (Y/N)")

#         if try_again=='Y':
#             filename = input("Please enter the name correctly this time")
#         else:
#             break


# import csv
# with open('testing.csv','r') as  csvfile:
#     result=csv.reader(csvfile)
#     for i in result:
#         print(i)


x==1,2