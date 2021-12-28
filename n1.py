def my_func (a, b):
    try:
        x = a / b
        return x
    except ZeroDivisionError:
        return "y is'n be a zero"
    except ValueError:
        return "enter only number"
print(my_func(int(input("Enter a = ")), int(input("Enter b = "))))