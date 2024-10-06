import sqlite3

# Conectar a SQLite (crea la base de datos si no existe)
conn = sqlite3.connect('hotel_reservas.db')
cursor = conn.cursor()

# Crear tabla de usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL UNIQUE,
        telefono TEXT,
        contraseña TEXT NOT NULL
    )
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
