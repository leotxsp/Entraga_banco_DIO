menu = """

[d] Depositar

[s] Sacar

[e] Extrato

[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
num_saques = 0
while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor do depósito: \n"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Entrada: R${deposito:.2f}\n"
        else:
            print("Valor inválido!")
    
    elif opcao == "s":
        saque = float(input("Digite o valor do saque: "))

        sem_saldo = saque > saldo

        sem_limite = saque > limite

        sem_limite_saques = num_saques == LIMITE_SAQUES

        if sem_saldo:
            print("Saldo insuficiente!")

        elif sem_limite:
            print("Voce atingiu o limite de R$500 por saque!")

        elif sem_limite_saques:
            print("Voce atingiu o limite de saques diários!")
        
        elif saque > 0:
            saldo -= saque
            extrato += f"Saida: R${saque:.2f}\n"
            num_saques += 1
        else:
            print("Valor inválido!")


    elif opcao == "e":
        print("\n<========================> Extrato <========================>\n")
        print("Não há extrato disponível." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n<=========================================================>")

    elif opcao == "q":
        break

    else:
        print("Opção inválida")
        continue