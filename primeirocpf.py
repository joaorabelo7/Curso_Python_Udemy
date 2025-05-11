import random

# Geração dos 9 primeiros dígitos aleatórios do CPF
nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

# Cálculo do primeiro dígito verificador
contador_1 = 10
soma = 0
for digito_1 in nove_digitos:
    numero_multiplicado = int(digito_1) * contador_1
    contador_1 -= 1
    soma += numero_multiplicado
soma_multiplicada = soma * 10
resto_div = soma_multiplicada % 11
digito_1 = resto_div if resto_div <= 9 else 0

# Adiciona o primeiro dígito verificador
dez_digitos = nove_digitos + str(digito_1)

# Cálculo do segundo dígito verificador
contador_2 = 11
soma = 0
for digito_2 in dez_digitos:
    numero_multiplicado = int(digito_2) * contador_2
    contador_2 -= 1
    soma += numero_multiplicado
soma_multiplicada = soma * 10
resto_div_2 = soma_multiplicada % 11
digito_2 = resto_div_2 if resto_div_2 <= 9 else 0

# Geração do CPF completo
novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

# Exibe o CPF gerado
print(f'CPF gerado: {novo_cpf}')

# Validação simplificada do CPF gerado
soma_1 = 0
for i in range(9):
    soma_1 += int(novo_cpf[i]) * (10 - i)
resto_1 = soma_1 % 11
digito_1_valido = 0 if resto_1 < 2 else 11 - resto_1

soma_2 = 0
for i in range(10):
    soma_2 += int(novo_cpf[i]) * (11 - i)
resto_2 = soma_2 % 11
digito_2_valido = 0 if resto_2 < 2 else 11 - resto_2

# Valida e imprime o resultado
if int(novo_cpf[9]) == digito_1_valido and int(novo_cpf[10]) == digito_2_valido:
    print(f"O CPF {novo_cpf} é válido")
else:
    print(f"O CPF {novo_cpf} é inválido")