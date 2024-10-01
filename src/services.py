from conexao import *

def enviar_dados(nome, email, senha):
    criar_ususario(nome, email, senha)


def criar_ususario(nome, email, senha):
    if conn.is_connected():
        print('Banc conectado com sucesso!')
        cursor = conn.cursor()

        sql = 'INSERT INTO usuario(nome, email, senha)values(%s, %s, %s)'
        values = (nome,email, senha)

        cursor.execute(sql, values)
        conn.commit()
        conn.close()
        cursor.close() 
    
    
    
    
    
    
    else:
        print('Falha ao conectar ao banco!')

        