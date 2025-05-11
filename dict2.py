people = {}

key = 'nome'

people[key] = 'Joao'
people['surname'] = 'Rabelo'


print(people)
print(people[key])

del people['surname']

print(people)

if people.get('surname') is None:
    print('Surname doesnt exist')
else:
    print('ur surname is',people['surname'])
