-- 1. Tablas padre (No dependen de ninguna otra)
CREATE TABLE PAISES (
    pais_ID INT PRIMARY KEY,
    pais_nombre VARCHAR(50) NOT NULL
);

CREATE TABLE CARGOS (
    cargo_ID INT PRIMARY KEY,
    cargo_nombre VARCHAR(50) NOT NULL, -- <-- Aquí faltaba la coma
    cargo_sueldo_minimo DECIMAL(10, 2),
    cargo_sueldo_maximo DECIMAL(10, 2)
);

-- 2. Tabla Hija (Depende de PAISES)
CREATE TABLE CIUDADES (
    ciudad_ID INT PRIMARY KEY,
    ciudad_nombre VARCHAR(50) NOT NULL,
    ciud_pais_ID INT,
    FOREIGN KEY (ciud_pais_ID) REFERENCES PAISES(pais_ID)
);

-- 3. Tabla Nieta (Depende de CIUDADES)
CREATE TABLE LOCALIZACIONES (
    localiz_ID INT PRIMARY KEY,
    localiz_direccion VARCHAR(100),
    localiz_ciudad_ID INT,
    FOREIGN KEY (localiz_ciudad_ID) REFERENCES CIUDADES(ciudad_ID) -- <-- Corregido a ciudad_ID
);

-- 4. Tabla Bisnieta (Depende de LOCALIZACIONES)
CREATE TABLE DEPARTAMENTOS (
    dpto_ID INT PRIMARY KEY,
    dpto_nombre VARCHAR(50) NOT NULL,
    dpto_localiz_ID INT,
    FOREIGN KEY (dpto_localiz_ID) REFERENCES LOCALIZACIONES(localiz_ID)
);

-- 5. Tabla Central (Depende de DEPARTAMENTOS y CARGOS)
CREATE TABLE EMPLEADOS (
    empl_ID INT PRIMARY KEY,
    empl_primer_nombre VARCHAR(50),
    empl_segundo_nombre VARCHAR(50),
    empl_email VARCHAR(100),
    empl_fecha_nac DATE,
    empl_sueldo DECIMAL(10, 2),
    empl_comision DECIMAL(5, 2),
    empl_cargo_ID INT,
    empl_dpto_ID INT,
    empl_Gerente_ID INT,
    FOREIGN KEY (empl_cargo_ID) REFERENCES CARGOS(cargo_ID),
    FOREIGN KEY (empl_dpto_ID) REFERENCES DEPARTAMENTOS(dpto_ID),
    FOREIGN KEY (empl_Gerente_ID) REFERENCES EMPLEADOS(empl_ID) 
);

-- 6. Tabla Final (Histórico de retiros)
CREATE TABLE HISTORICO (
    emphist_ID INT PRIMARY KEY,
    emphist_fecha_retiro DATE,
    emphist_cargo_ID INT,
    emphist_dpto_ID INT,
    emphist_empl_ID INT,
    FOREIGN KEY (emphist_cargo_ID) REFERENCES CARGOS(cargo_ID),
    FOREIGN KEY (emphist_dpto_ID) REFERENCES DEPARTAMENTOS(dpto_ID),
    FOREIGN KEY (emphist_empl_ID) REFERENCES EMPLEADOS(empl_ID)
);


--          INSERTS
-- Llenando PAISES
INSERT INTO PAISES (pais_ID, pais_nombre) VALUES -- <-- Corregido pais_ID
(1, 'Colombia'),
(2, 'Argentina'),
(3, 'México'),
(4, 'España'),
(5, 'Andorra');


-- Llenando CARGOS
INSERT INTO CARGOS (cargo_ID, cargo_nombre, cargo_sueldo_minimo, cargo_sueldo_maximo) VALUES
(1, 'Desarrollador Junior', 1500000.00, 3000000.00),
(2, 'Agente de soporte', 1300000.00, 2000000.00),
(3, 'Gerente de Proyectos', 5000000.00, 9000000.00),
(4, 'Ingeniero de Software', 3500000.00, 7500000.00),
(5, 'Director de Tecnología', 8000000.00, 15000000.00);


-- Llenando CIUDADES
INSERT INTO CIUDADES (ciudad_ID, ciudad_nombre, ciud_pais_ID) VALUES -- <-- Corregidos nombres de columnas y comas al final de cada fila
(1, 'Bogotá', 1),
(2, 'Medellín', 1),
(3, 'Pereira', 1),
(4, 'Buenos Aires', 2),
(5, 'Ciudad de México', 3);


-- Llenando LOCALIZACIONES
INSERT INTO LOCALIZACIONES (localiz_ID, localiz_direccion, localiz_ciudad_ID) VALUES
(1, 'Parque Funcional Fontibón, Calle 17', 1),
(2, 'Centro Comercial Hayuelos', 1),
(3, 'Plaza Claro, Avenida El Dorado', 1),
(4, 'Sede Principal Centro', 3),
(5, 'Sucursal Norte', 1);


-- Llenando DEPARTAMENTOS
INSERT INTO DEPARTAMENTOS (dpto_ID, dpto_nombre, dpto_localiz_ID) VALUES
(1, 'Tecnología e Ingeniería', 1),
(2, 'Soporte BPO', 3),
(3, 'Desarrollo de Software', 2),
(4, 'Administración Deportiva', 4),
(5, 'Recursos Humanos', 1);


-- Llenando EMPLEADOS
INSERT INTO EMPLEADOS (empl_ID, empl_primer_nombre, empl_segundo_nombre, empl_email, empl_fecha_nac, empl_sueldo, empl_comision, empl_cargo_ID, empl_dpto_ID, empl_Gerente_ID) VALUES
(1, 'Mateo', 'Sierra', 'msierra@empresa.com', '2000-08-15', 7500000.00, 0.00, 4, 1, NULL),
(2, 'Laura', 'Roméro', 'lgomez@empresa.com', '2001-05-20', 1800000.00, 0.05, 2, 2, 1),
(3, 'Jairo', 'Martínez', 'jmartinez@empresa.com', '1999-11-10', 2500000.00, 0.00, 1, 3, 1),
(4, 'Diego', 'López', 'dlopez@empresa.com', '2000-02-28', 5500000.00, 0.10, 3, 4, 1),
(5, 'Andu', 'Pérez', 'aperez@empresa.com', '1998-09-12', 1500000.00, 0.00, 2, 2, 2);


-- Llenando HISTORICO
INSERT INTO HISTORICO (emphist_ID, emphist_fecha_retiro, emphist_cargo_ID, emphist_dpto_ID, emphist_empl_ID) VALUES
(1, '2025-12-30', 2, 2, 1),
(2, '2024-06-15', 1, 3, 3),
(3, '2025-01-20', 2, 2, 2),
(4, '2023-11-30', 3, 4, 4),
(5, '2026-01-10', 2, 2, 5);


-- Demostración de que inserté los datos
SELECT * FROM EMPLEADOS;
SELECT * FROM DEPARTAMENTOS;
SELECT * FROM LOCALIZACIONES;