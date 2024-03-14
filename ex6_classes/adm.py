from usuario import Usuario

class Administrador(Usuario):
   def print_Usiario(self):
        print(f"{self.nome} ({self.email}) - administrador")