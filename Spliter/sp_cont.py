#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:34:44 2022

@author: jbarrionuevo
"""    
import numpy as np
import re  ## elimina los caracteres especiales
import nltk  ## Natural Languaje Toolkit
from nltk.corpus import stopwords  ## carga las stopwords
import time

nltk.download('stopwords')

# Eliminación de Stopwords
ne = stopwords.words('english')
lines = []
file = "alice.txt"
file1 = "parte1.txt"
file2 = "parte2.txt"
users = 2

##Open and split into lines a txt file
def os_file (file): 
    file_obj = open(file, "r")
    file_data = file_obj.read()
    lines = file_data.splitlines()
    return lines

    
# function to split the file into the number of the parameter users
def split_wr (lines):   
    sub_lists = np.array_split(lines, users)
    count=0
    
    for i in sub_lists:
        with open(f"parte{count+1}.txt", 'w') as fp:
            for item in sub_lists[count]:
                fp.write("%s\n" % item)
            print('Done File ', count)
            count+=1

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
def Ej_solo():
    
    print('Bienvenido al Contador de Palabras')
    ## abrir el archivo    
    original = os_file(file)
    ## Separar en Líneas y crear archivos individuales
    split_wr(original)
    ## limpieza para obtener únicamente las palabras (inglés)
    con_w(NEL(NLP(original)))
    ##obtener el Num de palabras en el texto
  
Ej_solo()


    

        
