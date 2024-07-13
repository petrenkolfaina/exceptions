def fun(list, el):
    if el in list:
        return el
    else:
        raise ValueError("This element is absent")
        return list
try:
    list = ["hi", 2, 0.8, 88]
    print(fun(list, 5))
except ValueError as e:
    print("Error", e)
