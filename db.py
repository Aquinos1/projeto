import pymysql

def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',  # Deixe vazio se não tiver senha
        database='db_escola',
        cursorclass=pymysql.cursors.DictCursor
    )
