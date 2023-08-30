import textwrap

def menu():
    menu = """
    \033[1;36m
    [d]\tDeposito
    [s]\tSaque
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair

    
    =>\033[0;0m"""

    return input(textwrap.dedent(menu))

def deposito(saldo,valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Entrada: \t\033[1;32mR$ {valor:.2f}\033[0;0m\n"
    else:
        print("Valor inválido!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saques >= limite_saques

    if excedeu_saldo:
        print("\n\033[1;37m Operação falhou! Você não tem saldo suficiente.\n\033[0;0m")

    elif excedeu_limite:
        print("\n\033[1;37m Operação falhou! O valor do saque excede o limite.\033[0;0m")

    elif excedeu_saques:
        print("\n\033[1;37m Operação falhou! Número máximo de saques excedido.\033[0;0m")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t\033[1;31mR$ {valor:.2f}\033[0;0m\n"
        num_saques += 1
        print("\n\033[1;37m === Saque realizado com sucesso! ===\033[0;0m")

    else:
        print("\n\033[1;37m Operação falhou! O valor informado é inválido. \033[0;0m")

    return saldo, extrato, num_saques

def mostra_extrato(saldo, /, *, extrato):
    print("\n\033[1;37m<========================>Extrato<========================>\n\033[0;0m")
    print("Extrato indisponível." if not extrato else extrato)
    print(f'\033[1;37mSaldo: \t\tR$ {saldo:.2f}\033[0;0m')
    print("\n\n\033[1;37m<=========================================================>\033[0;0m")

    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário (Apenas números!): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Um usuário já existe neste cpf!")
        return
    

    else:
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento do usuário(dd-mm-aaaa): ")
        endereco = input("Digite o endereço do usuário(logradouro, nro - bairro - cidade/sigla estado): ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Digite o CPF do usuário (Apenas números!): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": num_conta, "usuario": usuario}
    
    else:
        print("Usuário não encontrado!, não foi possível criar a conta!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Num_conta:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("="*100)
        print(textwrap.dedent(linha))

def main():
    agenda = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    LIMITE_SAQUES = 3
    num_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor do \033[1;32mdepósito\033[0;0m: \n"))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor do \033[1;31msaque\033[0;0m: "))
            saldo, extrato, num_saques = sacar(
                saldo = saldo,
                valor = valor, 
                extrato = extrato, 
                limite = limite, 
                num_saques = num_saques, 
                limite_saques=LIMITE_SAQUES)
        elif opcao == "e":
            mostra_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            num_conta = len(contas) + 1
            conta = criar_conta(agenda, num_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção inválida!")

main()