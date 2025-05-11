import copy

from dados import produtos



novos_produtos = [
    {**p, "preco": round(p['preco']* 1.1,2)}
    for p in copy.deepcopy(produtos)
]

# print(*produtos, sep="\n")
# print()
# print(*novos_produtos, sep= "\n")



produtos_ordernados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['nome'],
    reverse= True
)

# print(*produtos, sep="\n")
# print()
# print(*produtos_ordernados_por_nome, sep= "\n")


produtos_ordernados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['preco'],
)

print(*produtos, sep="\n")
print()
print(*novos_produtos, sep= "\n")  #Saída dos produtos com o valor aumentado em 10 por cento
print()
print(*produtos_ordernados_por_nome, sep= "\n") #Saída dos produtos ordenados por nome em ordem decrescente
print()
print(*produtos_ordernados_por_preco, sep= "\n")#Saída dos produtos ordenados por preço em ordem crescente
print()
