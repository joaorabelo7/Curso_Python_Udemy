import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

list = []
for x in range(3):
    for y in range(3):
        list.append((x,y))


list = [
    (x,y) 
    for x in range(3)
    for y in range(3)
]
p(list)