import os
os.system("clear")

# Solicita os dados do usuário
renda_mensal = float(input("Digite sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado: "))
num_prestacoes = int(input("Digite o número de prestações desejadas: "))

# Calcula o valor máximo permitido do empréstimo e da prestação
valor_maximo_emprestimo = renda_mensal * 10
prestacao_mensal = valor_emprestimo / num_prestacoes
valor_maximo_prestacao = renda_mensal * 0.3

# Verifica se o empréstimo pode ser concedido
if valor_emprestimo <= valor_maximo_emprestimo and prestacao_mensal <= valor_maximo_prestacao:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO!")
