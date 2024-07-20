def even(x):
    if x % 2 == 0:
        return x
    else:
        raise ValueError("This number isn`t even")


try:
    print(even(5))
except ValueError as e:
    print("Error", e)


