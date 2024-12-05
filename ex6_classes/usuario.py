# Módulo usuario.py

# i. Deve conter uma classe Usuario

# ii. Classe Usuario deve ter um construtor que recebe nome e email

# iii. Classe Usuario deve possuir um método de instância imprime_usuario que
# imprime: "Gabriel (gabriel@exemplo.com)", para uma instância com nome =
# "Gabriel" e email = "gabriel@exemplo.com"

# iv. Classe Usuario deve possuir um atributo de classe quantidade que
# armazena a quantidade de instâncias criadas, sejam instâncias de Usuario
# ou de qualquer classe que estenda Usuario . Por exemplo:
# Administrador(Usuario) .

class Usuario:
    quantidade = 0
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Usuario.quantidade += 1
        self.quantidade = Usuario.quantidade
    
    def print_Usiario(self):
        print(f"{self.nome} ({self.email})")

    
