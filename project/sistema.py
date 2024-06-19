LIMITE_SAQUE = 500
QUANTIDADE_MAXIMA_SAQUE = 3

MSG_OPERACOES = '''
    ######## MENU ########
        1. Depósito
        2. Saque
        3. Extrato
        4. Sair
    '''   

def menu_operacoes_bancarias(usuario):
    saldo = 0
    extrato_bancario = ""
    numero_saque = 0

    while True:
        print(MSG_OPERACOES)
        opcao = input("Opção => ")

        if opcao == "1": 
            valor_deposito = float(input("\nValor do Depósito: "))
            saldo, extrato_bancario = deposito(valor_deposito, saldo, extrato_bancario)

        elif opcao == "2":
            if numero_saque >= QUANTIDADE_MAXIMA_SAQUE:
                print("\nOperação bloqueada!\nLimite de saques excedido.\n")
            else:
                valor_saque = float(input("\nValor do Saque: "))    
                saldo, extrato_bancario, numero_saque = saque(
                    valor_saque=valor_saque,
                    saldo=saldo,
                    numero_saque=numero_saque,
                    extrato_bancario=extrato_bancario,
                    LIMITE_SAQUE=LIMITE_SAQUE
                )

        elif opcao == "3":
            extrato_bancario = mostrar_extrato(saldo, extrato_bancario=extrato_bancario)

        elif opcao == "4":
            print("\nTchau... :)")
            break
        else: 
            print("Operação inválida.")

def deposito(valor_deposito, saldo, extrato_bancario):
    if valor_deposito <= 0:
        print("\nO valor do depósito deve ser maior que ZERO.")
    else: 
        saldo += valor_deposito
        extrato_bancario += f"Depósito: R${valor_deposito:.2f}\n"
        print("\nDepósito efetuado com sucesso!")
    return saldo, extrato_bancario

def saque(*, saldo, valor_saque, numero_saque, extrato_bancario, LIMITE_SAQUE):
    if valor_saque > LIMITE_SAQUE:
        print("\nO valor do saque não pode exceder R$ 500,00.")
    elif valor_saque > saldo:
        print("\nO valor do saque não pode ser maior que o Saldo.")
    else:
        saldo -= valor_saque
        extrato_bancario += f"Saque: R${valor_saque:.2f}\n"
        numero_saque += 1
        print("\nSaque efetuado com sucesso!")
    return saldo, extrato_bancario, numero_saque

def mostrar_extrato(saldo, *, extrato_bancario):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_bancario else extrato_bancario)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return extrato_bancario