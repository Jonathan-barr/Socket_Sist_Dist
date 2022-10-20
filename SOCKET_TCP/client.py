import socket

HOST = "127.0.0.1"
PORT = 65000

#CREAMOS EL SOCKET DEL CLIENTE
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b"Hola desde el cliente") ##transformo a binario
    data=s.recv(1024)
print(f"Recibido desde el servidor {data!r}")

#Ctrl+Shift+` para el terminal