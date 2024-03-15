import hashlib
class Usuarios():
    id  = 1
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.id = Usuarios.id
        Usuarios.id += 1
    
    def hash_string(self):
      return  hashlib.sha256(self.senha.encode()).hexdigest() 

        


    
