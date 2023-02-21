menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

-> """

saldo = 0
limite = 500
extrato = ""
numero_saqes = 0
LIMITE_SAQES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('informe o valor do deposito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operção falhou! O valor informado é inválido.')
    
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saqes >= LIMITE_SAQES

        if excedeu_saldo:
            print('Operção falhou! Saldo insuficiente.')
        
        elif excedeu_limite:
            print('Operção falhou! O valor do saque excede o limite.')
        
        elif excedeu_saques:
            print('Operação falhou! Número maximo de saques excedido.')
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saqes += 1
        
        else:
            print('Operção falhou! O valor informadoé inválido.')
                 
    
    elif opcao == 'e':
        
        print('\n===============Extrato===============')
        print('Não foram realizadas movimentaçções.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('========================================')


    elif opcao == 'q':
        break

    else:
        print('Operção inválida, por favor selecione novamente a operação desejada.')    