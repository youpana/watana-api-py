import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from WatanaApi.watana import *

ruta = '<RUTA>'
token = '<TOKEN>'
# Crear una instancia de WatanaApi
api = WatanaApi(ruta, token)


# Crear el diccionario de datos
data = {
    'carpeta_codigo': 'DOC00s1'
}

# Llamar a la función consultar_carpeta
try:
    response = api.consultar_carpeta(data)
    print(response)
except Exception as e:
    print(str(e))
    
