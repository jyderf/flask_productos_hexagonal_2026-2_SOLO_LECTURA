from flask import Flask
from src.infrastructure.web.controllers.product_controller import bp_products

# Crea Flask; busca la plantilla HTML dentro de src/views/templates.
app = Flask(__name__, template_folder="src/views/templates", static_folder=None)
# Registra todas las rutas del Blueprint; las nuevas rutas se agregan en el controlador.
app.register_blueprint(bp_products)


if __name__ == "__main__":
    # Inicia el servidor local; Flask atenderá las solicitudes usando product_controller.listar.
    app.run(host="127.0.0.1", port=5000, debug=True)

# Ruta: app.py. Se invoca desde la terminal con: python app.py.
