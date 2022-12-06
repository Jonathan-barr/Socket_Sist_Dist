import re  # # elimina los caracteres especiales
import time
from socket import error, socket

import nltk  # # Natural Languaje Toolkit
from nltk.corpus import stopwords  # # carga las stopwords

nltk.download('stopwords')

# Eliminación de Stopwords
ne = stopwords.words('english')

HOST = "127.0.0.3"
PORT = 65002

try:
    raw_input
except NameError:
    raw_input = input


##Open and split into lines a txt file
def os_file (file): 
    file_obj = open(file, "r")
    file_data = file_obj.read()
    lines = file_data.splitlines()
    return lines

## Function to delete stopwords
def stopWords(doc):
    docr = doc
    for word in doc:
        if word in ne:
            docr.remove(word)
    return docr

## Funcion para Limpieza de Datos
def NLP(filas):
    for i in range(len(filas)):
      filas[i] = (re.sub('[^A-Za-z0-9]+', ' ', filas[i])).lower().split()
      res = NEL(filas)
    return [stopWords(i) for i in res]

## Funcion para eliminar elementos vacios de la lista
def NEL(filas):
    res = [ele for ele in filas if ele != []]
    return res


## Funcion para contar el número de palabras 
    
def con_w (filas):
    n_words = 0
    for i in range (len(filas)):
        n_words = len(filas[i]) + n_words
        
    print('El número total de palabras es: ', n_words)
    return n_words

## medir tiempo de ejecucion
def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        print('El tiempo de ejecución es de: ', (time.time() - inicio), ' segundos')
        return c

    return funcion_medida


@mide_tiempo 
def Ej_solo(file):
    
    print('Bienvenido al Contador de Palabras')
    ## abrir el archivo    
    original = os_file(file)
    ## limpieza para obtener únicamente las palabras (inglés)
    con_w(NEL(NLP(original)))
    ##obtener el Num de palabras en el texto
  

def main():
    s = socket()
    s.connect((HOST,PORT))
    
    input_data = s.recv(1024)
    if input_data:
        print(input_data.decode("utf-8") if isinstance(input_data, bytes) else input_data)
    
    output_data = raw_input("> ")
    if output_data:
        try:
            s.send(output_data)
        except TypeError:
            s.send(bytes(output_data, "utf-8"))
  
    name = int(input_data.decode("utf-8")[0])+1   
    print("Holaaaaa "+str(name))
    file = open(f"parte{str(name)}.txt", 'wb')

    # Keep receiving data from the server
    line = s.recv(1024)

    while(line):
        file.write(line)
        line = s.recv(1024)
    
    s.close()
        
    Ej_solo(f"parte{str(name)}.txt")
        

if __name__ == "__main__":
    main()