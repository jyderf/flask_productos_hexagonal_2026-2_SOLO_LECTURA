from src.application.service.product_service import ProductService
from flask import Blueprint, render_template
from src.infrastructure.persistence.mysql.product_repository_mysql import ProductRepositoryMySQL


# Agrupa las rutas de productos. app.py registra este Blueprint una sola vez.
# Todas las direcciones definidas aquí empiezan por /productos.
bp_products = Blueprint("products", __name__, url_prefix="/productos")


# Flask la llama desde la ruta del Blueprint al visitar GET /productos/.
# Llama ProductService.listar(ProductRepositoryMySQL) y envía las filas a src/views/templates/index.html.
@bp_products.get("/")
def listar():
    productos = ProductService.listar(ProductRepositoryMySQL)
    return render_template("index.html", productos=productos)

# Ruta: src/infrastructure/web/controllers/product_controller.py.
# app.py registra su Blueprint; conecta las peticiones HTTP con el servicio y las plantillas.
