from flask import Flask, render_template, request
import sqlite3

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insertar', methods=['POST'])
def insertar():
    nombre = request.form['nombre']
    edad = request.form['edad']

    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conexion.commit()
    conexion.close()

    return 'Datos insertados correctamente'

@app.route('/consultar')
def consultar():
    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    filas = cursor.fetchall()
    conexion.close()

    return render_template('consulta.html', filas=filas)

if _name_ == '_main_':
    app.run(debug=True)
    