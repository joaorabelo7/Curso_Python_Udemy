def start(multiplicator):
    def multiplication(number):
        return number * multiplicator
    return multiplication

duplication = start(2)
triplication = start(3)
quadruplication = start(4)
  
print(duplication(2))
print(triplication(2))
print(quadruplication(2))