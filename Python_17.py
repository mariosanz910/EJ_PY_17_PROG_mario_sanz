import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="empresa"
)

if conexion.is_connected():
    print("Conexión exitosa a la base de datos")

def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Gestionar Departamentos")
        print("2. Gestionar Categorías")
        print("3. Gestionar Clientes")
        print("4. Gestionar Trabajadores")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_departamentos()
        elif opcion == "2":
            menu_categorias()
        elif opcion == "3":
            menu_clientes()
        elif opcion == "4":
            menu_trabajadores()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# ======================== FUNCIONES CRUD PARA DEPARTAMENTOS ========================

# Menú para Departamentos
def menu_departamentos():
    while True:
        print("\n=== Gestión de Departamentos ===")
        print("1. Crear nuevo departamento")
        print("2. Leer departamentos existentes")
        print("3. Actualizar un departamento")
        print("4. Eliminar un departamento")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_departamento()
        elif opcion == "2":
            leer_departamentos()
        elif opcion == "3":
            actualizar_departamento()
        elif opcion == "4":
            eliminar_departamento()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

def crear_departamento():
    cursor = conexion.cursor()
    numdep = input("Introduce el código del departamento: ")
    nombredep = input("Introduce el nombre del departamento: ")
    consulta = "INSERT INTO departamento (numdep, nombredep) VALUES (%s, %s)"
    cursor.execute(consulta, (numdep, nombredep))
    conexion.commit()
    print(f"Departamento '{nombredep}' agregado exitosamente.")
    cursor.close()

def leer_departamentos():
    cursor = conexion.cursor()
    consulta = "SELECT * FROM departamento"
    cursor.execute(consulta)
    departamentos = cursor.fetchall()
    if departamentos:
        print("\n=== Departamentos ===")
        for dep in departamentos:
            print(f"Código: {dep[0]}, Nombre: {dep[1]}")
    else:
        print("No hay departamentos registrados.")
    cursor.close()

def actualizar_departamento():
    cursor = conexion.cursor()
    numdep = input("Introduce el código del departamento a actualizar: ")
    nuevo_nombre = input("Introduce el nuevo nombre del departamento: ")
    consulta = "UPDATE departamento SET nombredep = %s WHERE numdep = %s"
    cursor.execute(consulta, (nuevo_nombre, numdep))
    conexion.commit()
    print("Departamento actualizado correctamente.")
    cursor.close()

def eliminar_departamento():
    cursor = conexion.cursor()
    numdep = input("Introduce el código del departamento a eliminar: ")
    consulta = "DELETE FROM departamento WHERE numdep = %s"
    cursor.execute(consulta, (numdep,))
    conexion.commit()
    print("Departamento eliminado correctamente.")
    cursor.close()

# ======================== FUNCIONES CRUD PARA CATEGORÍAS ========================

# Menú para Categorías
def menu_categorias():
    while True:
        print("\n=== Gestión de Categorías ===")
        print("1. Crear nueva categoría")
        print("2. Leer categorías existentes")
        print("3. Actualizar una categoría")
        print("4. Eliminar una categoría")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_categoria()
        elif opcion == "2":
            leer_categorias()
        elif opcion == "3":
            actualizar_categoria()
        elif opcion == "4":
            eliminar_categoria()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

# CRUD Categorías
def crear_categoria():
    cursor = conexion.cursor()
    idcate = input("Introduce el código de la categoría: ")
    nombre = input("Introduce el nombre de la categoría: ")
    consulta = "INSERT INTO categoria (idcat, nombrecat) VALUES (%s, %s)"
    cursor.execute(consulta, (idcate, nombre))
    conexion.commit() # Guardar cambios con commit
    print(f"Categoría '{nombre}' agregada exitosamente.")
    cursor.close()

def leer_categorias():
    cursor = conexion.cursor()
    consulta = "SELECT * FROM categoria"
    cursor.execute(consulta)
    categorias = cursor.fetchall()
    if categorias:
        print("\n=== Categorías ===")
        for categ in categorias:
            print(f"Código: {categ[0]}, Nombre: {categ[1]}")
    else:
        print("No hay categorías registradas.")
    cursor.close()

def actualizar_categoria():
    cursor = conexion.cursor()
    idcate = input("Introduce el código de la categoría a actualizar: ")
    nuevo_nombre = input("Introduce el nuevo nombre de la categoría: ")
    consulta = "UPDATE categoria SET nombrecat = %s WHERE idcat = %s"
    cursor.execute(consulta, (nuevo_nombre, idcate))
    conexion.commit()
    print("Categoría actualizada correctamente.")
    cursor.close()

def eliminar_categoria():
    cursor = conexion.cursor()
    idcate = input("Introduce el código de la categoría a eliminar: ")
    consulta = "DELETE FROM categoria WHERE idcat = %s"
    cursor.execute(consulta, (idcate,))
    conexion.commit()
    print("Categoría eliminada correctamente.")
    cursor.close()

