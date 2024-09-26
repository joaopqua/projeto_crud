import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = 'quaresma',
    host = 'localhost',
    password = 'projeto123',
    db = 'projeto_crud'
)

