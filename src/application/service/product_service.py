class ProductService:
    # ProductRepositoryMySQL es un parámetro recibido del controlador, no un import.
    # Tiene el mismo nombre que la clase enviada desde el controlador para facilitar el seguimiento.
    @staticmethod
    # Lo llama product_controller.listar() en infrastructure/web/controllers/product_controller.py.
    # Llama ProductRepositoryMySQL.listar(): en la aplicación es ProductRepositoryMySQL.listar(); devuelve las filas.
    def listar(ProductRepositoryMySQL):
        # El parámetro ProductRepositoryMySQL recibe la clase del mismo nombre desde el controlador.
        # Su listar() está en src/infrastructure/persistence/mysql/product_repository_mysql.py.
        data = ProductRepositoryMySQL.listar()
        return data

# Ruta: src/application/service/product_service.py.
# La función listar del controlador invoca el servicio para consultar los productos.

