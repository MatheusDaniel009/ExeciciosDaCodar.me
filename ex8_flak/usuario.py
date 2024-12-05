
# Define a classe Usuario para representar usuários do sistema
class Usuario:
    id = 1  # Atributo de classe para controle incremental de IDs

    def __init__(self, nome, email):
        self.nome = nome  # Nome do usuário
        self.email = email  # Email do usuário
        self.id = Usuario.id  # Define o ID único do usuário
        Usuario.id += 1  # Incrementa o ID da classe para o próximo usuário

    # Método para imprimir as informações do usuário
    def print_Usiario(self):
        print(f"{self.nome} ({self.email})")

