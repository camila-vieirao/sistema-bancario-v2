LIMITE_SAQUE = 500
QUANTIDADE_MAXIMA_SAQUE = 3
saldo = 0
extrato_bancario = ""
numero_saque = 0

MSG_OPERACOES = '''
    ######## MENU ########
        1. Depósito
        2. Saque
        3. Extrato
        4. Sair
    '''   

def menu_operacoes_bancarias(usuario):
    global saldo, extrato_bancario, numero_saque

    while True:
        print(MSG_OPERACOES)
        opcao = input("Opção => ")

        if opcao == "1": 
            deposito()
        elif opcao == "2":
            saque()
        elif opcao == "3":
            mostrar_extrato()
        elif opcao == "4":
            print("\nTchau... :)")
            break
        else: 
            print("Operação inválida.")

def deposito():
    global saldo, extrato_bancario

    valor_deposito = float(input("\nValor do Depósito: "))
    if valor_deposito <= 0:
        print("\nO valor do depósito deve ser maior que ZERO.")
    else: 
        saldo += valor_deposito
        extrato_bancario += f"Depósito: R${valor_deposito:.2f}\n"
        print("\nDepósito efetuado com sucesso!")

def saque():
    global saldo, extrato_bancario, numero_saque

    if numero_saque >= QUANTIDADE_MAXIMA_SAQUE:
        print("\nOperação bloqueada!\nLimite de saques excedido.\n")
    else:
        valor_saque = float(input("\nValor do Saque: "))
        if valor_saque > LIMITE_SAQUE:
            print("\nO valor do saque não pode exceder R$ 500,00.")
        elif valor_saque > saldo:
            print("\nO valor do saque não pode ser maior que o Saldo.")
        else:
            saldo -= valor_saque
            extrato_bancario += f"Saque: R${valor_saque:.2f}\n"
            numero_saque += 1
            print("\nSaque efetuado com sucesso!")

def mostrar_extrato():
    global extrato_bancario, saldo

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_bancario else extrato_bancario)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


