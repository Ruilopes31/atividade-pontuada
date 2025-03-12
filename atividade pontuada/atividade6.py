# Passo 1: Solicita ao usuário as duas notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Passo 2: Calcula a média aritmética
media = (nota1 + nota2) / 2

# Passo 3: Verifica a situação do aluno e exibe a mensagem correspondente
if media >= 6.0:
    mensagem = "Parabéns! Você foi aprovado!"
elif media >= 4.0:
    mensagem = "Você está de recuperação. Estude mais!"
else:
    mensagem = "Infelizmente, você foi reprovado."

# Passo 4: Exibe a média e a mensagem correspondente
print("Sua média é:", media)
print(mensagem)
