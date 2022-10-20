
import socket

#DEFINIMOS PUERTOS
HOST = "127.0.0.1"
PORT = 65000 ##65500 HACIA ABAJO

#CREAMOS EL SOCKET DEL SERVIDOR
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s: #STREAM TCP / DGRAM UDP
    #VINCULAMOS EL SOCKET AL PUERTO Y LA DIRECCION
    s.bind((HOST,PORT))
    #PONEMOS AL SOCKET A ESCUCHAR LAS CONEXIONES
    s.listen()
    conn,addr=s.accept()

    with conn:
        #SI ENCUENTRA UNA CONEXION INDICAR MENSAJE
        print(f"Conectado exitosamente: {addr}")
        while conn:
            data = conn.recv(1024)
            if not data:
                # SI NO HAY
                print("No hay datos")
                break
            conn.sendall(data) 