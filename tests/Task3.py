persons = []

oleh = {'name': "Oleh", 'age': 19, 'hobbies': ["Programing", "Swimming"]}
mariia = {'name': "Mariia", 'age': 20, 'hobbies': ["Sleeping"]}
vlad = {'name': "Vlad", 'age': 21, 'hobbies': ["Sleeping"]}
kate = {'name': "Kate", 'age': 20, 'hobbies': ["Sleeping"]}


print("Task #1 - Create list of persons")
persons.append(oleh)
persons.append(mariia)
persons.append(vlad)
persons.append(kate)

print(persons)

print("Task #2 - List of names")
print([person['name'] for person in persons])

print("Task #3 - Check if all persons are older than 20")
print(all([person['age'] > 20 for person in persons]))

print("Task #4 - Safe edit first person name")

# safe_copy = persons[:]
safe_copy = [person.copy() for person in persons]
safe_copy[0]['name'] = "Test"

print(safe_copy[0])
print(persons[0])

print("Task #5 - Unpack list")
p1, p2, p3, p4 = persons

print(p1)
print(p2)
print(p3)
print(p4)