from src.config.mysql_connection import conectar
from src.application.ports.product_repository import ProductRepository


class ProductRepositoryMySQL(ProductRepository):
    # Hereda de ProductRepository, definido en src/application/ports/product_repository.py.
    # Los paréntesis indican la clase padre; no envían datos a un constructor.
    # Cada método de abajo cumple el contrato del padre y escribe el SQL concreto.
    # ProductService llama estos métodos del hijo; no ejecuta los cuerpos del padre.
    @staticmethod
    # Lo llama ProductService.listar() usando el parámetro repositorio.
    # Abre la conexión con conectar() de src/config/mysql_connection.py y ejecuta SELECT; devuelve data.
    def listar():
        # Al salir del bloque with, la conexión se cierra automáticamente.
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id, name, price, description FROM products ORDER BY id")
                # DictCursor ya entrega cada fila como un diccionario.
                data = cursor.fetchall()
                return data






# Ruta: src/infrastructure/persistence/mysql/product_repository_mysql.py.
# ProductService invoca este adaptador. Los valores SQL se envían separados de la consulta.
