# Solicita ao usuário um código de operação
operacao = input("Digite a operação (+, -, *, /): ")

# Solicita os dois números inteiros
A = int(input("Digite o primeiro número inteiro: "))
B = int(input("Digite o segundo número inteiro: "))

# Verifica qual operação foi escolhida e realiza o cálculo correspondente
if operacao == '+':
    resultado = A + B
elif operacao == '-':
    resultado = A - B
elif operacao == '*':
    resultado = A * B

else:
    resultado = "Operação inválida"

# Exibe o resultado
print("Resultado:", resultado)
