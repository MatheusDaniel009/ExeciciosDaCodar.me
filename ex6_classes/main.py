from usuario import Usuario
from adm import Administrador

u = Usuario("jonas", "jonasdasilva@gmail.com")
a = Administrador("elias", "eliascampos@gmail.com")

u.print_Usiario()
a.print_Usiario()
print(Usuario.quantidade)
print(u.quantidade)
print(a.quantidade)