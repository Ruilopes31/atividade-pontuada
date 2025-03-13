import os
os.system("clear")

# Exibe as opções disponíveis
print("Cores disponíveis: Verde, Azul, Amarelo, Vermelho")

# Solicita a cor ao usuário
cor =((input("Digite a cor do CD: ").lower))

# Verifica a cor e mostra o preço correspondente
if cor() == "verde":
    print("O preço do CD é R$ 10,00")
elif cor () == "azul":
    print("O preço do CD é R$ 20,00")
elif cor() == "amarelo":
    print("O preço do CD é R$ 30,00")
elif cor() == "vermelho":
    print("O preço do CD é R$ 40,00")
else:
    print("Cor inválida! Escolha entre Verde, Azul, Amarelo ou Vermelho.")
