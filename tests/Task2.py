names = ['John', 'Luke', 'Austin', 'Jummy']

def get_names_lenght():
    for name in names:
        if len(name) > 5:
            print("Name consists of more that 5 letter")

        if ("N" or "n") in name:
            print("Name contains N letter")

        print(name , "lenght is" , len(name))
    else:
        print("-" * 20)


def clean_names_array():
    while len(names) > 0:
        print("Pop" , names.pop() , "from array")

get_names_lenght()
clean_names_array()