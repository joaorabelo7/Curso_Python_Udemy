people = {
    'name =':'joao',
    'surname =': 'rabelo',

}

people.setdefault('age', 16)

# for value in people.values():
#     print(value)

for key,value in people.items():
    print(key,value)

print(people['age'])