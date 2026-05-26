import sqlite3

# conexion y creacion de cursor
conn = sqlite3.connect('BBDDPoryectoPYD.db')
cursor = conn.cursor()

# Creacion  tablas
# tablas Paises
cursor.execute('''CREATE TABLE IF NOT EXISTS PAISES (
    pais_ID INTEGER PRIMARY KEY,
    pais_nombre TEXT
)''')

# tabla Ciudades
cursor.execute('''CREATE TABLE IF NOT EXISTS CIUDADES (
    ciud_ID INTEGER PRIMARY KEY,
    ciud_nombre TEXT,
    ciud_pais_ID INTEGER,
    FOREIGN KEY (ciud_pais_ID) REFERENCES PAISES(pais_ID)
)''')

# tabla Localizaciones
cursor.execute('''CREATE TABLE IF NOT EXISTS LOCALIZACIONES (
    localiz_ID INTEGER PRIMARY KEY,
    localiz_ciudad_ID INTEGER,
    localiz_direccion TEXT,
    FOREIGN KEY (localiz_ciudad_ID) REFERENCES CIUDADES(ciud_ID)
)''')

# tabla Departamentos
cursor.execute('''CREATE TABLE IF NOT EXISTS DEPARTAMENTOS (
    dpto_ID INTEGER PRIMARY KEY,
    dpto_nombre TEXT
)''')

# tabla Cargos
cursor.execute('''CREATE TABLE IF NOT EXISTS CARGOS (
    cargo_ID INTEGER PRIMARY KEY,
    cargo_nombre TEXT,
    cargo_sueldo_minimo REAL,
    cargo_sueldo_maximo REAL
)''')

# tabla Empleados
cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLEADOS (
    empl_ID INTEGER PRIMARY KEY,
    empl_primer_nombre TEXT,
    empl_segundo_nombre TEXT,
    empl_email TEXT,
    empl_fecha_nac TEXT,
    empl_sueldo REAL,
    empl_comision REAL,
    empl_cargo_ID INTEGER,
    empl_Gerente_ID INTEGER,
    empl_dpto_ID INTEGER,
    FOREIGN KEY (empl_cargo_ID) REFERENCES CARGOS(cargo_ID),
    FOREIGN KEY (empl_Gerente_ID) REFERENCES EMPLEADOS(empl_ID),
    FOREIGN KEY (empl_dpto_ID) REFERENCES DEPARTAMENTOS(dpto_ID)
)''')

# tabla Historicos
cursor.execute('''CREATE TABLE IF NOT EXISTS HISTORICO (
    emphist_ID INTEGER PRIMARY KEY,
    emphist_fecha_retiro TEXT,
    emphist_cargo_ID INTEGER,
    emphist_dpto_ID INTEGER,
    FOREIGN KEY (emphist_cargo_ID) REFERENCES CARGOS(cargo_ID),
    FOREIGN KEY (emphist_dpto_ID) REFERENCES DEPARTAMENTOS(dpto_ID)
)''')

# Insert data into PAISES
cursor.executemany('INSERT INTO PAISES (pais_ID, pais_nombre) VALUES (?, ?)', [
    (1, 'Argentina'),
    (2, 'Brazil'),
    (3, 'Chile'),
    (4, 'Peru'),
    (5, 'Uruguay')
])

# Insert data into CIUDADES
cursor.executemany('INSERT INTO CIUDADES (ciud_ID, ciud_nombre, ciud_pais_ID) VALUES (?, ?, ?)', [
    (1, 'Buenos Aires', 1),
    (2, 'Rio de Janeiro', 2),
    (3, 'Santiago', 3),
    (4, 'Lima', 4),
    (5, 'Montevideo', 5)
])

# Insert data into LOCALIZACIONES
cursor.executemany('INSERT INTO LOCALIZACIONES (localiz_ID, localiz_ciudad_ID, localiz_direccion) VALUES (?, ?, ?)', [
    (1, 1, 'Calle Falsa 123'),
    (2, 2, 'Avenida Brasil 456'),
    (3, 3, 'Calle O bello 789'),
    (4, 4, 'Avenida Larco 1011'),
    (5, 5, 'Calle 18 de Julio 1213')
])

# Insert data into DEPARTAMENTOS
cursor.executemany('INSERT INTO DEPARTAMENTOS (dpto_ID, dpto_nombre) VALUES (?, ?)', [
    (1, 'Recursos Humanos'),
    (2, 'Ventas'),
    (3, 'Marketing'),
    (4, 'IT'),
    (5, 'Administración')
])

# Insert data into CARGOS
cursor.executemany('INSERT INTO CARGOS (cargo_ID, cargo_nombre, cargo_sueldo_minimo, cargo_sueldo_maximo) VALUES (?, ?, ?, ?)', [
    (1, 'Analista', 30000, 50000),
    (2, 'Gerente', 50000, 80000),
    (3, 'Desarrollador', 40000, 70000),
    (4, 'Vendedor', 20000, 40000),
    (5, 'Soporte', 25000, 45000)
])

# Insert data into EMPLEADOS
cursor.executemany('INSERT INTO EMPLEADOS (empl_ID, empl_primer_nombre, empl_segundo_nombre, empl_email, empl_fecha_nac, empl_sueldo, empl_comision, empl_cargo_ID, empl_Gerente_ID, empl_dpto_ID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [
    (1, 'Juan', 'Perez', 'juan.perez@mail.com', '1980-01-01', 35000, 5000, 1, None, 1),
    (2, 'Maria', 'Lopez', 'maria.lopez@mail.com', '1985-02-02', 60000, 7000, 2, 1, 2),
    (3, 'Carlos', 'Garcia', 'carlos.garcia@mail.com', '1990-03-03', 45000, 6000, 3, 2, 3),
    (4, 'Ana', 'Martinez', 'ana.martinez@mail.com', '1995-04-04', 30000, 4000, 4, 3, 4),
    (5, 'Luis', 'Fernandez', 'luis.fernandez@mail.com', '2000-05-05', 27000, 3000, 5, 4, 5)
])

# Insert data into HISTORICO
cursor.executemany('INSERT INTO HISTORICO (emphist_ID, emphist_fecha_retiro, emphist_cargo_ID, emphist_dpto_ID) VALUES (?, ?, ?, ?)', [
    (1, '2020-01-01', 1, 1),
    (2, '2020-02-02', 2, 2),
    (3, '2020-03-03', 3, 3),
    (4, '2020-04-04', 4, 4),
    (5, '2020-05-05', 5, 5)
])

conn.commit()

conn.close()
