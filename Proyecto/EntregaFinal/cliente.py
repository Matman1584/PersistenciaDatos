import socket
import pickle
from tkinter import Tk, Label, Entry, Button, StringVar, Text, END

username = "[NoUser]"
IPservidor = "127.0.0.1"
puerto = 59420
estado = "default"


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

def CargarTODO():
    global  username, IPservidor, puerto, estado
    Origen="CargarTodo"
    Pais_Intro = entrada_Pais.get().upper()
    Departamento_Intro = entrada_Departamento.get().upper()
    Ciudad_Intro = entrada_Ciudad.get().upper()
    LocalidadBarrio_Intro = entrada_LocalidadBarrio.get().upper()
    Cargo_Intro = entrada_Cargo.get().upper()
    Empleado_Intro = entrada_Empleado.get().upper()
    Documento_Intro = entrada_DocumentoID.get()
    Ingreso_User = {"Origen":f"{Origen}",
                    "Pais":f"{Pais_Intro}",
                    "Departamento":f"{Departamento_Intro}",
                    "Ciudad":f"{Ciudad_Intro}",
                    "Localidad_Barrio":f"{LocalidadBarrio_Intro}",
                    "Cargo":f"{Cargo_Intro}",
                    "Empleado":f"{Empleado_Intro}",
                    "ID":f"{Documento_Intro}"}
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
            mensaje_conex.grid(column=0, row=11, sticky="W", padx=10, pady=10)
            print(f"conexion socekt {direccion_servidor}")
            socket_cliente.send(pickle.dumps(Ingreso_User)) # envio de mesaje al servidor
            socket_cliente.close()
        
        except OSError:
            print(f"conexion socekt {direccion_servidor}")
            mensaje_conex = Label(text="Estado conexión: error")
            mensaje_conex.grid(column=0, row=11)
            msj = str("Conexion fatal \n mensaje no entregado a destinatario")
            #Cuadro_chat.insert(END, msj + "\n")
            #Cuadro_chat.configure(state="disabled")
            socket_cliente.close()
    
def CargarPAIS():
    global  username, IPservidor, puerto, estado
    Origen="CargarPais"
    Pais_Intro = entrada_Pais.get().upper()
    Ingreso_User = {"Origen":f"{Origen}",
                    "Pais":f"{Pais_Intro}",
                    }
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
            mensaje_conex.grid(column=0, row=11, sticky="W", padx=10, pady=10)
            print(f"conexion socekt {direccion_servidor}")
            socket_cliente.send(pickle.dumps(Ingreso_User)) # envio de mesaje al servidor
            socket_cliente.close()
        
        except OSError:
            print(f"conexion socekt {direccion_servidor}")
            mensaje_conex = Label(text="Estado conexión: error")
            mensaje_conex.grid(column=0, row=11)
            msj = str("Conexion fatal \n mensaje no entregado a destinatario")
            #Cuadro_chat.insert(END, msj + "\n")
            #Cuadro_chat.configure(state="disabled")
            socket_cliente.close()

def CargarDepartamento():
    global  username, IPservidor, puerto, estado
    Origen="CargarDepartamento"
    Pais_Intro = entrada_Pais.get().upper()
    Departamento_Intro = entrada_Departamento.get().upper()
    Ingreso_User = {"Origen":f"{Origen}",
                    "Pais":f"{Pais_Intro}",
                    "Departamento":f"{Departamento_Intro}"}
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
            mensaje_conex.grid(column=0, row=11, sticky="W", padx=10, pady=10)
            print(f"conexion socekt {direccion_servidor}")
            socket_cliente.send(pickle.dumps(Ingreso_User)) # envio de mesaje al servidor
            socket_cliente.close()
        
        except OSError:
            print(f"conexion socekt {direccion_servidor}")
            mensaje_conex = Label(text="Estado conexión: error")
            mensaje_conex.grid(column=0, row=11)
            msj = str("Conexion fatal \n mensaje no entregado a destinatario")
            #Cuadro_chat.insert(END, msj + "\n")
            #Cuadro_chat.configure(state="disabled")
            socket_cliente.close()

def CargarCiudad():
    global  username, IPservidor, puerto, estado
    Origen="CargarCiudad"
    Pais_Intro = entrada_Pais.get().upper()
    Departamento_Intro = entrada_Departamento.get().upper()
    Ciudad_Intro = entrada_Ciudad.get().upper()
    Ingreso_User = {"Origen":f"{Origen}",
                    "Pais":f"{Pais_Intro}",
                    "Departamento":f"{Departamento_Intro}",
                    "Ciudad":f"{Ciudad_Intro}",
                    }
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
            mensaje_conex.grid(column=0, row=11, sticky="W", padx=10, pady=10)
            print(f"conexion socekt {direccion_servidor}")
            socket_cliente.send(pickle.dumps(Ingreso_User)) # envio de mesaje al servidor
            socket_cliente.close()
        
        except OSError:
            print(f"conexion socekt {direccion_servidor}")
            mensaje_conex = Label(text="Estado conexión: error")
            mensaje_conex.grid(column=0, row=11)
            msj = str("Conexion fatal \n mensaje no entregado a destinatario")
            #Cuadro_chat.insert(END, msj + "\n")
            #Cuadro_chat.configure(state="disabled")
            socket_cliente.close()

