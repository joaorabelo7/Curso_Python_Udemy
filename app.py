palavra_secreta = "perfume"
letras_acertadas = ""
tentaivas = 0
while True:
    letra_digitada = input("Digite uma letra: ")

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    tentaivas += 1


    print(palavra_formada)
    print(f'Você tem mais {20 - tentaivas} tentativas restantes')

    if tentaivas == 20:
        print(f'Você usou todas as suas tentavias')
        break

    if palavra_formada == palavra_secreta:
        print(f'PARABÉNS, VOCÊ GANHOU')
        print(f'Você usou {tentaivas} tentatvias')
        break