# Importa os módulos necessários
from flask import Flask, jsonify, abort, make_response, request, json
from usuario import Usuario
from adm import Administrador

# Inicializa os objetos de exemplo para usuários e administradores
u = Usuario("jonas", "jonasdasilva@gmail.com")
a = Administrador("elias", "eliascampos@gmail.com")
u2 = Usuario("bruno", "brunodosantos@gmail.com")
users = [u, a, u2]

# Instruções para rodar o Flask no ambiente de desenvolvimento
# set FLASK_APP=main.py && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

# Inicializa a aplicação Flask
app = Flask(__name__)

# Rota raiz que retorna uma mensagem de status
@app.route("/")
def index():
    return "<h1>flask on</h1>"

# Tratamento para erros 404 (não encontrado)
@app.errorhandler(404)
def nao_encontrado(erro):
    return (jsonify(erro=str(erro)), 404)

# Tratamento para erros 400 (requisição inválida)
@app.errorhandler(400)
def nao_encontrado(erro):
    return (jsonify(erro=str(erro)), 400)

# Rota para listar todos os usuários
@app.route("/api/usuarios/")
def listar_eventos():
    users_dict = []
    for user in users:
        users_dict.append(user.__dict__)  # Converte cada objeto usuário em dicionário
    return jsonify(users_dict)

# Rota para criar um novo usuário
@app.route("/api/usuarios/", methods=["POST"])
def criar_usuario():
    data = json.loads(request.data)
    nome = data.get("nome")
    email = data.get("email")

    if not nome:
        abort(400, f"'nome' precisa ser informado!!!")

    usuario = Usuario(nome=nome, email=email)
    users.append(usuario)

    return {
        "id": usuario.id,
        "url": f"/api/usuarios/{usuario.id}/"
    }

# Função utilitária para buscar um usuário pelo ID ou retornar 404
def get_usuario_or_404(id):
    for user in users:
        if user.id == id:
            return user
    abort(404, f"usuario do id {id} não encontrado")

# Rota para detalhar informações de um usuário específico
@app.route("/api/usuarios/<int:id>/")
def detalhar_usuario(id):
    user = get_usuario_or_404(id)
    return jsonify(user.__dict__)

# Rota para deletar um usuário pelo ID
@app.route("/api/usuarios/<int:id>/", methods=["DELETE"])
def deletar_usuario(id):
    user = get_usuario_or_404(id)
    users.remove(user)
    return jsonify(id=id)

# Rota para editar completamente um usuário pelo ID
@app.route("/api/usuarios/<int:id>/", methods=["PUT"])
def editar_usuario(id):
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")

    if not nome:
        abort(400, f"'nome' precisa ser informado!!!")
    
    if not email:
        abort(400, f"'email' precisa ser informado!!!")

    user = get_usuario_or_404(id)
    user.nome = nome
    user.email = email
    
    return jsonify(user.__dict__)

# Rota para editar parcialmente um usuário pelo ID
@app.route("/api/usuarios/<int:id>/", methods=["PATCH"])
def editar_parcial_usuario(id):
    data = request.get_json()
    user = get_usuario_or_404(id)
    
    if "nome" in data.keys():
        nome = data.get("nome")
        if not nome:
            abort(400, f"'nome' precisa ser informado!!!")
        user.nome = nome

    if "email" in data.keys():
        email = data.get("email")
        if not email:
            abort(400, f"'email' precisa ser informado!!!")
        user.email = email
    
    return jsonify(user.__dict__)
