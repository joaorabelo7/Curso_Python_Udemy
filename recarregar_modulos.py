import importlib




import recarregar_mofulos_m

print(recarregar_mofulos_m.variavel )

for i in range(10):
    print(i)
    importlib.reload( recarregar_mofulos_m) 

print("fim")