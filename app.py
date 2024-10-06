from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Ruta para la página principal


@app.route('/')
def home():
    return render_template('index.html')  # archivo en la carpeta templates

# Ruta para el registro de usuarios


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombre = request.form['name']
        correo = request.form['email']
        telefono = request.form['phone']
        contraseña = request.form['password']

        # Guardar usuario en la base de datos
        conn = sqlite3.connect('hotel_reservas.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO usuarios (nombre, correo, telefono, contraseña) VALUES (?, ?, ?, ?)',
                           (nombre, correo, telefono, contraseña))
            conn.commit()
        except sqlite3.IntegrityError:
            return "El correo ya está registrado. Intenta con otro."
        finally:
            conn.close()
        return redirect(url_for('inicio_sesion'))
    return render_template('Registro.html')

# Ruta para el inicio de sesión


@app.route('/login', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        correo = request.form['email']
        contraseña = request.form['password']

        # Verificar credenciales
        conn = sqlite3.connect('hotel_reservas.db')
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM usuarios WHERE correo = ? AND contraseña = ?', (correo, contraseña))
        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            # Redirigir a la página principal si el inicio de sesión es exitoso
            return redirect(url_for('home'))
        else:
            return "Credenciales incorrectas. Inténtelo de nuevo."
    return render_template('login.html')

# Ruta para los tipos de habitaciones


@app.route('/tipos_habitaciones')
def tipos_habitaciones():
    # archivo en la carpeta templates
    return render_template('tipos_habitaciones.html')


if __name__ == '__main__':
    app.run(debug=True)
