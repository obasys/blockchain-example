
def unlimited_input(*args, **kwargs):
    print(args)
    for arguments in args:
        print(arguments)

    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


unlimited_input(*[1,2,3,4], name='Oleh', age=19)