import os
os.system("clear")


print(""""

====================== FORMA DE PAGAMENTO ==================================
\t       \t\tAté 5kg \t\tAcima de 5kg
1.morango    \t\tR$ 2,50  \t\tR$ 2,50
2.maçã      \t\tR$ 1,80  \t\tR$ 1,50
""")


#solicitar dados

quantidade_de_morango = int(input("digite a quantidade de morango(em kg):"))
quantidade_de_maca= int(input("digite a quantidade de maçã(em kg):"))

if quantidade_de_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango= 2.50

#preço maçã
if quantidade_de_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

#calcular valor total
valor_maca = quantidade_de_maca * preco_maca
valor_morango = quantidade_de_morango* preco_morango
valor_total = valor_maca+ valor_morango

#desconto
if quantidade_de_morango + quantidade_de_maca > 8 or valor_total > 50:
    valor_total *= 0.90

print(f"valor a pagar:R$ {valor_total: .2f}")

