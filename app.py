from flask import Flask, render_template, request, session,redirect, url_for,flash
from banco_de_dados import Banco
from model import Usuario

app = Flask(__name__)
app.secret_key = 'MUITO_SECRETO'
banco = Banco()

@app.route('/login')
def telaDeLogin():
        return render_template('login.html')

@app.route('/validacao', methods=['GET','POST'])
def validacao_usuario():
      if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        usuario_encontrado = banco.buscarUsuario(usuario=usuario, senha=senha)
        if usuario_encontrado:
            newUsuario = Usuario(usuario_encontrado[0], usuario_encontrado[1], usuario_encontrado[2],usuario_encontrado[3],usuario_encontrado[4],usuario_encontrado[5] )
            if usuario == newUsuario.usuario and senha == newUsuario.senha:
                session['usuario_dados'] = {
                     'usuario': newUsuario.usuario,
                     'senha': newUsuario.senha,
                     'nome': newUsuario.nome,
                     'data_nascimento': newUsuario.data_nascimento,
                     'email': newUsuario.email
                }
                return redirect(url_for('pagina_principal', nome_usuario = newUsuario.usuario))
        mensagem = 'Usuario não encontrado.'    
        return render_template('login.html', mensagem_erro=mensagem)
        
           
@app.route('/pagina_principal/<nome_usuario>')
def pagina_principal(nome_usuario):
    usuario = session.get('usuario_dados',None)
    if usuario:
        return render_template('pagina_usuario.html', nome=usuario['nome'], data_nascimento=usuario['data_nascimento'], email=usuario['email'])
    else:
         return render_template('login.html')

@app.route('/cadastrar', methods=['GET','POST'])
def cadastrar_usuario():
     if request.method == 'GET':
        return render_template('cadastrar.html')
     elif request.method == 'POST':
         nome = request.form.get('nome')
         data_nascimento = request.form.get('data_nascimento')
         email = request.form.get('email')
         usuario = request.form.get('usuario')
         senha = request.form.get('senha')
         banco.inserirUsuario(usuario,senha,nome,data_nascimento,email)
         return redirect(url_for('sucesso'))

@app.route('/sucesso')    
def sucesso():
    return render_template('cadastro_com_sucesso.html')     
     
      


            
            


if __name__ == '__main__':
    app.run(debug=True)