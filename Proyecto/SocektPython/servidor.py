from tkinter import Tk, Label
import pickle

import socket

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
        Socket_Cliente.send(b"hola desde el servidor")
        Socket_Cliente.close()

if __name__ == "__main__":
    conexion()