# -*- coding: utf-8 -*-
#%%% Import
################################### Import ####################################
import pandas as pd
import os
import sys
###############################################################################
#%% Set Parameters
############################### Set Parameters ################################
actual_dir = os.getcwd()
file_dir_in = os.path.join(actual_dir,"Datos.tsv")
file_dir_out = os.path.join(actual_dir,"DatosOutput.csv")
###############################################################################
#%% Functions
################################# Functions ###################################
def Escribir_csv_desde_tsv(file_dir_in,file_dir_out):
    inputFile = open(file_dir_in, "r",encoding="UTF-16-LE")
    outputFile = open(file_dir_out, "w", encoding="UTF-8")
    vec = []
    for line in inputFile:
        entry = line.split("\t")
        for i in range(len(entry)):
            if entry[i] == ' ':
               entry[i] = ""
        if i == 4:
            #Escritura de archivo de salida sin los registros que estan "rotos"
            outputFile.write("|".join(entry))
        else:
            vec.append(entry)
    result_ejec = True     
    inputFile.close()
    outputFile.close()
    return(result_ejec,vec)
###############################################################################
#%% Principal
################################## Principal ##################################
#Leer el archivo de input en formato tsv y escribirlo en formato csv
[result_ejec, vec] = Escribir_csv_desde_tsv(file_dir_in,file_dir_out)

# Creacion de str_list con los valores de los registros que estan "rotos"
flat_list = []
for sublist in vec:
    for item in sublist:
        flat_list.append(item.strip())

#flat_list = [item.replace("n.a", "") for item in flat_list]
str_list = list(filter(None, flat_list))
###############################################################################