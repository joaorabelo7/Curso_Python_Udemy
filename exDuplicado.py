
list_of_int_numbers = [
    [1,2,3,4,5,6,7,8,9,10],
    [1,5,3,7,3,7,7,10,9,10],
    [1,3,4,4,4,6,7,8,9,10],
    [1,2,1,4,2,6,9,8,9,10],
    [1,3,3,4,5,5,4,10,9,10],
    [1,2,3,4,5,6,7,8,9,10],

]

def find_first_duplicated(int_list):
    
    check = set()
    boolean = False
    for number in int_list:
        if number in check:
            print(f'The first duplicated number is {number}')
            boolean = True
            break
        else:
            check.add(number)
    if boolean == False:
            print("Does not have any duplicated number here")
            
    print()

for list in list_of_int_numbers:
    print(list)
    find_first_duplicated(list)
