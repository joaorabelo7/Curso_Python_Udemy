def multiplication(*args):
    total = 1
    for number in args:
        total *= number
    return total
variable1 = multiplication(1,2,3,4,5)
print(variable1)



def pair_odd(x):
    if x % 2 == 0:
        return f'{x} is Pair'
    
    return f'{x} is Odd'
print(pair_odd(48))
print(pair_odd(43))
print(pair_odd(45))
print(pair_odd(44))