if __name__ == "__main__":

    import sqlite3

    # Conectar a la base de datos (creará un archivo si no existe)
    conn = sqlite3.connect('formulas.db')

    # Crear un cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # insertar un producto en la tabla productos
    cursor.execute('''
        INSERT INTO productos (nombre) VALUES ("Acid Stone TX1")
    ''')

    # insertar los componentes a la tabla de componentes,  del producto antes insertado
    cursor.execute('''
        INSERT INTO componentes (nombre, porcentaje, producto_id) VALUES ("Sal", 0.99, 1)

    ''')
    cursor.execute('''
        INSERT INTO componentes (nombre, porcentaje, producto_id) VALUES ("Cloro al 91 en polvo", 0.01, 1)
    ''')

    # insertar las instrucciones a la tabla de instrucciones, del producto antes insertado
    inst_acid_stone_tx1 = [
        ("Agregar 3 kilos de sal al meclador de tambor y dar 20 min para remover suciedad", 1),
        ("Vaciar sal de limpieza", 1),
        ("Agregar la cantidad de sal y de cloro al 91 en polvo de la formula", 1),
        ("Mezclar por 3 horas", 1),
        ("vaciar y empacar la mezcla", 1)
    ]
    cursor.executemany(
        '''INSERT INTO instrucciones (instruccion, producto_id) VALUES (?, ?)''',
        (inst_acid_stone_tx1)
    )

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()



# SE INGRESARÁ UNA SEGUNDA FÓRMULA

# Conectar a la base de datos (creará un archivo si no existe)
    conn = sqlite3.connect('formulas.db')

    # Crear un cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # insertar un producto en la tabla productos
    cursor.execute('''
        INSERT INTO productos (nombre) VALUES ("Producto1")
    ''')

    # insertar los componentes a la tabla de componentes, del producto antes insertado 
    comp_prod1 = [
        ("Comp1", 0.08, 2),
        ("Comp2", 0.08, 2),
        ("Comp3", 0.08, 2),
        ("Comp4", 0.08, 2),
        ("Comp5", 0.08, 2),
        ("Comp6", 0.08, 2),
        ("Comp7", 0.08, 2),
        ("Comp8", 0.08, 2),
        ("Comp9", 0.08, 2),
        ("Comp10", 0.08, 2),
        ("Comp11", 0.08, 2),
        ("Comp12", 0.08, 2),
        ("Comp13", 0.01, 2),
        ("Comp14", 0.01, 2),
        ("Comp15", 0.01, 2),
        ("Comp16", 0.01, 2)
    ]
    cursor.executemany(
        '''INSERT INTO componentes (nombre, porcentaje, producto_id) VALUES (?, ?, ?)''', (comp_prod1)
    )

    # insertar las instrucciones a la tabla de instrucciones, del producto antes insertado
    inst_prod1 = [
        ("instrucción 1", 2),
        ("instrucción 2", 2),
        ("instrucción 3", 2),
        ("instrucción 4", 2),
        ("instrucción 5", 2)
    ]
    cursor.executemany(
        '''INSERT INTO instrucciones (instruccion, producto_id) VALUES (?, ?)''', (inst_prod1)
    )

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()