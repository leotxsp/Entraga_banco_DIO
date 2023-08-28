menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[s] Sair

=>"""

Saldo = 0
limite = 500
extrato = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
    
    elif opcao == "s":
        print("Saque")

    elif opcao == "e":
        print("Extrato")
    
    elif opcao == "s":
        print("Sair")
        break
    else:
        print("Opção inválida")
        continue