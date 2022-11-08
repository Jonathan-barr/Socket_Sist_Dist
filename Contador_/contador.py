# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:16:15 2021

@author: jonatbarr
"""
import math
import numpy as np
import re  ## elimina los caracteres especiales
import csv  ## generar los archivos y leerlos
import nltk  ## Natural Languaje Toolkit
from nltk.corpus import stopwords  ## carga las stopwords
import time

nltk.download('stopwords')  ## descomentar antes de entregar

from nltk.stem import PorterStemmer  ## importamos stemmer de porter
from sklearn.feature_extraction.text import CountVectorizer

## importar archivo CSV



with open ('alice.txt') as archivo:
    palabra = []
    for linea in archivo:
        array = linea.split()
        for parte in array: 
            if parte not in palabra and parte in stopwords.words(): 
                palabra.append(parte)



## medir tiempo de ejecucion
def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        print('El tiempo de ejecución es de: ', (time.time() - inicio), ' segundos')
        return c

    return funcion_medida


# Eliminación de Stopwords
ne = stopwords.words('english')


## Función para eliminar StopWords
def stopWords(doc):
    docr = doc
    for word in doc:
        if word in ne:
            docr.remove(word)
    return docr



def SteamingPor(doc):
    return [Porter.stem(i) for i in doc]


## Funcion para Limpieza de Datos

def NLP(filas):
    for i in range(len(filas)):
        filas[i] = (re.sub('[^A-Za-z0-9]+', ' ', filas[i])).lower().split()
    #stm = [SteamingPor(j) for j in filas]
    return [stopWords(i) for i in filas]


titlimp = NLP(palabra)  ## titulos limpios

print(titlimp)
