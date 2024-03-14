#1 . Escreva uma função que recebe um número inteiro positivo e retorna True caso ele
#seja primo e False , caso contrário

# def primo(n):
#  l =  1
#  n1 = 1
#  while l != n :
#     l = l + 1
#     n1 = n % l
#     if n1 == 0:
#         break
    
#  if n1 == 0 and n == l:
#     return True
#  else:
#     return False

# print("o numero é primo?", primo(2))

#2  Implemente uma função que recebe uma lista de números inteiros e retorna uma
# tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num
# é o valor desse número.

# lista = [1000000, 20000, 409, 100]

# def grande():
#     n1 = 0
#     i = 0
#     for n in lista:
#         if n > n1:
#             n1 = n
#             i1 = i
#         i += 1
#     tu  = (i1, n1)
#     return tu

# print("o maior  numero de uma lista é:", grande())
        
#3 Implemente uma função maior_idade(pessoa) que receba uma tupla representando
# uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou
# não.

# pessoa = ("marcos", 23)

# def Maior_Idade():
#     nome,  idade = pessoa
#     if idade >= 18:
#         return print(nome,"é maior de idade")
#     else:
#         return print(nome,"é menor de idade")
    
# print(Maior_Idade())
        
#4 Adapte a função maior_idade(pessoa) de forma que ela possa receber tanto uma
#tupla quanto um dicionário. Dica: método type pode te ajudar.

# pessoa = ("marcos", 23)
# pessoa1 ={
#     "tiago": 12
# }

# def Maior_Idade(a):
#     b = type(a)
#     if b == tuple:
#         nome,  idade = a
#         if idade >= 18:
#             return print(nome,"é maior de idade")
#         else:
#             return print(nome,"é menor de idade")
#     elif b == dict:
#         c = input("digite  o nome do individo")
#         if a[c] >=  18:
#             return print(c,"é maior de idade")
#         else:
#             return print(c,"é menor de idade")
    
# print(Maior_Idade(pessoa1))   

#5  Implemente uma função que recebe dois argumentos, uma lista e um elemento , e
# retorna True caso elemento seja encontrado na lista , e False caso contrário. Não
# é permitido utilizar o método in .

# lista = [10,20,100,2]

# def tem(l,n = 0):
#     quantidade = len(l)
#     lo = 0
#     while lo < quantidade:
#         if l[lo] == n:
#             return True
#         lo += 1
#     return False

# print("o numero existe na lista:", tem(lista, 20))

#6 Implemente a função fatorial(n) de modo que ela retorne o valor do fatorial de n

# nu = int(input("digite um numero"))

# def fatorial(n):
#     if n == 0:
#         n = 1
#     l = 1
#     n1 = n
#     while l < n:
#         n1 = n1 * l
#         l += 1
        
#     return n1

# print("o fatorial de", nu, "é", fatorial(nu))



