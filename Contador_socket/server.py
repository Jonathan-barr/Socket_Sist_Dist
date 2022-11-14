
from socket import error, socket
from threading import Thread

import numpy as np

#DEFINIMOS PUERTOS
HOST = "127.0.0.3"
PORT = 65002


def os_file (file): 
    file_obj = open(file, "r")
    file_data = file_obj.read()
    lines = file_data.splitlines()
    return lines

def split_wr (lines, users):   
    sub_lists = np.array_split(lines, users)
    count=0
    
    for i in sub_lists:
        with open(f"parte{count+1}.txt", 'w') as fp:
            for item in sub_lists[count]:
                fp.write("%s\n" % item)
            print('Done File ', count)
            count+=1

personas=0
class Client(Thread):
    def __init__(self, conn, addr, clie):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.clie = clie
        
    def run(self):
        global personas
        texto = str(self.clie)+". Bienvenido\nSeleccione una de las dos opciones\n1. Para recibir archivo\n2. Para salir"
        self.conn.send(bytes(texto, 'utf-8'))
        while True:
            try:
                
                input_data = self.conn.recv(1024)
                if str(input_data, "utf-8")=='1':
                    personas+=1
                    print("\r** Clientes conectados ["+str(personas)+"] **\n--------------------------------------\n¿Desea comenzar?\n1. Si\n2. No\n", end="\n", flush=True)
                    
            except error:
                print("[%s] Error de lectura. " % self.name)
            else:
                if str(input_data, "utf-8")!='1':
                    self.conn.send(b"** Muchas gracias por usar el servidor **")
                    break
            acciones = input("> ")
            if int(acciones) == 1:
                break
        files = "alice.txt"
        original = os_file(files)
        sub_lists = np.array_split(original, personas)
        count=0
        
        for i in sub_lists:
            with open(f"parte{count+1}.txt", 'w') as fp:
                for item in sub_lists[count]:
                    fp.write("%s\n" % item)
                print('Done File ', count)
                count+=1
        
        file = open(f"parte{self.clie+1}.txt", 'rb')
        line = file.read(1024)
        # Keep sending data to the client

        while(line):
            self.conn.send(line)
            line = file.read(1024)
        
        file.close()
        print("Archivo enviado a cliente "+str(self.clie+1))

            

def main():
    personas = 0
    s = socket()
    s.bind((HOST, PORT))
    print("--------------------------------------")
    print("Servidor encendido en el puerto: "+ str(PORT))
    print("--------------------------------------")
    print("")
    print("Esperando usuarios")
    print("--------------------------------------")
    for i in range(2):
        
        s.listen(i)
        conn, addr = s.accept()
        
        c = Client(conn, addr, i)
        
        c.start()

        
if __name__ == "__main__":
    main()
