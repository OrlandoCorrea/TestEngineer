# -*- coding: utf-8 -*-

# Importar librerias
import pandas as pd
import unidecode
from Funciones import *
from Database import *
from InsertDB import *
from scriptsql import *
from timeit import default_timer as timer
from datetime import timedelta
import time


start = timer()

## Creación de la Tabla
create_table()

# Rutas de Archivos
path_csv = "C:/Users/Orlando/Documents/TestEngineer/Tratados_internacionales_de_Colombia.csv"
path_json = "C:/Users/Orlando/Documents/TestEngineer/all.json"

# Extracción y Lectura de la información

dataframe_tratados= pd.read_csv(path_csv, quotechar='"',header=0,engine='python')
data_countrys = pd.read_json(path_json, typ='series')

## Transformación de la información

acople_listas = []
fullist_insert = []
fronteras = ""

dataframe_tratados = dataframe_tratados.replace(["(NO REGISTRA)","(NO REGISTRA)\n"], [None,None])

for index_tratados, x in dataframe_tratados.iterrows():
    for index_countrys, y in data_countrys.items():
        estados_organismos = normalize_countrys(unidecode.unidecode(str(x['Estados-Organismos']).lower()))
        pais = unidecode.unidecode(str(y['translations']['spa']['common']).lower())
        fronteras = exist_border(y)
        diff_time = diff_zonetime(y['timezones'])
        if x['Bilateral'] == "SI":
            bilateral = True
        else:
            bilateral = False
        if x['Vigente'] == "SI":
            vigente = True
        else:
            vigente = False
        if findword(estados_organismos,pais):
            info = {'Nombre del Tratado':x['Nombre del Tratado'],
                                 'Bilateral':bilateral,
                                 'Lugar de Adopcion':x['Lugar de Adopcion'],
                                 'Fecha de Adopcion':x['Fecha de Adopcion'],
                                 'Estados-Organismos':x['Estados-Organismos'],
                                 'Temas':x['Temas'],
                                 'Naturaleza del Tratado':x['Naturaleza del Tratado'],
                                 'Depositario':x['Depositario'],
                                 'Suscribio Por Colombia':x['Suscribio Por Colombia'],
                                 'Vigente':vigente,
                                 'Fecha Ley Aprobatoria':x['Fecha Ley Aprobatoria'],
                                 'Numero Ley Aprobatoria':x['Numero Ley Aprobatoria'],
                                 'Sentencia Fecha Ley':x['Sentencia Fecha Ley'],
                                 'Sentencia Numero':x['Sentencia Numero'],
                                 'Decreto Fecha Diario Oficial':x['Decreto Fecha Diario Oficial'],
                                 'Decreto Numero Diario Oficial':x['Decreto Numero Diario Oficial'],
                                 'Pais del Tratado':y['translations']['spa']['common'],
                                 'Codigo de llamadas':y['idd']['root'],
                                 'Capital':y['capital'],
                                 'Region':y['region'],
                                 'Subregion':y['subregion'],
                                 'Poblacion':y['population'],
                                 'Area':y['area'],
                                 'Zona horaria':y['timezones'],
                                 'Monedas':y['currencies'],
                                 'Idiomas':y['languages'],
                                 'Cantidad Fronteras':fronteras,
                                 'Diferencia horas zona horaria':diff_time
                                 }
            info_probe = [tuple([x['Nombre del Tratado']]),tuple([bilateral]),tuple([x['Lugar de Adopcion']]),tuple([x['Fecha de Adopcion']]),tuple([x['Estados-Organismos']]),tuple([x['Temas']]),tuple([x['Naturaleza del Tratado']]),tuple([x['Depositario']]),tuple([x['Suscribio Por Colombia']]),tuple([vigente]),tuple([x['Fecha Ley Aprobatoria']]),tuple([x['Numero Ley Aprobatoria']]),tuple([x['Sentencia Fecha Ley']]),tuple([x['Sentencia Numero']]),[x['Decreto Fecha Diario Oficial']],tuple([x['Decreto Numero Diario Oficial']]),tuple([y['translations']['spa']['common']]),tuple([y['idd']['root']]),tuple([y['capital']]),tuple([y['region']]),tuple([y['subregion']]),tuple([y['population']]),tuple([y['area']]),tuple([y['timezones']]),tuple([list(y['currencies'])]),tuple([list(y['languages'])]),tuple([fronteras]),tuple([diff_time])]
            acople_listas.append(info)
            fullist_insert.append(info_probe)

insert_data(fullist_insert)
df = pd.DataFrame(acople_listas)

dataframe_final = pd.DataFrame(acople_listas)
dataframe_final.to_parquet('test_engineer.parquet')

## Ejecución script SQL
querysql()


end = timer()
print(timedelta(seconds=end-start))
## Insercción de la información en la tabla
