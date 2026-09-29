from decimal import Decimal


# Representa un producto del negocio; no depende de Flask ni de MySQL.
# Puede usarse al crear, editar o consultar productos, si se trabaja con objetos.
# El listado actual no utiliza esta clase: recibe diccionarios del repositorio
# y los envía directamente a la plantilla index.html.
class Product:
    @staticmethod
    # Método de fábrica: crea y devuelve un objeto Product con valores iniciales.
    # No es un constructor __init__ ni guarda información en la base de datos.
    # En un futuro CRUD, el servicio puede llamarlo para preparar un producto
    # y asignarle los datos antes de enviarlo al repositorio.
    def crear():
        # Cada llamada crea un producto independiente.
        producto = Product()
        # Un producto nuevo todavía no tiene un ID asignado por la base de datos.
        producto.id = None
        producto.name = ""
        # Decimal representa el precio con precisión decimal.
        producto.price = Decimal("0.00")
        producto.description = ""
        return producto


# Ruta: src/domain/model/product.py.
# Actualmente no lo invoca ningún servicio. Se conserva como base para ampliar
# el ejemplo; crear() solo prepara datos y no valida, consulta ni escribe en la BD.
