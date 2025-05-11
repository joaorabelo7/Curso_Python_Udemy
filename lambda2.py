def executa(funcao,*args):
    return(funcao(*args))

print(
    executa(
      lambda x,y : x+y, 4,3)
)
duplica  = executa(
    lambda m: lambda n : n*m, 2 #iSSO N SE USA POIS DEIXA MUITO COMPLEXO
)

print(duplica(3))

print(executa(
    lambda *args : sum(args),2,3,41,24,214,2
))

