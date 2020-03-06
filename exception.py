while True:
    try:

        x=int(input("enter first no"))
        y=int(input("enter second no"))
        avg=(x+y)/2
       

    except NameError:
        print("please provide correct value")

    except ValueError:
        print("provide correct integer")

    else:
        print("the average is",avg)
    