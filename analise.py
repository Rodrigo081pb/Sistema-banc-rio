def mostrar_menu():
    print("Menu de Operação")
    print("[A] Mostrar Saldo")
    print("[B] Efetuar Depósito")
    print("[C] Efetuar Saque")
    print("[D] Finalizar")
    return input("Digite sua opção: ")


encerrar_programa = False
saldo = 0

while not encerrar_programa:
    opcao_selecionada = mostrar_menu()

    if opcao_selecionada == "A":
        print("Seu saldo é:", saldo)
    elif opcao_selecionada == "B":
        valor = int(input("Digite o valor a depositar: "))
        saldo += valor
        print("Depósito efetuado com sucesso")
    elif opcao_selecionada == "C":
        valor = int(input("Digite o valor a retirar: "))
        if valor > saldo:
            print("Saque não permitido. Você está sem dinheiro.")
        else:
            saldo -= valor
            print("Saque efetuado")
    elif opcao_selecionada == "D":
        encerrar_programa = True
    else:
        print("Opção inválida, tente novamente")
