def decorator(func1):

    def inner():
        print("this is before function execution")
        x=int(input("ennter any no"))
        y=int(input("enter second value"))
        result=x+y
        print(result)

        func1()
        
    return inner

@decorator
def need():
    print("hello I need to be decorated")

# need=decorator(need)
need()
    
