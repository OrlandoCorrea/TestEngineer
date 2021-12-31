# -*- coding: utf-8 -*-
import unidecode

######  FUNCIONES   #################
# Función para buscar los paises que componen los tratado
def findword(wordx, wordy):
    if (wordx.find(wordy) != -1):
        return True
    else:
        return False

# Función para diferencia en horas de Colombia con otra zona horaria
def diff_zonetime(x):
    if isinstance(x, str):
        x = x
    if isinstance(x, list):
        x = x[0]
    utctime = str(x).split("UTC")[1]
    if utctime == "":
        signo = "+"
        utctime = "+00"
    else:
        signo = str(utctime[0])

    hour = utctime[1:3]
    diff_hour = ""
    if signo == "+":
        diff_hour = abs(5 + int(hour))
    else:
        if int(hour) == 5:
            diff_hour = 0
        if int(hour) > 5:
            diff_hour = -abs(int(hour) - 5)
        elif int(hour) < 5:
            diff_hour = abs(5 - int(hour))
    return diff_hour
 
# Revisar fechas
def check_date(x):
    x = x
    if x == None:
        return "01/01/9999"
    else:
        return x
# Función normalizar algunos nombres de paises
def normalize_countrys(estados_organismos):
    if estados_organismos == unidecode.unidecode('GRAN BRETANA'.lower()):
        return 'reino unido'
    elif estados_organismos == unidecode.unidecode('ESLOVAQUIA'.lower()):
        return 'republica eslovaca'
    elif estados_organismos == unidecode.unidecode('CHECA REPUBLICA'.lower()):
        return 'chequia'
    elif estados_organismos == unidecode.unidecode('QATAR'.lower()):
        return 'catar'
    elif estados_organismos == unidecode.unidecode('NUEVA ZELANDIA'.lower()):
        return 'nueva zelanda'
    else:
        return estados_organismos

# Función para validar si existe atributo 'border'
def exist_border(value):
    if "borders" in value:
        return len(value['borders'])
    else:
        return 0