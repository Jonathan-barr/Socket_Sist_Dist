#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:34:44 2022

@author: jbarrionuevo
"""    
import math
import numpy as np
import re  ## elimina los caracteres especiales
import csv  ## generar los archivos y leerlos
import nltk  ## Natural Languaje Toolkit
from nltk.corpus import stopwords  ## carga las stopwords
import time

# Eliminación de Stopwords
ne = stopwords.words('english')
lines = []
file = "alice.txt"
file1 = "parte1.txt"
file2 = "parte2.txt"
users = 2

##Open and split into lines a txt file
def os_file (file): 
    with open(file,'r') as data_file:
        for line in data_file:
            data = line.split()
            lines.append(data)
    return lines

## Open a file

#def o_file (file):
#    with open(file,'r') as data_file:
#        data1 = data_file
#    return data1
        
      

    
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
    for j in range (len(filas)):
     for i in range(len(filas[j])):
        filas[j][i] = (re.sub('[^A-Za-z0-9]+', ' ', filas[j][i])).lower().split()
    return filas

os_file(file)   
split_wr(lines)

archivo1 = os_file(file1)

test = NLP(archivo1)
test2 = stopWords(test)









