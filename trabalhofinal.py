print('PROGRAMA ELABORADO POR BERNARDO AUGUSTO LODI, GABRIEL ARAUJO VALONI E NICOLAS ANDRADE DE CAMPOS.')
print('Olá, Bem-vindo ao Sistema de Gerenciamento de Saúde Animal da Clínica Veterinária Bixo Feliz!')
print('Insira os dados solicitados abaixo para a montagem da sua tabela: ')
print(' ')

matriz = []
doencas = ["câncer","obesidade","carrapato", "deficiência física","sarnas"]
animais = ["cachorros","gatos","hamsters","pássaros","coelhos"]
menu = '0'

def print_erro_formatacao():
    print('Houve um erro de formatação, tente novamente.\n')

def print_linha(animal, linha, tamanhos):
    linha_formatada = animal
    for i, item in enumerate(linha):
        linha_formatada += item
        comprimento = len(item)
        espaco = tamanhos[i] - comprimento
        linha_formatada += espaco * ' ' + '  '
    print(linha_formatada)

for i in animais:
    linha = []
    for j in doencas:
        while True:
            try:
                cont = int(input('Informe a quantidade de {} com {}: '.format(i,j)))
                if cont >= 0:
                    if cont < 1000000:
                        break
                    else:
                        print('O número precisa menor que um milhão. ')
                else:
                    print('O número precisa maior ou igual a zero. ')
            except:
                print_erro_formatacao()
        linha.append(str(cont))
    matriz.append(linha)
    print(' ')

animais = ["Cachorros  ","Gatos      ","Hamsters   ","Pássaros   ","Coelhos    "]
cabecalho = ["Animais  ","Câncer","Obesidade","Carrapato","Deficiência física","Sarnas"]
tamanhos = [6, 9, 9, 18, 6]

while menu != '4':
    print('Digite o número da opção que você deseja a seguir. ')
    print('1 - Para ver a tabela completa.')
    print('2 - Para pesquisar um dado específico.')
    print('3 - Para alterar algum dado.')
    print('4 - Para encerrar o programa (isso apagará os dados da tabela). ')
    menu = str(input('Opção: '))
    print(' ')

    if menu == '1':
        print("  ".join(cabecalho))
        for i, a in enumerate(animais):
            print_linha(a, matriz[i], tamanhos)
        print(' ')

    elif menu == '2':
        while True:
            print("Você deseja os dados de que animal? ")
            print('1 - Cachorros')
            print('2 - Gatos')
            print('3 - Hamsters')
            print('4 - Pássaros')
            print('5 - Coelhos')
            try:
                pesquisaA = int(input('Opção: '))
                print(' ')
                if pesquisaA == 1:
                    animal = 'cachorros'
                    break
                elif pesquisaA == 2:
                    animal = 'gatos'
                    break
                elif pesquisaA == 3:
                    animal = 'hamsters'
                    break
                elif pesquisaA == 4:
                    animal = 'pássaros'
                    break
                elif pesquisaA == 5:
                    animal = 'coelhos'
                    break
                else:
                    print('Digite um número dentre as opções.')
                    print(' ')
            except:
                print_erro_formatacao()
        while True:
            print(f"Você deseja a quantidade de {animal} com qual doença? ")
            print('1 - Câncer')
            print('2 - Obesidade')
            print('3 - Carrapato')
            print('4 - Deficiência físicas')
            print('5 - Sarnas')
            try:
                pesquisaB =  int(input('Opção: '))
                print(' ')
                if pesquisaB == 1:
                    doenca = 'câncer'
                    break
                elif pesquisaB == 2:
                    doenca = 'obesidade'
                    break
                elif pesquisaB == 3:
                    doenca = 'carrapato'
                    break
                elif pesquisaB == 4:
                    doenca = 'deficiência física'
                    break
                elif pesquisaB == 5:
                    doenca = 'sarnas'
                    break
                else:
                    print('Digite um número dentre as opções.')
                    print(' ')
            except:
                print_erro_formatacao()
        pesquisaA -= 1
        pesquisaB -= 1
        print(f'Na clínica há {matriz[pesquisaA][pesquisaB]} {animal} com {doenca}.\n')

    elif menu == '3':
        while True:
            print("Você deseja alterar os dados de que animal? ")
            print('1 - Cachorros')
            print('2 - Gatos')
            print('3 - Hamsters')
            print('4 - Pássaros')
            print('5 - Coelhos')
            try:
                pesquisaA = int(input('Opção: '))
                print(' ')
                if pesquisaA == 1:
                    animal = 'cachorros'
                    break
                elif pesquisaA == 2:
                    animal = 'gatos'
                    break
                elif pesquisaA == 3:
                    animal = 'hamsters'
                    break
                elif pesquisaA == 4:
                    animal = 'pássaros'
                    break
                elif pesquisaA == 5:
                    animal = 'coelhos'
                    break
                else:
                    print('Digite um número dentre as opções.')
                    print(' ')
            except:
                print_erro_formatacao()
        while True:
            print(f"Você deseja alterar a quantidade de {animal} com qual doença? ")
            print('1 - Câncer')
            print('2 - Obesidade')
            print('3 - Carrapato')
            print('4 - Deficiência física')
            print('5 - Sarnas')
            try:
                pesquisaB =  int(input('Opção: '))
                print(' ')
                if pesquisaB == 1:
                    doenca = 'câncer'
                    break
                elif pesquisaB == 2:
                    doenca = 'obesidade'
                    break
                elif pesquisaB == 3:
                    doenca = 'carrapato'
                    break
                elif pesquisaB == 4:
                    doenca = 'deficiência física'
                    break
                elif pesquisaB == 5:
                    doenca = 'sarnas'
                    break
                else:
                    print('Digite um número dentre as opções.')
                    print(' ')
            except:
                print_erro_formatacao()    
        pesquisaA -= 1
        pesquisaB -= 1
        while True:
            try:
                cont = int(input(f"Quantos {animal} com {doenca} há na clínica? "))
                if cont >= 0:
                    if cont < 1000000:
                        break
                    else:
                        print('O número precisa menor que um milhão. ')
                else:
                    print('O número precisa maior ou igual a zero. ')
            except:
                print_erro_formatacao()
        matriz[pesquisaA][pesquisaB] = str(cont)
        print('Dado atualizado com sucesso.\n')

    elif menu == '4':
        while True:
            confirmacao = str(input('Tem certeza de que deseja apagar os dados e encerrar o programa? (s/n) ')).lower()
            if confirmacao == 'n':
                menu = '0'
                print(' ')
                break
            elif confirmacao == 's':
                break
            else:
                print_erro_formatacao()
    else:
        print('Por favor, digite um número dentre as opções! ')
        print(' ')

print('Programa encerrado. Até a próxima! ')
