def fun(mylist, el):
    if el in mylist:
        list.remove(mylist, el)
        return mylist
    else:
        raise ValueError("This element is absent")


try:
    mylist = [15, 8, 6, "Hello"]
    print(fun(mylist, 0))
except ValueError as e:
    print("Error", e)