# ======================== FUNCIONES CRUD PARA CLIENTES ========================

def crear_cliente():
    cursor = conexion.cursor()
    nombre = input("Introduce el nombre del cliente: ")
    telefono = input("Introduce el teléfono del cliente: ")
    consulta = "INSERT INTO clientes (nombre, telefono) VALUES (%s, %s)"
    cursor.execute(consulta, (nombre, telefono))
    conexion.commit()
    print(f"Cliente '{nombre}' agregado exitosamente.")
    cursor.close()

def ver_clientes():
    cursor = conexion.cursor()
    consulta = "SELECT * FROM clientes"
    cursor.execute(consulta)
    clientes = cursor.fetchall()
    if clientes:
        print("=== Clientes ===")
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Teléfono: {cliente[2]}")
    else:
        print("No hay clientes registrados.")
    cursor.close()

def actualizar_cliente():
    cursor = conexion.cursor()
    cliente_id = input("Introduce el ID del cliente a actualizar: ")
    nuevo_nombre = input("Introduce el nuevo nombre del cliente: ")
    nuevo_telefono = input("Introduce el nuevo teléfono del cliente: ")
    consulta = "UPDATE clientes SET nombre = %s, telefono = %s WHERE id = %s"
    cursor.execute(consulta, (nuevo_nombre, nuevo_telefono, cliente_id))
    conexion.commit()
    print("Cliente actualizado exitosamente.")
    cursor.close()

def eliminar_cliente():
    cursor = conexion.cursor()
    cliente_id = input("Introduce el ID del cliente a eliminar: ")
    consulta = "DELETE FROM clientes WHERE id = %s"
    cursor.execute(consulta, (cliente_id,))
    conexion.commit()
    print("Cliente eliminado exitosamente.")
    cursor.close()

def menu_clientes():
    while True:
        print("\n=== Gestión de Clientes ===")
        print("1. Crear nuevo cliente")
        print("2. Ver clientes")
        print("3. Actualizar cliente")
        print("4. Eliminar un cliente")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            ver_clientes()
        elif opcion == "3":
            actualizar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

# ======================== FUNCIONES CRUD PARA TRABAJADORES ========================

def crear_trabajador():
    cursor = conexion.cursor()
    nombre = input("Introduce el nombre del trabajador: ")
    puesto = input("Introduce el puesto del trabajador: ")
    salario = input("Introduce el salario del trabajador: ")
    consulta = "INSERT INTO trabajadores (nombre, puesto, salario) VALUES (%s, %s, %s)"
    cursor.execute(consulta, (nombre, puesto, salario))
    conexion.commit()
    print(f"Trabajador '{nombre}' agregado exitosamente.")
    cursor.close()

def ver_trabajadores():
    cursor = conexion.cursor()
    consulta = "SELECT * FROM trabajadores"
    cursor.execute(consulta)
    trabajadores = cursor.fetchall()
    if trabajadores:
        print("=== Trabajadores ===")
        for trabajador in trabajadores:
            print(f"ID: {trabajador[0]}, Nombre: {trabajador[1]}, Puesto: {trabajador[2]}, Salario: {trabajador[3]}")
    else:
        print("No hay trabajadores registrados.")
    cursor.close()

def actualizar_trabajador():
    cursor = conexion.cursor()
    trabajador_id = input("Introduce el ID del trabajador a actualizar: ")
    nuevo_nombre = input("Introduce el nuevo nombre del trabajador: ")
    nuevo_puesto = input("Introduce el nuevo puesto del trabajador: ")
    nuevo_salario = input("Introduce el nuevo salario del trabajador: ")
    consulta = "UPDATE trabajadores SET nombre = %s, puesto = %s, salario = %s WHERE id = %s"
    cursor.execute(consulta, (nuevo_nombre, nuevo_puesto, nuevo_salario, trabajador_id))
    conexion.commit()
    print("Trabajador actualizado exitosamente.")
    cursor.close()

def eliminar_trabajador():
    cursor = conexion.cursor()
    trabajador_id = input("Introduce el ID del trabajador a eliminar: ")
    consulta = "DELETE FROM trabajadores WHERE id = %s"
    cursor.execute(consulta, (trabajador_id,))
    conexion.commit()
    print("Trabajador eliminado exitosamente.")
    cursor.close()

def menu_trabajadores():
    while True:
        print("\n=== Gestión de Trabajadores ===")
        print("1. Crear nuevo trabajador")
        print("2. Ver trabajadores existentes")
        print("3. Actualizar un trabajador")
        print("4. Eliminar un trabajador")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_trabajador()
        elif opcion == "2":
            ver_trabajadores()
        elif opcion == "3":
            actualizar_trabajador()
        elif opcion == "4":
            eliminar_trabajador()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Iniciamos el menú principal
menu_principal()

# Cerrar conexión al final por si es necesario
conexion.close()
