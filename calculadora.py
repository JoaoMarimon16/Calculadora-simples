from time import sleep
listaresult = []
print('=-'*19)
print('             CALCULADORA')
print()
print('''- Digite 2 valores numericos e depois 
podera escolher a operaçao entre eles''')
print('=-'*19)
while True:
    cont = ''
    print('_ _ _ = ?')
    print('^')
    n1 = int(input('Digite o primeiro valor: '))
    print(f'{n1} _ _ = ?')
    print('     ^')
    n2 = int(input('Digite o segundo valor: '))
    print(f'{n1} _ {n2} = ?')
    print('   ^')
    print('Digite:')
    print('''[ 1 ] - Adição, [ 2 ] - Subtração,
[ 3 ] - Multiplicação, [ 4 ] - Divisão''')
    sinal = int(input('Qual operação você quer efetuar? '))
    print('='*20)
    print('Calculando...')
    sleep(0.5)
    if sinal == 1:
        numero = f'{n1} + {n2} = {n1 + n2}'
        listaresult.append(numero)
        print(f'{n1} + {n2} = {n1 + n2}')
    elif sinal == 2:
        numero = f'{n1} - {n2} = {n1 - n2}'
        listaresult.append(numero)
        print(f'{n1} - {n2} = {n1 - n2}')
    elif sinal == 3:
        numero = f'{n1} × {n2} = {n1 * n2}'
        print(f'{n1} × {n2} = {n1 * n2}')
        listaresult.append(numero)
    elif sinal == 4:
        numero = f'{n1} ÷ {n2} = {n1 / n2}'
        print(f'{n1} ÷ {n2} = {n1 / n2}')
        listaresult.append(numero)
    print('='*20)
    cont = input('Deseja continuar? [S/N] ').upper()
    if cont == 'N':
        break
print('=-'*25)
print('HISTORICO DAS CONTAS:')
for c in range(0, len(listaresult)):
    sleep(0.7)
    print(f'- {listaresult[c]}')
print('='*30)
print('Fim do programa')
