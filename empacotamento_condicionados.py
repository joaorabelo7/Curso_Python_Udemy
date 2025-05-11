
# a,b = person.values()
# print(b,a)
# (a1,a2), (b1,b2) = person.items()
# print(a1,a2)
# print(b1,b2)

# for key,value in person.items():
#     print(key,value)



person = {
    'name' :'Joao',
    'surname' : 'Rabelo',
}

person_stats = {
    'age': 16,
    'height': 1.7,
}

completed_person = {**person, **person_stats}

# print(completed_person )

def show_named_arguments(*args, **kwargs):
    for key,value in kwargs.items():
        print(key,value)

show_named_arguments(**completed_person)