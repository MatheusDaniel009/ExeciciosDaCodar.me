#1 Escreva um programa que lê números inteiros positivos do usuário, um após o
# outro, e monta uma lista a partir desses números e depois imprime a lista montada.
# O programa deve continuar solicitando por números até que o elemento digitado
# seja um número negativo (que não deve ser inserido na lista).

# n =  int(input("digite um numero: "))
# lista  = []
# while n > 0:
#     lista.append(n)
#     print (lista)
#     n =  int(input("digite um numero: "))

#2 Dada uma lista de números inteiros, escreva um programa que calcula a soma de
#todos os números na lista

# soma = [1, 10, 20, 35, 22, 12]

# quantidade = len(soma)

# l = 0
# total = 0
# while l < quantidade:
#     total = total + soma[l]
#     l += 1


# print ("a soma é:", total )

#3 Data uma lista de números inteiros, escreva um programa que calcula a média dos
#números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3
# deve imprimir apenas 12 .


# numero = [1, 10, 20, 35, 22, 12]

# quantidade = len(numero)
# l = 0
# total = 0
# while l < quantidade:
#     total = total + numero[l]
#     l += 1

# media = total / quantidade
# media = int(media)

# print("a media é:", media)

#4 Suponha o seguinte programa:
# alunos = [
# ("Alice", 8),
# ("Bob", 7),
# ("Carlos", 9),
# ]

#Escreva uma programa que calcula a média das notas de todos os alunos.

# total_notas = 0
# l = 0
# quantidade = len(alunos)

# while l < quantidade:
#     nome, nota = alunos[l]
#     total_notas = nota + total_notas
#     l += 1

# media  = total_notas / l

# print("a media das notas é:", media)

# total = 0

# for aluno in alunos:
#     nome, nota = aluno
#     total = total + nota

# media = total /  len(alunos)
# print("a media das notas é:", media)

#5 Suponha o seguinte programa:
# alunos = [
# {
# "nome": "Alice",
# "nota": 8,
# },
# {
# "nome": "Bob",
# "nota": 7,
# },
# {
# "nome": "Carlos",
# "nota": 9,
# }
# ]

# Escreva uma programa que calcula a média das notas de todos os alunos.

# total = 0
# quantidade = len(alunos)
# l = 0

# while l < quantidade:
#     nome,  nota  = alunos[l].values()
#     total = total + nota
#     l += 1

# media = total /l

# print("a media é:",media)

# total = 0
# for aluno in alunos:
#     nome, nota = aluno.values()
#     total += nota

# media = total / len(alunos)
# print("a media é:",media)


#6 Escreva um programa que dado uma lista de números inteiros, imprime
#o maior número dessa lista.

# lista = [1, 3, 2, 5]

# lista.sort(reverse = True)

# print("o maior numero  é:", lista[0])

#7 Escreva um programa que solicite uma string para o usuário e imprima quantas
#vezes cada letra aparece na palavra. Por exemplo:

# p = input("escreva uma palavra:")
# alfabeto = {

# }

# n = 0

# for l in p:
#     alfabeto[l] = 0

# for l in p:
#     alfabeto[l] += 1
  

# print (sorted(alfabeto.items()))

#8 Escreva um programa que declara uma lista com elementos de
# diferentes tipos e imprime na tela essa lista invertida. Não é permitido utilizar
# métodos como reverse ou sort .


# lista = ["a", 5, {1}]

# inverte_lista = []

# quantidade = len(lista)
# l = 0

# while l < quantidade :
#     p = lista.pop()
#     inverte_lista.append(p)
#     l +=  1

# print(inverte_lista)

    