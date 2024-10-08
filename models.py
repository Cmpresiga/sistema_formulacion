if __name__ == "__main__":

    import sqlite3

    # Conectar a la base de datos (creará un archivo si no existe)
    conn = sqlite3.connect('formulas.db')

    # Crear un cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # Crear tablas
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS componentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            porcentaje REAL NOT NULL,
            producto_id INTEGER, FOREIGN KEY (producto_id) REFERENCES productos(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS instrucciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            instruccion TEXT NOT NULL,
            producto_id INTEGER, FOREIGN KEY (producto_id) REFERENCES productos(id)
        )
    ''')

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()