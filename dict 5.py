people1 = {
    'name' : 'Joao',
    'surname': 'Rabelo',
}

# print(people1.get('name'))

# name = people1.pop('name')
# print(name)
# print(people1)
people1.update({
    'name': 'novo nome',
    'age': 16,
})
# Ou

people1.update(name = 'novo nome', age = 16)
print(people1)