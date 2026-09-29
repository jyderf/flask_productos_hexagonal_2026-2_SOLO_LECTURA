# Arrancar el proyecto con:
flask run

# Arrancar el proyecto de forma reactiva con:
flask --app app run --debug

# Productos con Flask y MySQL

Proyecto educativo para leer productos de MySQL y mostrarlos en HTML, sin crear, editar ni eliminar registros desde la aplicación. Usa Python 3.12, Flask, Jinja2 y arquitectura hexagonal.

## 1. Instalar

Necesitas Python 3.12, un servidor MySQL 8.0.16 o superior y MySQL Workbench.

Abre PowerShell en la carpeta del proyecto:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

No necesitas activar el entorno. Si no tienes el comando `py`, usa `python` después de comprobar que sea la versión 3.12.

## 2. Preparar MySQL

1. Inicia el servidor MySQL y conéctate desde Workbench.
2. Abre `dbs/productosdb.sql` y ejecuta **todo el archivo** para crear la base, la tabla y los datos de ejemplo.
3. Si acabas de descargar el proyecto, crea la configuración local:

```powershell
Copy-Item src/config/mysql_connection.example.py src/config/mysql_connection.py
```

Si ya tienes `mysql_connection.py` configurado, omite esa copia. Abre ese archivo y ajusta `HOST`, `PORT`, `USER`, `PASSWORD` y `DATABASE`. La conexión se configura allí, sin usar `.env`.

## 3. Arrancar

```powershell
.\.venv\Scripts\python.exe app.py
```

Abre [http://127.0.0.1:5000/productos/](http://127.0.0.1:5000/productos/).

Detén el servidor con **Ctrl+C**. Es un servidor de desarrollo para practicar localmente.

## Archivos principales

- `app.py`: crea Flask, registra el Blueprint de productos y arranca el servidor, sin funciones anidadas.
- `src/infrastructure/web/controllers/product_controller.py`: Blueprint, rutas y controlador. Las nuevas rutas de productos se agregan aquí, sin modificar `app.py`.
- `src/application/service/product_service.py`: casos de uso.
- `src/application/ports/product_repository.py`: clase padre del repositorio.
- `src/infrastructure/persistence/mysql/product_repository_mysql.py`: consultas SQL.
- `src/views/templates/index.html`: única plantilla HTML del listado, sin CSS ni JavaScript.

- `dbs/productosdb.sql`: creación de la base de datos.

El flujo se mantiene: app.py → controlador → servicio → puerto/repositorio MySQL → plantilla Jinja2. El repositorio solo ejecuta SELECT. Las filas se devuelven como diccionarios, sin modelo Product. No hay manejadores personalizados de errores ni notificaciones. El script SQL se usa únicamente para preparar la base de datos de forma manual.

## GitHub

El `.gitignore` excluye los entornos virtuales, cachés, archivos del editor y la configuración local de MySQL. El ejemplo de conexión y el script SQL sí se incluyen.

Antes de hacer un commit, revisa qué archivos vas a agregar:

```powershell
git status
git add .
git diff --cached
git commit -m "Proyecto de productos con Flask y MySQL"
```

Estos comandos requieren un repositorio Git inicializado. Si un archivo ya estaba versionado, `.gitignore` no lo deja de seguir automáticamente.

