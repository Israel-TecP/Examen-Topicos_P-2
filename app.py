#2. Aplicación de Inventario
#Descripción: Un sistema para registrar y administrar productos en un almacén.
#Tecnologías: Python +Flask, Visual Studio Code, HTML+ Bootstrap
# Funciones CRUD:
#•	Crear un nuevo producto con nombre, cantidad y precio.
#•	Leer la lista de productos y su stock.
#•	Actualizar la cantidad y precio de un producto.
#•	Eliminar productos obsoletos.


from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import mysql.connector # importar el conector de MYsql

def get_db_connection():
    return mysql.connector.connect( # Ingresar los datos necesarios para ingresar a la base de dato
        host="localhost", # El nombre es localhost porque la base de datos esta en la computadora
        user="root", 
        password="10092005",
        database="inventario" # Nombre de la base de datos
    )
    
@app.route("/")
def index():
    conn=get_db_connection() # conectar a la base de datos
    cursor=conn.cursor() # El cursor es el que ejecuta las instrucciones en la base de datos como leer o escribir
    cursor.execute("SELECT * FROM tbl_productos") # el * selecciona toda la tabla
    Productos = cursor.fetchall() # fetchall trae todos los datos
    conn.close() # Cerrar la conexion a la base de datos
    return render_template("index.html", productos=Productos)

@app.route("/AñadirProducto", methods=["POST"]) 
def add():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO tbl_productos (Nombre, Cantidad, Precio, Caducidad) VALUES (%s, %s, %s, %s)", (request.form["inputProducto"], request.form["inputCantidad"], 
                    request.form["inputPrecio"], request.form["inputFecha"]))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM tbl_productos WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/Actualizar/<int:id>", methods=["POST"])
def update(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tbl_productos SET Nombre=%s, Cantidad=%s, Precio=%s, Caducidad=%s WHERE id = %s", (request.form["inputProducto"], 
                    request.form["inputCantidad"], request.form["inputPrecio"], request.form["inputFecha"], id))
    conn.commit()
    conn.close()
    return redirect('/')