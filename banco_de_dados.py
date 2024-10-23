import sqlite3

#Classe responsável pelo gerenciamento do banco de dados.
class Banco:

    def __init__(self): #Método construtor da classe banco.
        self.con = sqlite3.connect('usuario.db', check_same_thread=False) #Representa a conexão criada com o banco de dados se caso o banco não existir ele será criado.
        self.cursor = self.con.cursor() #Representa o nosso cursor, responsável por executar instruções SQL

    #Este metodo retorna um usuario.
    def buscarUsuario(self, usuario, senha): #recebe dois parametros usuario e senha.
        self.cursor.execute('SELECT * FROM usuarios WHERE usuario = ? and senha = ?', (usuario,senha)) #faz a consulta no banco.
        resposta = self.cursor.fetchone() #Armazena a resposta na variavel resposta.
        return resposta #Retornando o usuario que está na variavel resposta.

    def criarBanco(self): #Está função criará nossa tabela no banco, ela será chamada apenas uma vez.
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
                            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                            usuario TEXT NOT NULL,
                            senha TEXT NOT NULL,
                            nome TEXT NOT NULL,
                            data_nascimento DATE NOT NULL,
                            email TEXT NOT NULL
                        )''')
        self.con.commit()
        self.con.close()

    def inserirUsuario(self,usuario,senha,nome,data_nascimento,email):
        self.cursor.execute('INSERT INTO usuarios (usuario,senha,nome,data_nascimento,email) values (?,?,?,?,?)',
                            (usuario,senha,nome,data_nascimento,email))
        self.con.commit()
        






if __name__ == '__main__':
    banco = Banco()
    banco.inserirUsuario()
