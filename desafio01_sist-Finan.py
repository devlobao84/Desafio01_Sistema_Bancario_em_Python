tela_inicial = """

[d] Depositar grana
[s] Sacar grana
[e] Extrato completo
[q] Sair do sistema

=> """

saldo = 0
limite = 1800
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:

    opcao = input(tela_inicial)

    if opcao == "d":
        valor = float(input("Quanto pretende depositar?: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Opa! Algo de errado não está certo. O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Quanto pretende sacar?: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Tá maluco! Você não tem saldo suficiente!")

        elif excedeu_limite:
            print( "Calma a! O valor do seu saque excede o limite.")

        elif excedeu_saques:
            print("Não é possível mais sacar! Seu número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Opa, algo de errado não está certo! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO  COMPLETO ================")
        print("Sem movimentações realizadas no momento." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Por favor digite uma opção válida!")
