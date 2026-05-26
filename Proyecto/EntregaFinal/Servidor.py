import pickle
import sqlite3

import socket


# conexion y creacion de cursor
conn = sqlite3.connect('BBDDPoryectoPYD.db')
cursor = conn.cursor()

# Creacion  tablas
# tablas Paises
cursor.execute('''CREATE TABLE IF NOT EXISTS PAISES (
    Id_Pais INTEGER PRIMARY KEY AUTOINCREMENT,
    Pais_Nombre TEXT UNIQUE NOT NULL
)''')
# tabla Departamentos
cursor.execute('''CREATE TABLE IF NOT EXISTS DEPARTAMENTOS (
    ID_Departamento INTEGER PRIMARY KEY AUTOINCREMENT,
    Departamento_Nombre TEXT UNIQUE NOT NULL,
    Id_Departamento_Pais INTEGER,
    FOREIGN KEY (Id_Departamento_Pais) REFERENCES PAISES (Id_Pais)
)''')
# tabla Ciudades
cursor.execute('''CREATE TABLE IF NOT EXISTS CIUDADES (
    Id_Ciudad INTEGER PRIMARY KEY AUTOINCREMENT,
    Ciudad_Nombre TEXT UNIQUE NOT NULL,
    ID_Ciudad_Departamento INTEGER,
    FOREIGN KEY (ID_Ciudad_Departamento) REFERENCES DEPARTAMENTOS (Id_Departamento)
)''')
# tabla Localizaciones
cursor.execute('''CREATE TABLE IF NOT EXISTS LOCALIZACIONES (
    Id_Localizacion INTEGER PRIMARY KEY AUTOINCREMENT,
    Id_Localizacion_Ciudad INTEGER,
    Localizacion_Nombre TEXT UNIQUE NOT NULL,
    FOREIGN KEY (Id_Localizacion_Ciudad) REFERENCES CIUDADES(Id_Ciudad)
)''')
# tabla Cargos
cursor.execute('''CREATE TABLE IF NOT EXISTS CARGOS (
    Id_Cargo INTEGER PRIMARY KEY,
    Cargo_Nombre TEXT UNIQUE NOT NULL,
    Sueldo_Min_cargo REAL,
    Sueldo_Max_cargo  REAL
)''')
# tabla DocumentoIDs
cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLEADOS (
    Id_Empleado INTEGER PRIMARY KEY,
    Empleado_Nombre TEXT UNIQUE NOT NULL,
    NumId_Empleado INTEGER UNIQUE NOT NULL
)''')
conn.commit()

# crear objeto socket
# especificando version Ip usando protocolo IPv4 y puerto indicando protocolo TCP 

def conexion ():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establece coneccion mediante el metodo bind
    # una dirección y puerto

    Host = "127.0.0.1"
    Puerto = 59420

    socket_servidor.bind((Host,Puerto))

    # poner servidor en modo escucha, estableciendo el maximo de conexiones en cola
    socket_servidor.listen(5)

    while True:
        # aceptar conexiones entrantes retorna el socket del cliente y su direccion
        Socket_Cliente, adrr = socket_servidor.accept()
        print("Conexion establecida")
        print(f"conectado desde: {adrr}")
        print(Socket_Cliente)
        MensajeRecibido = pickle.loads(Socket_Cliente.recv(1024))
        print(MensajeRecibido)
                   
        if MensajeRecibido["Origen"]=="CargarTodo":
            try:
                Pais= MensajeRecibido["Pais"]
                Departamento = MensajeRecibido["Departamento"]
                Ciudad = MensajeRecibido["Ciudad"]
                Localidad_Barrio = MensajeRecibido["Localidad_Barrio"]
                Cargo = MensajeRecibido["Cargo"]
                Empleado = MensajeRecibido["Empleado"]
                IDEmpleado= MensajeRecibido["ID"]
                # validacion registros vacios
                if Pais !="" and Departamento !="" and Ciudad !="" and Localidad_Barrio !="" and Cargo !="" and Empleado !="" and IDEmpleado !="":
                    cursor.execute('INSERT INTO PAISES (Pais_Nombre) VALUES (?)',(f"{Pais}",))
                    cursor.execute('INSERT INTO DEPARTAMENTOS (Departamento_Nombre) VALUES (?)',(f"{Departamento}",))
                    cursor.execute('INSERT INTO CIUDADES (Ciudad_Nombre) VALUES (?)',(f"{Ciudad}",))
                    cursor.execute('INSERT INTO LOCALIZACIONES (Localizacion_Nombre) VALUES (?)',(f"{Localidad_Barrio}",))
                    cursor.execute('INSERT INTO CARGOS (Cargo_Nombre) VALUES (?)',(f"{Cargo}",))
                    cursor.execute('INSERT INTO EMPLEADOS (Empleado_Nombre,NumId_Empleado) VALUES (?,?)',(f"{Empleado}",f"{IDEmpleado}",))
                    conn.commit()
                else:
                    print("No es posible realizar la carga, se tiene campos vacios")
            except:
                print("verificar data")  
        
        elif MensajeRecibido["Origen"]=="CargarPais":
            try:
                Pais= MensajeRecibido["Pais"]            
                if Pais !="":
                    
                    cursor.execute('INSERT INTO PAISES (Pais_Nombre) VALUES (?)',(f"{Pais}",))
                    conn.commit()
                    print("Pais Cargado")
                else:
                    print("No es posible realizar la carga, se tiene campos vacios PAIS")
            except:
                print("verificar data paises")
        
        elif MensajeRecibido["Origen"]=="CargarDepartamento":
            try:
                Pais= MensajeRecibido["Pais"]
                Departamento = MensajeRecibido["Departamento"]
                consulta = "SELECT * FROM PAISES WHERE Pais_Nombre = ?"
                cursor.execute(consulta,(Pais,))
                resultado=cursor.fetchone()
                idPais= resultado[0]
                cursor.execute('INSERT INTO DEPARTAMENTOS (Departamento_Nombre, Id_Departamento_Pais) VALUES (?, ?)',(f"{Departamento}",idPais))
                conn.commit()
                print("Departamento Ingresado")
            except:
                print("Pais No creado, cargar pais para proceder con la carga de departamento")

        elif MensajeRecibido["Origen"]=="CargarCiudad":
            try:
                Pais= MensajeRecibido["Pais"]
                Departamento = MensajeRecibido["Departamento"]
                Ciudad = MensajeRecibido["Ciudad"]
                consulta = "SELECT * FROM DEPARTAMENTOS WHERE Departamento_Nombre = ?"
                cursor.execute(consulta,(Departamento,))
                resultado=cursor.fetchone()
                idDepartamento= resultado[0]
                cursor.execute('INSERT INTO CIUDADES (Ciudad_Nombre, ID_Ciudad_Departamento) VALUES (?, ?)',(f"{Ciudad}",idDepartamento))
                conn.commit()
                print("Ciudad Ingresada")
            except:
                print("Departamento no creado, cargar Departamento para proceder con la carga de Ciudad")

        elif MensajeRecibido["Origen"]=="CargarLocalidad":
            try:
                Ciudad = MensajeRecibido["Ciudad"]
                Localidad_Barrio = MensajeRecibido["Localidad_Barrio"]
                consulta = "SELECT * FROM CIUDADES WHERE Ciudad_Nombre = ?"
                cursor.execute(consulta,(Ciudad,))
                resultado=cursor.fetchone()
                idCiudad= resultado[0]
                cursor.execute('INSERT INTO LOCALIZACIONES (Localizacion_Nombre, Id_Localizacion_Ciudad) VALUES (?, ?)',(f"{Localidad_Barrio}",idCiudad))
                conn.commit()
                print("Localidad Ingresada")
            except:
                print("Departamento no creado, cargar Departamento para proceder con la carga de Ciudad")

        elif MensajeRecibido["Origen"]=="CargarCargo":
            try:
                Cargo= MensajeRecibido["Cargo"]            
                if Cargo !="":
                    cursor.execute('INSERT INTO CARGOS (Cargo_Nombre) VALUES (?)',(f"{Cargo}",))
                    conn.commit()
                    print("Cargo ingresado")
                else:
                    print("No es posible realizar la carga, se tiene campos vacios CARGO")
            except:
                print("verificar data CARGOS")

        elif MensajeRecibido["Origen"]=="CargarEmpleado":
            try:
                Empleado = MensajeRecibido["Empleado"]
                IDEmpleado= MensajeRecibido["ID"]
                # validacion registros vacios
                if Empleado !="" and IDEmpleado !="":
                    cursor.execute('INSERT INTO EMPLEADOS (Empleado_Nombre,NumId_Empleado) VALUES (?,?)',(f"{Empleado}",f"{IDEmpleado}",))
                    conn.commit()
                else:
                    print("No es posible realizar la carga, se tiene campos vacios")
            except:
                print("verificar data")
                 
        elif MensajeRecibido["Origen"]=="ConsultaXIDEmpleado":
            try:
                IDEmpleado= MensajeRecibido["ID"]
                consulta = "SELECT * FROM EMPLEADOS WHERE NumId_Empleado = ?"
                cursor.execute(consulta,(IDEmpleado,))
                resultado=cursor.fetchone()
                print(resultado[1])
                Socket_Cliente.sendall(resultado[1].encode())
                conn.close()
                   
            except:
                print(f"No es posible realizar LA BUSUEDAD ID {IDEmpleado} no existe")                                 
                    
        #Socket_Cliente.send(b"hola desde el servidor")
        Socket_Cliente.close()

if __name__ == "__main__":
    conexion()