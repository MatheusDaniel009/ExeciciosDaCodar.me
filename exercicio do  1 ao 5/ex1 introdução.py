#1 Escreva um programa que contenha 4 variáveis e que imprima na tela o tipo de
#cada uma delas. A saída do seu programa deve ser na seguinte ordem:

p = "palavra"
i = 24
f = 6.9
b = False

print (type(p),"\n", type(i),"\n", type(f),"\n",type(b))




#2 Escreva um programa com as seguintes especificações:
# Uma variável “valor_compras” que receba um valor do tipo float, representando
# o valor total das compras.
# Uma variável “desconto” que receba um valor do tipo float, representando o
# desconto a ser aplicado sobre o valor total das compras.
# Uma variável “quantidade_itens”, que represente a quantidade de itens que
# foram comprados.
# Seu programa deve imprimir dois resultados:
# 1. O valor final das compras, considerando o desconto aplicado.
# 2. O custo médio de cada item (considerando o valor final das compras).


Valor_Compras = 100

Desconto = Valor_Compras * 0.25

Quantidade_Item = 75

Valor_Final = Valor_Compras - Desconto

Media = Valor_Final / Quantidade_Item 

print ("o valor final da compra é: " , Valor_Final , " a media do prudutos são: " , Media)