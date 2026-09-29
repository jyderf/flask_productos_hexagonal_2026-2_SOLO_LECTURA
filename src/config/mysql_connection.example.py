# Copia este archivo como mysql_connection.py y completa tus datos locales.
import pymysql

# Completa aquí los mismos datos de acceso que utilizas en Workbench.
HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "CAMBIA_POR_TU_CLAVE"
DATABASE = "productosdb"


# Lo llaman los métodos de ProductRepositoryMySQL antes de ejecutar sus consultas.
# Invoca pymysql.connect() con la configuración de este archivo y devuelve la conexión.
def conectar():
    return pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5,
        autocommit=False,
    )

# Ruta de este ejemplo: src/config/mysql_connection.example.py.
# Ruta de la copia que importa la aplicación: src/config/mysql_connection.py.
# Se invoca desde product_repository_mysql.py para abrir cada conexión.
