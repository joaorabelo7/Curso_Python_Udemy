import os

compras = []

while True:
    print('Selecione uma opção')
    decisao = input('[i]inserir, [a]apagar, [l]listar :')
    if decisao == 'i':
        os.system('cls')
        add_val = input("Digite o valor que deseja adicionar: ")
        compras.append(add_val)

    elif decisao == 'a':
        os.system('cls')
        del_val_str = input('digite o indice que deseja apagar: ')
        try:
            del_val_int = int(del_val_str)
            del compras[del_val_int]
        
        except ValueError:
            print('Digite um número inteiro')
        except IndexError:
            print('Selecione in índice válido')
        except Exception:
            print('Erro desconhecido')


    elif decisao == 'l':
        os.system('cls')
        for indice, nome in enumerate(compras):
         print(indice, nome)
    
    else:
        print('Escolha uma opção válida. "i", "a" ou "l"')