def CargarLocalidad():
    global  username, IPservidor, puerto, estado
    Origen="CargarLocalidad"
    Pais_Intro = entrada_Pais.get().upper()
    Departamento_Intro = entrada_Departamento.get().upper()
    Ciudad_Intro = entrada_Ciudad.get().upper()
    LocalidadBarrio_Intro = entrada_LocalidadBarrio.get().upper()
    Ingreso_User = {"Origen":f"{Origen}",
                    "Pais":f"{Pais_Intro}",
                    "Departamento":f"{Departamento_Intro}",
                    "Ciudad":f"{Ciudad_Intro}",
                    "Localidad_Barrio":f"{LocalidadBarrio_Intro}"
                    }
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
            mensaje_conex.grid(column=0, row=11, sticky="W", padx=10, pady=10)
            print(f"conexion socekt {direccion_servidor}")
            socket_cliente.send(pickle.dumps(Ingreso_User)) # envio de mesaje al servidor
            socket_cliente.close()
        
        except OSError:
            print(f"conexion socekt {direccion_servidor}")
            mensaje_conex = Label(text="Estado conexión: error")
            mensaje_conex.grid(column=0, row=11)
            msj = str("Conexion fatal \n mensaje no entregado a destinatario")
            #Cuadro_chat.insert(END, msj + "\n")
            #Cuadro_chat.configure(state="disabled")
            socket_cliente.close()       

def CargarCargo():
    global  username, IPservidor, puerto, estado
    Origen="CargarCargo"

    Cargo_Intro = entrada_Cargo.get().upper()

    Ingreso_User = {"Origen":f"{Origen}",
                    "Cargo":f"{Cargo_Intro}"
                    }
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
            mensaje_conex.grid(column=0, row=11, sticky="W", padx=10, pady=10)
            print(f"conexion socekt {direccion_servidor}")
            socket_cliente.send(pickle.dumps(Ingreso_User)) # envio de mesaje al servidor
            socket_cliente.close()
        
        except OSError:
            print(f"conexion socekt {direccion_servidor}")
            mensaje_conex = Label(text="Estado conexión: error")
            mensaje_conex.grid(column=0, row=11)
            msj = str("Conexion fatal \n mensaje no entregado a destinatario")
            #Cuadro_chat.insert(END, msj + "\n")
            #Cuadro_chat.configure(state="disabled")
            socket_cliente.close()

def CargarEmpleado():
    global  username, IPservidor, puerto, estado
    Origen="CargarEmpleado"
    Empleado_Intro = entrada_Empleado.get().upper()
    Documento_Intro = entrada_DocumentoID.get()
    Ingreso_User = {"Origen":f"{Origen}",
                    "Empleado":f"{Empleado_Intro}",
                    "ID":f"{Documento_Intro}"}
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
            mensaje_conex.grid(column=0, row=11, sticky="W", padx=10, pady=10)
            print(f"conexion socekt {direccion_servidor}")
            socket_cliente.send(pickle.dumps(Ingreso_User)) # envio de mesaje al servidor
            socket_cliente.close()
        
        except OSError:
            print(f"conexion socekt {direccion_servidor}")
            mensaje_conex = Label(text="Estado conexión: error")
            mensaje_conex.grid(column=0, row=11)
            msj = str("Conexion fatal \n mensaje no entregado a destinatario")
            #Cuadro_chat.insert(END, msj + "\n")
            #Cuadro_chat.configure(state="disabled")
            socket_cliente.close()

def ConsultarNumID():
    global  username, IPservidor, puerto, estado
    Origen="ConsultaXIDEmpleado"
    Documento_Intro = entrada_DocumentoID.get()
    Ingreso_User = {"Origen":f"{Origen}",
                    "ID":f"{Documento_Intro}"}
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
            mensaje_conex.grid(column=0, row=11, sticky="W", padx=10, pady=10)
            print(f"conexion socekt {direccion_servidor}")
            socket_cliente.send(pickle.dumps(Ingreso_User)) # envio de mesaje al servidor
            respuesta = socket_cliente.recv(4096)
            Cuadro_chat.configure(state="normal")
            Cuadro_chat.insert(END, respuesta.decode() + "\n")
            Cuadro_chat.configure(state="disabled")            
            
        
        except OSError:
            print(f"conexion socekt {direccion_servidor}")
            mensaje_conex = Label(text="Estado conexión: error")
            mensaje_conex.grid(column=0, row=11)
            msj = str("Conexion fatal \n mensaje no entregado a destinatario")
            #Cuadro_chat.insert(END, msj + "\n")
            #Cuadro_chat.configure(state="disabled")
            socket_cliente.close()
        finally:
            socket_cliente.close()


