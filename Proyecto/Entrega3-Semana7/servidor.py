import socket
import json
import psycopg2
from psycopg2 import Error

# Configuración de tu base de datos PostgreSQL
DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'Politec1!',
    'host': 'localhost',
    'port': '5432'
}

def ejecutar_transaccion(accion, datos):
    try:
        conexion = psycopg2.connect(**DB_CONFIG)
        cursor = conexion.cursor()
        
        if accion == "INSERT_TODO":
            # 5.a: Crear país, ciudad, localiz, dpto, cargo y empleado
            cursor.execute("INSERT INTO PAISES VALUES (6, 'Perú');")
            cursor.execute("INSERT INTO CIUDADES VALUES (6, 'Lima', 6);")
            cursor.execute("INSERT INTO LOCALIZACIONES VALUES (6, 'Av. Arequipa 123', 6);")
            cursor.execute("INSERT INTO DEPARTAMENTOS VALUES (6, 'Marketing', 6);")
            cursor.execute("INSERT INTO CARGOS VALUES (6, 'Analista', 2000000, 4000000);")
            cursor.execute("""
                INSERT INTO EMPLEADOS (empl_ID, empl_primer_nombre, empl_email, empl_fecha_nac, empl_sueldo, empl_cargo_ID, empl_dpto_ID) 
                VALUES (6, 'Carlos', 'carlos@empresa.com', '1995-01-01', 2500000, 6, 6);
            """)
            mensaje = "Transacción completa: Se crearon todas las entidades y el empleado Carlos (ID 6)."
            
        elif accion == "SELECT":
            # 5.b: Consultar un empleado
            cursor.execute("SELECT * FROM EMPLEADOS WHERE empl_ID = %s;", (datos['id'],))
            registro = cursor.fetchone()
            mensaje = str(registro) if registro else "Empleado no encontrado."
            
        elif accion == "DELETE":
            # 5.c: Retiro de empleado (Insertar histórico y cambiar estado a borrado)
            # Primero obtenemos sus datos actuales
            cursor.execute("SELECT empl_cargo_ID, empl_dpto_ID FROM EMPLEADOS WHERE empl_ID = %s;", (datos['id'],))
            emp = cursor.fetchone()
            if emp:
                # CORRECCIÓN: Consultamos el ID más alto del histórico y le sumamos 1
                cursor.execute("SELECT COALESCE(MAX(emphist_ID), 0) + 1 FROM HISTORICO;")
                nuevo_id_historico = cursor.fetchone()[0]
                
                # Insertamos en histórico usando el ID dinámico y seguro
                cursor.execute("""
                    INSERT INTO HISTORICO (emphist_ID, emphist_fecha_retiro, emphist_cargo_ID, emphist_dpto_ID, emphist_empl_ID) 
                    VALUES (%s, CURRENT_DATE, %s, %s, %s);
                """, (nuevo_id_historico, emp[0], emp[1], datos['id']))
                
                # Marcamos como borrado
                cursor.execute("UPDATE EMPLEADOS SET estado = 'Borrado' WHERE empl_ID = %s;", (datos['id'],))
                mensaje = f"Transacción completa: Empleado {datos['id']} retirado y guardado en histórico con ID {nuevo_id_historico}."
            else:
                mensaje = "Error: Empleado no existe."
                
        elif accion == "UPDATE_UBICACION":
            # 5.d: Cambio de dirección/ciudad (Se logra cambiándolo a un departamento en otra ciudad)
            # Vamos a moverlo al departamento 1 (que está en Bogotá)
            cursor.execute("UPDATE EMPLEADOS SET empl_dpto_ID = %s WHERE empl_ID = %s;", (datos['nuevo_dpto'], datos['id']))
            mensaje = f"Transacción completa: Empleado {datos['id']} trasladado al departamento {datos['nuevo_dpto']}."

        # Si todo salió bien, confirmamos la transacción
        conexion.commit()
        return {"status": "OK", "mensaje": mensaje}

    except Error as e:
        if conexion:
            conexion.rollback() # Si hay error, deshacemos todo para proteger la base de datos
        return {"status": "ERROR", "mensaje": str(e)}
    finally:
        if conexion:
            cursor.close()
            conexion.close()

def iniciar_servidor():
    host = '127.0.0.1'
    puerto = 5000
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, puerto))
    servidor.listen(1)
    print(f"Servidor Socket iniciado y escuchando en {host}:{puerto}...")

    while True:
        conexion, direccion = servidor.accept()
        datos_recibidos = conexion.recv(1024).decode('utf-8')
        if datos_recibidos:
            peticion = json.loads(datos_recibidos)
            print(f"Petición recibida del cliente: {peticion['accion']}")
            
            # Ejecutamos la transacción en la BD
            respuesta = ejecutar_transaccion(peticion['accion'], peticion.get('datos', {}))
            
            # Enviamos respuesta al cliente
            conexion.send(json.dumps(respuesta).encode('utf-8'))
        conexion.close()

if __name__ == "__main__":
    iniciar_servidor()