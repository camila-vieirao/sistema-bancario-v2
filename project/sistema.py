LIMITE_SAQUE = 500
QUANTIDADE_MAXIMA_SAQUE = 3
saldo = 0
extrato = ""
numero_saque = 0

MENU = '''\n
    ### MENU ###
    1. Deposito
    2. Saque
    3. Extrato
    4. sair

'''    
while (True): 
    print(MENU)
    opcao = input("Opcao => ")

    # DEPOSITO

    if (opcao == "1"): 
        valor_deposito = float(input("\nValor do Deposito: "))
        if (valor_deposito <= 0):
            print("\nO valor do deposito deve ser maior que ZERO")
        else: 
            saldo += valor_deposito
            extrato += f"Deposito: R${valor_deposito:.2f}\n"
            print("\nDeposito efetuado com sucesso!")

    # SAQUE

    elif (opcao == "2"):
        if (numero_saque > QUANTIDADE_MAXIMA_SAQUE):
            print("\nOperação bloqueada!\nLimite de saques excedido\n")
        else: valor_saque = float(input("\nValor do Saque: "))

        if (valor_saque > LIMITE_SAQUE):
            print("\nO valor do saque nao pode exceder R$ 500,00.")
        elif (valor_saque > saldo):
            print("\nO valor do saque não pode ser maior que o Saldo.")
        else:
            saldo -= valor_saque
            extrato += f"Saque: R${valor_saque:.2f}\n"
            numero_saque += 1
            print("\nSaque efetuado com sucesso!")

    # EXTRATO

    elif (opcao == "3"):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # SAIR

    elif (opcao == "4"):
        print("\nTchau... :)")
        break

    # OUTRA OPCAO

    else: 
        print("Operação invalida.")