def fun(mylist, el):
    if el in mylist:
        return el
    else:
        raise ValueError("This element is absent")


try:
    mylist = ["hi", 2, 0.8, 88]
    print(fun(mylist, 5))
except ValueError as e:
    print("Error", e)
