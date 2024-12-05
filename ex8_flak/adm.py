# Importa a classe Usuario para herança
from usuario import Usuario

# Define a classe Administrador como uma subclasse de Usuario
class Administrador(Usuario):
    # Método para imprimir informações do administrador
    def print_Usiario(self):
        print(f"{self.nome} ({self.email}) - administrador")
