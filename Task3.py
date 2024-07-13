def even(x):
    if x %2 == 0:
        return x
    else:
        raise ValueError("This number isn`t even")
        return x

try:
    print(even(5))
except ValueError as e:
    print("Error", e)