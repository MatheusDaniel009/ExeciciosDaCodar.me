from http.server import HTTPServer, BaseHTTPRequestHandler
from usuarios import Usuarios

j = Usuarios("jonas", "jonasdasilva@gmail.com", "Jomas149")
e = Usuarios("elias", "eliascampos@gmail.com", "elias088")
b = Usuarios("bruno", "brunodosantos@gmail.com", "bruno573")
user = [j, e, b]



class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/usuarios":
           self.send_response(200)
           self.send_header("Content-Type", "text/html; charset=utf-8")
           self.end_headers()
           
           user_html = ""

           for  us in user:
               user_html  += f"""
                <tr>
                    <td>{us.id}</td>
                    <td>{us.nome}</td>
                    <td>{us.email}</td>
                    <td>{us.hash_string()[0:5]}</td>
                </tr>

               """
           stylesheet  = """ 
            <style>
                table {
                    border-collapse: collapse;
                }

             td, th {
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }
            </style>


"""

           data = f"""
            <html>
    <head>{stylesheet}</head>
    <h1>Usuários</h1>
    <table>
        
        <tr>
            <th>Id</th>
            <th>Nome</th>
            <th>Email</th>
            <th>Senha</th>
        </tr>
        {user_html} 
    </table>
</html>
           """.encode()
           self.wfile.write(data)

 
server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever()