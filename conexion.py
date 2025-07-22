import pymysql

def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='123456l',
        db='escuela',
        cursorclass=pymysql.cursors.DictCursor
    )
