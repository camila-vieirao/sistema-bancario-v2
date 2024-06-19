lista_usuarios = []
lista_contas_corrente = []
numero_conta_incremetal = 1
AGENCIA = "0001"

MENU = '''
========= BEM-VINDO! =========
Digite uma opção para começar:
    1. Criar Usuário
    2. Criar Conta Corrente
    3. Fazer Login
    4. Sair
==============================
'''
MSG_CRIAR_USUARIO = '''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Ótimo! Primeiramente, vamos precisar coletar alguns dados.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

MSG_CRIAR_CONTA_CORRENETE = '''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
     Certo! Vamos criar uma Conta Corrente para você!
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

def menu_inicio():
    while True:
        print(MENU)
        opcao = input("Opção => ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_conta_corrente()
        elif opcao == "3":
            return login_usuario()
        elif opcao == "4":
            print("Saindo... ")
            break
        else:
            print("Opção inválida. Tente novamente.")

# CRIAR USUARIO

def criar_usuario():
    print(MSG_CRIAR_USUARIO)
    print("\n========= DADOS PESSOAIS =========")
    nome = input("Nome: ").strip()
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    cpf = input("CPF: ").strip()

    if any(usuario['cpf'] == cpf for usuario in lista_usuarios):
        print("Usuário com esse CPF já cadastrado.")
        return

    print("\n============ ENDEREÇO ============")
    logradouro = input("Logradouro: ").strip()
    numero_casa = input("Número: ").strip()
    bairro = input("Bairro: ").strip()
    cidade = input("Cidade: ").strip()
    uf = input("UF: ").strip().upper()

    endereco = f"{logradouro}, {numero_casa} - {bairro} - {cidade}/{uf}"
    dados_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }

    lista_usuarios.append(dados_usuario)
    print("Usuário criado com sucesso!")
    print("Dados do Usuário:")
    for chave, valor in dados_usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print("\nLista atual de usuários:")
    for usuario in lista_usuarios:
        print(f"CPF: {usuario['cpf']} - Nome: {usuario['nome']}")

# CRIAR CONTA CORRENTE

def criar_conta_corrente():
    global numero_conta_incremetal
    print(MSG_CRIAR_CONTA_CORRENETE)

    cpf = input("Digite o CPF do usuário: ").strip()

    usuario = next((usuario for usuario in lista_usuarios if usuario['cpf'] == cpf), None)
    if usuario is None:
        print("CPF não cadastrado. Crie um usuário primeiro.")
        return

    agencia = "0001"
    numero_conta = numero_conta_incremetal

    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario['nome']
    }

    lista_contas_corrente.append(conta)
    numero_conta_incremetal += 1

    print("Conta criada com sucesso!")
    print(f"Agência: {agencia}")
    print(f"Número da Conta: {numero_conta}")
    print(f"Usuário: {usuario['nome']}")
    print("\nLista atual de contas:")
    for conta in lista_contas_corrente:
        print(f"Agência: {conta['agencia']} - Número da Conta: {conta['numero_conta']} - Usuário: {conta['usuario']}")

# FAZER LOGIN

def login_usuario():
    
    cpf = input("Digite o CPF do usuário: ").strip()

    usuario = next((usuario for usuario in lista_usuarios if usuario['cpf'] == cpf), None)
    if usuario is None:
        print("Usuário não cadastrado. Crie um usuário primeiro.")
        return
    else:
        print("Usuário autenticado!")
        return cpf
    




