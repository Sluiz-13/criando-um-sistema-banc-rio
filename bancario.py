menu = """
[d] = depositar
[s] = sacar
[e] = extrato
[q] = sair 
"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0: 
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite diário")
        elif excedeu_saques:
            print("Operação falhou! Você excedeu o limite de saques diários")
        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        else: 
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print("\n====================== EXTRATO ======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=========================================================")

    elif opcao == "q":
        break
    
    else:
        print("Opção inválida, por favor selecione novamente a opção desejada ")