# Programs using decorator functions or text styling programs
def my_decorator(func):
    def decorate():
        print("********************")
        func()
        print("********************")
    return decorate
def print_raw():
    print("I love you Mitu")

decorated_function = my_decorator(print_raw)
decorated_function()

@my_decorator
def print_raw():
    print("I love you tow Mitu")
print_raw()