import sqlite3

def create_prod(_name, _comps, _percs, _insts):
    # Se comprueba si el nombre de producto que se va a crear ya existe
    conn = sqlite3.connect('formulas.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM productos WHERE nombre = ?", (_name, ))
    conteo = cursor.fetchone()
    if conteo[0] > 0:
        raise sqlite3.ProgrammingError("El producto ya existe")
    else:
        # Se inserta un producto
        cursor.execute(f"INSERT INTO productos (nombre) VALUES (?)", (_name, ))

        # Se consulta el id del producto
        cursor.execute(f"SELECT id FROM productos WHERE nombre = ?", (_name, ))
        id_prod = cursor.fetchone()[0]

        data1 = list(zip(_comps, _percs, [id_prod] * len(_comps)))
        data2 = list(zip(_insts, [id_prod] * len(_insts)))

        # Se insertan los componentes
        cursor.executemany(f"INSERT INTO componentes (nombre, porcentaje, producto_id) VALUES (?, ?, ?)", data1)

        # Se insertan las instrucciones
        cursor.executemany(f"INSERT INTO instrucciones (instruccion, producto_id) VALUES (?, ?)", data2)

    conn.commit()
    conn.close()

def delete_prod(prod_name):
    conn = sqlite3.connect('formulas.db')
    cursor = conn.cursor()

    # se consulta el id del producto, ya que el argumento que llega es el nombre del producto
    cursor.execute("SELECT id FROM productos WHERE nombre = ?", (prod_name, ))
    _prod_id = cursor.fetchall()
    _prod_id = [prod[0] for prod in _prod_id][0]

    # se eliminan todos los datos relacionados con el producto
    cursor.execute(f'DELETE FROM componentes WHERE producto_id = ?', (_prod_id, ))
    cursor.execute(f'DELETE FROM instrucciones WHERE producto_id = ?', (_prod_id, ))
    cursor.execute(f'DELETE FROM productos WHERE nombre = ?', (prod_name, ))

    conn.commit()
    conn.close()

def get_prod_names():
    conn = sqlite3.connect('formulas.db')
    cursor = conn.cursor()

    # Consulta todos los productos para mostrarlos en los menú despegables
    cursor.execute("SELECT nombre FROM productos")
    data_raw = cursor.fetchall()

    conn.commit()
    conn.close()

    # toma los datos crudos y crea una lista que pueda ser leída por el programa
    data_list = [prod[0] for prod in data_raw]
    return data_list

def create_comp(_name, _perc, prod_name):
    conn = sqlite3.connect('formulas.db')
    cursor = conn.cursor()

    # se consulta el id del producto, ya que el argumento que llega es el nombre del producto
    cursor.execute("SELECT id FROM productos WHERE nombre = ?", (prod_name, ))
    _prod_id = cursor.fetchall()
    _prod_id = [prod[0] for prod in _prod_id][0]

    # Se comprueba si el nombre del componente ya está creado con el id del producto.
    # Esto para no repetir componentes en el mismo producto
    cursor.execute(f"SELECT COUNT(*) FROM componentes WHERE nombre = ? AND producto_id = ?", (_name, _prod_id))
    conteo = cursor.fetchone()
    if conteo[0] > 0:
        raise sqlite3.ProgrammingError("Este Componente ya existe en este producto")
    else: # se insertan los datos del componente
        cursor.execute(f"INSERT INTO componentes (nombre, porcentaje, producto_id) VALUES (?, ?, ?)", (_name, _perc, _prod_id))
    
    conn.commit()
    conn.close()

def create_inst(_inst, prod_name):
    conn = sqlite3.connect('formulas.db')
    cursor = conn.cursor()

    # se consulta el id del producto, ya que el argumento que llega es el nombre del producto
    cursor.execute("SELECT id FROM productos WHERE nombre = ?", (prod_name, ))
    _prod_id = cursor.fetchall()
    _prod_id = [prod[0] for prod in _prod_id][0]

    # se inserta la instrucción
    cursor.execute(f"INSERT INTO instrucciones (instruccion, producto_id) VALUES (?, ?)", (_inst, _prod_id))
    
    conn.commit()
    conn.close()

def get_prod(prod_name):
    conn = sqlite3.connect('formulas.db')
    cursor = conn.cursor()

    # se consulta el id del producto, ya que el argumento que llega es el nombre del producto
    cursor.execute("SELECT id FROM productos WHERE nombre = ?", (prod_name, ))
    _prod_id = cursor.fetchall()
    _prod_id = [prod[0] for prod in _prod_id][0]

    # Consulta los componentes de un producto para mostrarlos en la interfaz
    cursor.execute("SELECT nombre, porcentaje FROM componentes WHERE producto_id = ?", (_prod_id, ))
    comp_perc = cursor.fetchall()

    conn.commit()
    conn.close()
    return comp_perc

def get_inst(prod_name):
    conn = sqlite3.connect('formulas.db')
    cursor = conn.cursor()

    # se consulta el id del producto, ya que el argumento que llega es el nombre del producto
    cursor.execute("SELECT id FROM productos WHERE nombre = ?", (prod_name, ))
    _prod_id = cursor.fetchall()
    _prod_id = [prod[0] for prod in _prod_id][0]

    # Consulta las instrucciones de un producto para mostrarlas en la interfaz
    cursor.execute("SELECT instruccion FROM instrucciones WHERE producto_id = ?", (_prod_id, ))
    inst = cursor.fetchall()

    conn.commit()
    conn.close()
    return inst


if __name__ == "__main__":
    _name = "deter_prueba2"
    _comps = ["agua", "Lauril", "glicerina"]
    _percs = [0.75, 0.12, 0.13]
    _insts = ["agregar agua", "mezclar Lauril", "agregar glicerina"]
    create_prod(_name, _comps, _percs, _insts)