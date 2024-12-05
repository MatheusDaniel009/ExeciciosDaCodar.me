#1 Implemente o programa FizzBuzz.

# n = int(input("digite um numero: "))
# FizzBuzz = "nada"
# if  n % 3 == 0 and n % 5 == 0:
#     FizzBuzz = "Fizzbuzz"

# elif  n % 3 == 0:
#     FizzBuzz = "Fizz"
    
# elif n % 5 == 0:
#    FizzBuzz = "Buzz"

# print (FizzBuzz)

#2  Implemente uma calculadora que recebe 3 valores do usuário:

# x = float(input("digite um numero: "))
# y = float(input("digite outro numero: "))
# op = input ("escolha um operador:\n 1) soma\n 2) subtração\n 3) multipricação\n 4) divição\n")
# R = 0
# if op == "1" or op == "soma" or op == "+":
#     R = x + y
#     op = "soma"

# elif op == "2" or op == "subtração" or op == "-":
#     R = x - y
#     op = "subtração"

# elif op == "3" or op == "multipricação" or op == "*":
#     R = x * y
#     op = "multipricação"

# elif op == "4" or op == "divição" or op == "/":
#     if y == 0:
#         y = float(input("0 é invalido para a divição\n digite outro valor: "))
#     R = x / y
#     op = "divição"

# print ("o resutado da", op , "é:", R)

#3 Escreva um programa de autenticação que receba um nome de usuário e senha
#( input ) informe se

# user = "jonas"
# senha = "69"

# VerificaNome = input("digite o nome do usuario: ")
# VerificaSenha = input("digite a senha: ")

# while VerificaNome != user:
#     VerificaNome = input("usuario inegistente \ndigite um usuario valido: ")

# while VerificaSenha != senha:
#     VerificaSenha = input("senha invalida \ndigite uma senha valida: ")

# print ("autenticação foi bem-sucedida")

#4 Escreva um programa que receba um número inteiro n e imprima a soma de todos
#os números de 1 até n (inclusive n ).

# n = int(input("digite um numero: "))

# l = 0 
# n1 = 0

# while l < n:
#     l = l + 1
#     n1 = l + n1

# print ("a soma de todos os numeros ate ", n, "é:", n1)

#5 Escreva um programa que receba um número inteiro n e imprima todos os
#números pares de 1 até n (inclusive n ).


# n = int(input("digite um numero: "))

# l = 0

# while l <= n:
#     print( l )
#     l = l + 2
    

#6 Um número primo é um número que é divisível apenas por 1 e por ele mesmo.
#Escreva um programa que receba um número n e informe se esse número é primo
#ou não


# n = int(input("digite um numero: "))

# l =  1

# while l != n :
#     l = l + 1
#     n1 = n % l
#     if n1 == 0:
#         break
    
 

# if  n == l:
#     print(n, "é primo")

# else:
#     print(n, " não é primo")

# l1= 100
# n = 2
# while n != l1:

#     l =  1

#     while l != n :
#         l = l + 1
#         n1 = n % l
#         if n1 == 0:
#             break
        
#     if n1 == 0 and n == l:
#         print(n)
#     n = n + 1



# 7 Implemente o jogo “Acerte o número”
# print ("tente acerta o numero")
# n = int(input("digite um numero: "))

# l = 1

# while l != 3:
#     if n < 69:
#         print ("errou, ", l , " falha o ", n , " e menor que o numero de acerto")
#         n = int(input("digite um numero: "))
#     elif n > 69:
#         print ("errou, ", l , " falha o ", n , " e maior que o numero de acerto")
#         n = int(input("digite um numero: "))
#     else :
#         break
#     l = l + 1


# if n == 69:
#     print("parabens vc ganhou")
# else:
#     print("perdeu otario kkkkkkkll")


pessoa = [
    ("oi", 12,),
    ("cu", 69)
]
print (pessoa[0][1], pessoa[1][1])

    

