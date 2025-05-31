def calculadora():
    print("Calculadora Simples")
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite a opção (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = num1 + num2
            operacao = "soma"
        elif escolha == '2':
            resultado = num1 - num2
            operacao = "subtração"
        elif escolha == '3':
            resultado = num1 * num2
            operacao = "multiplicação"
        elif escolha == '4':
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
                return
            resultado = num1 / num2
            operacao = "divisão"

        print(f"O resultado da {operacao} é: {resultado}")

    else:
        print("Opção inválida! Execute o programa novamente e escolha uma opção correta.")

# Executar a calculadora
calculadora()