# frame chat
root = Tk()
root.title("BoxCliente")
root.geometry("470x650")
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
Boton_salir.grid(column=2, row=8, sticky="WE", padx=5, pady=5)

# Entrada Pais
Pais = Label(text="Pais: ")
Pais.grid(column=0, row=5, sticky="E", padx=5, pady=5)
entrada_Pais = Entry()
entrada_Pais.grid(column=1, row=5, sticky="EW", padx=5, pady=5)
Boton_Pais = Button(text="Cargar Pais",anchor='w', command=CargarPAIS)
Boton_Pais.grid(column=2, row=5, sticky="EW", padx=5, pady=5)

# Entrada Departamento
Departamento = Label(text="Departamento: ")
Departamento.grid(column=0, row=6, sticky="E", padx=5, pady=5)
entrada_Departamento = Entry()
entrada_Departamento.grid(column=1, row=6, sticky="EW", padx=5, pady=5)
Boton_Departamento = Button(text="Cargar Departamento",anchor='w',command=CargarDepartamento)
Boton_Departamento.grid(column=2, row=6, sticky="EW", padx=5, pady=5)

# Entrada Ciudad
Ciudad = Label(text="Ciudad: ")
Ciudad.grid(column=0, row=7, sticky="E", padx=5, pady=5)
entrada_Ciudad = Entry()
entrada_Ciudad.grid(column=1, row=7, sticky="EW", padx=5, pady=5)
Boton_Ciudad = Button(text="Cargar Ciudad",anchor='w',command=CargarCiudad)
Boton_Ciudad.grid(column=2, row=7, sticky="EW", padx=5, pady=5)

# Entrada LocalidadBarrio
LocalidadBarrio = Label(text="Localidad/Barrio: ")
LocalidadBarrio.grid(column=0, row=8, sticky="E", padx=5, pady=5)
entrada_LocalidadBarrio = Entry()
entrada_LocalidadBarrio.grid(column=1, row=8, sticky="EW", padx=5, pady=5)
Boton_LocalidadBarrio = Button(text="Cargar Localidad/Barrio",anchor='w',command=CargarLocalidad)
Boton_LocalidadBarrio.grid(column=2, row=8, sticky="EW", padx=5, pady=5)

# Entrada Cargo
Cargo = Label(text="Cargo: ")
Cargo.grid(column=0, row=9, sticky="E", padx=5, pady=5)
entrada_Cargo = Entry()
entrada_Cargo.grid(column=1, row=9, sticky="EW", padx=5, pady=5)
Boton_Cargo = Button(text="Cargar Cargo",anchor='w',command=CargarCargo)
Boton_Cargo.grid(column=2, row=9, sticky="EW", padx=5, pady=5)

# Entrada Empleado
Empleado = Label(text="Empleado: ")
Empleado.grid(column=0, row=10, sticky="E", padx=5, pady=5)
entrada_Empleado = Entry()
entrada_Empleado.grid(column=1, row=10, sticky="EW", padx=5, pady=5)
Boton_Empleado = Button(text="Cargar Empleado",anchor='w',command=CargarEmpleado)
Boton_Empleado.grid(column=2, row=10, sticky="EW", padx=5, pady=5)

# Entrada DocumentoID
DocumentoID = Label(text="DocumentoID: ")
DocumentoID.grid(column=0, row=11, sticky="E", padx=5, pady=5)
entrada_DocumentoID = Entry()
entrada_DocumentoID.grid(column=1, row=11, sticky="EW", padx=5, pady=5)
Boton_ConsultarNumID = Button(text="Consultar x ID",anchor='w',bg="green",fg="white",command=ConsultarNumID)
Boton_ConsultarNumID.grid(column=2, row=11, sticky="EW", padx=5, pady=5)

#Cargar Todo
TexTCargarTodo = Label(text="Use para cargar todos los registros")
TexTCargarTodo.grid(column=1, row=12, sticky="EW", padx=5, pady=5)
Boton_CargarTodo = Button(text="Cargar Todo",anchor='w',command=CargarTODO)
Boton_CargarTodo.grid(column=2, row=12, sticky="EW", padx=5, pady=5)






# cuadro Historial Chat
Cuadro_chat = Text(state="disabled", height=8, width=4)
Cuadro_chat.grid(column=0, row=13, columnspan=3, sticky="EW", padx=5, pady=5)

#Var_Mensaje_cone=StringVar()
#Var_Mensaje_cone.set("sin conexion")
#mensaje_conex = Label(textvariable=Var_Mensaje_cone)
#mensaje_conex.grid(column=0, row=7)



root.mainloop()
