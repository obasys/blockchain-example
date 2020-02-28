file = open('test.txt', mode='r')
#file.write("Rest Test\n")

buffer = file.readlines()

print("Reading result:", buffer)

file.close()

print('Done')
