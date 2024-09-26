import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = 'victor',
    host = 'localhost',
    password = 'projeto123',
    db = 'projeto_crud'
)

if conn.is_connected():
    print('conectando com o banco')
else:
    print('Não conectado com o banco')

