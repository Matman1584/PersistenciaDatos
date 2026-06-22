import socket
import json

def enviar_peticion(peticion):
    host = '127.0.0.1'
    puerto = 5000
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        cliente.connect((host, puerto))
        cliente.send(json.dumps(peticion).encode('utf-8'))
        respuesta = cliente.recv(2048).decode('utf-8')
        resultado = json.loads(respuesta)
        print("\n--- RESPUESTA DEL SERVIDOR ---")
        print(resultado['mensaje'])
        print("------------------------------\n")
    except ConnectionRefusedError:
        print("\nError: El servidor no está en línea. Inicia servidor.py primero.\n")
    finally:
        cliente.close()

def menu():
    while True:
        print("=== SISTEMA TRANSACCIONAL DE RECURSOS HUMANOS ===")
        print("1. Insertar todo (País, Ciudad, Localiz, Dpto, Cargo y Empleado)")
        print("2. Consultar un empleado (Select)")
        print("3. Retirar empleado (Delete lógico e Histórico)")
        print("4. Cambiar sede/ciudad de empleado (Update)")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            enviar_peticion({"accion": "INSERT_TODO"})
        elif opcion == '2':
            id_emp = input("Ingresa el ID del empleado a consultar: ")
            enviar_peticion({"accion": "SELECT", "datos": {"id": id_emp}})
        elif opcion == '3':
            id_emp = input("Ingresa el ID del empleado a retirar: ")
            enviar_peticion({"accion": "DELETE", "datos": {"id": id_emp}})
        elif opcion == '4':
            id_emp = input("Ingresa el ID del empleado a trasladar: ")
            enviar_peticion({"accion": "UPDATE_UBICACION", "datos": {"id": id_emp, "nuevo_dpto": 1}})
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()