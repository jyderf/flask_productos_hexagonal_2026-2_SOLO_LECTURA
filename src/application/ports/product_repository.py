"""Puerto del repositorio: contrato de las operaciones que necesita el servicio.

Ahora este archivo también define una clase base que heredan los repositorios.
Cualquier repositorio debe ofrecer este método:

listar()                  Devuelve las filas de MySQL como diccionarios (colección vacía si no hay filas).

El servicio llama este método directamente en el repositorio recibido como parámetro.
Los repositorios heredan el contrato y escriben su propio método estático.
Las lecturas se envían directamente a Jinja2. Este contrato solo permite consultas.
"""

# ProductRepository es una clase padre normal, como Animal en el ejemplo de herencia.
# ProductRepositoryMySQL(ProductRepository) hereda de ella, como Perro(Animal).
# Este puerto no importa MySQL ni Flask; solamente declara las operaciones.
class ProductRepository:
    # ProductService.listar() llama la versión escrita en el repositorio concreto.
    # @staticmethod permite llamar sin crear un objeto y sin utilizar self.
    # El hijo escribe su propia versión de cada operación para realizar el trabajo.
    # NotImplementedError avisa si se llama una operación que el hijo no escribió.
    @staticmethod
    # Debe devolver las filas como diccionarios; aquí no se ejecuta ningún SELECT.
    def listar():
        raise NotImplementedError("El repositorio hijo debe implementar listar().")

# Los métodos del hijo reemplazan los del padre: esto se llama sobrescribir.
# No se llama a estos cuerpos cuando el hijo implementa la operación correspondiente.
# Esta herencia sencilla no impide crear un hijo que olvide implementar un método.
# En ese caso, el hijo hereda el método del padre y, al llamarlo, aparece el aviso
# NotImplementedError. Las pruebas comprueban que ambos hijos escriban sus métodos.

# Ruta: src/application/ports/product_repository.py.
# Lo importan ProductRepositoryMySQL y RepositorioMemoria para heredar el contrato.
# ProductService sigue recibiendo el repositorio concreto desde el controlador.
