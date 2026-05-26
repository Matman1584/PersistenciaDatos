import socket
import pickle
from tkinter import Tk, Label, Entry, Button, StringVar, Text, END

username = "[NoUser]"
IPservidor = "127.0.0.1"
puerto = 0
estado = "default"


def Enviar_msj():
    global  username, IPservidor, puerto, estado
    print(username, IPservidor, puerto, estado)
    Cuadro_chat.configure(state="normal")
    
    if estado == "ok":
        # creacion del socket
        # crear objeto socket; especificando version Ip usando protocolo IPv4 y puerto indicando protocolo TCP
        socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # conetar socket al servidor
        # socket_cliente.connect (direccion_servidor)
        direccion_servidor = (str(IPservidor), int(puerto))
        try:
            socket_cliente.connect(direccion_servidor)  # conexion con servidor
            mensaje_conex = Label(text="Estado conexión: ok")
            mensaje_conex.grid(column=0, row=7, sticky="W", padx=10, pady=10)
            print(f"conexion socekt {direccion_servidor}")
            msj = entrada_msj.get()
            envio = {}
            envio[username] = msj
            socket_cliente.send(pickle.dumps(envio)) # enviando mensaje al servidor
            Cuadro_chat.insert(END, msj + "\n")
            entrada_msj.delete(0, "end")
            Cuadro_chat.configure(state="disabled")
            socket_cliente.close()
            

        # envio de mesaje al servidor
        except OSError:
            print(f"conexion socekt {direccion_servidor}")
            mensaje_conex = Label(text="Estado conexión: error")
            mensaje_conex.grid(column=0, row=7)
            msj = str("Conexion fatal \n mensaje no entregado a destinatario")
            Cuadro_chat.insert(END, msj + "\n")
            Cuadro_chat.configure(state="disabled")
            socket_cliente.close()
        


def Salir():
    root.destroy()

def ingresar ():
    global username, IPservidor	, puerto, estado
    if entrada_Usuario.get() == "[NoUser]":
        pass
    else:
        username = entrada_Usuario.get()
        IPservidor = entrada_IPServidor.get()
        puerto = entrada_PuertoServidor.get()
        estado = "ok"
        UsuarioInf_label.config(text= f"Usuario: {username}\n IPServidor: {IPservidor} \n Puerto: {puerto} \n Estado: {estado}")
        
        return username, IPservidor	, puerto, estado
        
# frame chat
root = Tk()
root.title("BoxCliente")
root.geometry("400x350")
#root.resizable(False, False)

# Usuario
Variable_usuario = StringVar()
Variable_usuario.set(username)
Usuario_label = Label(text="Usuario: ")
Usuario_label.grid(column=0, row=0, sticky="E", padx=5, pady=5)
entrada_Usuario = Entry(textvariable=Variable_usuario)
entrada_Usuario.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
Boton_IngresarUsuario = Button(text="Ingresar", command=ingresar)
Boton_IngresarUsuario.grid(column=2, row=0, sticky="WE", padx=5, pady=5)
UsuarioInf_label = Label(text= f"Usuario: {username}\n Estado: {estado}")
UsuarioInf_label.grid (column=0, row=4, sticky="WE", padx=5, pady=5)

# Ip servidor
VariableIP=StringVar()
VariableIP.set(IPservidor)
IPServidor_label = Label(text="IP servidor: ")
IPServidor_label.grid(column=0, row=1, sticky="E", padx=5, pady=5)
entrada_IPServidor = Entry(textvariable= VariableIP)
entrada_IPServidor.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

# Puerto
Variable_puerto = StringVar()
Variable_puerto.set(puerto)
PuertoServidor_label = Label(text="Puerto: ")
PuertoServidor_label.grid(column=0, row=2, sticky="E", padx=5, pady=5)
entrada_PuertoServidor = Entry(textvariable= Variable_puerto)
entrada_PuertoServidor.grid(column=1, row=2, sticky="EW", padx=5, pady=5)



# salida segura
Boton_salir = Button(text="Salida segura", command=Salir)
Boton_salir.grid(column=2, row=8, sticky="WE", padx=10, pady=10)

# entrada de texto
Mensaje = Label(text="Mensaje: ")
Mensaje.grid(column=0, row=5, sticky="E", padx=10, pady=10)
entrada_msj = Entry()
entrada_msj.grid(column=1, row=5, sticky="EW", padx=10, pady=10)
Boton_enviar = Button(text="Enviar", command=Enviar_msj)
Boton_enviar.grid(column=2, row=5, sticky="EW", padx=10, pady=10)

# cuadro Historial Chat
Cuadro_chat = Text(state="disabled", height=8, width=4)
Cuadro_chat.grid(column=0, row=6, columnspan=3, sticky="EW", padx=10, pady=5)

Var_Mensaje_cone=StringVar()
Var_Mensaje_cone.set("sin conexion")
mensaje_conex = Label(textvariable=Var_Mensaje_cone)
mensaje_conex.grid(column=0, row=7)



root.mainloop()
