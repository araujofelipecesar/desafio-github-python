numero1 = int(input("Digite o primeiro número: "))

numero2 = int(input("Digite o segundo número: "))

operacao = input("Digita a operação que deseja realizar (+, -, *, / ): ")

if operacao == '+':
    print(numero1 + numero2)
elif operacao == '-':
    print(abs(numero1 - numero2))
elif operacao == '*':
    print(numero1 * numero2)
elif operacao == '/':
    print(numero1 / numero2)
else:
    print("operação inválida")