
def normal_function(func):
    print(func(10))

normal_function(lambda value: 10 + value)

def normal_function2(func, *args):
    for argument in args:
        print(func(argument))

normal_function2(lambda value: value / 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)

def normal_function3(func, *args):
    for argument in args:
        print("Result: {:^20.2f}".format(func(argument)))

normal_function3(lambda value: value / 2, 10, 15, 20, 25, 30, 35, 40, 45, 50)
