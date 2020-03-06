# n=2
# s="consultadd"
# print(s*n)

# [1,2,3,4,5,6]--> [[1,2],[3,4],[5,6]]

def chunk(list,size):
    return [list[i:i+size] for i in range(0,len(list),size)]
y=chunk([1,2,3,4,5,6],2)
print(y)


#join

training=['java','aws','python'] 
print("My trainings are : ")
print (" ".join(training) )

#split

s="Hello"
a=s.split()
print(a)

def split(word):
    return [i for i in word]
print(split("hello"))


#merging 2 dic
# a,b
# {**a,**b}

# # 

# def get_vowels(string):
#     return [i for i in string if i not in 'aieou']
# a=get_vowels("consultadd")
# print("".join(a))


def palindrom(a):
    return a==a[::-1]
print(palindrom("mom"))

