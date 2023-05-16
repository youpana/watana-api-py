import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from WatanaApi.watana import *

ruta = 'http://localhost:6001/api/v1/proveedor/lyLny3VbSmrlw8mJ9a1Io9n1hMAsbUvKBlG9CZrvu68'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJ0b2tlbiI6ImYwYjhkOTJkMTA1YTFjM2JhYTM0MjE3MDg2YTY4NDg1N2ExM2JjMzFkODJhOWU0ZCJ9.a_9AQUWLRk-ga4jhRVt_4adMHKFdP5lqVSxpquMmqlE'
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
    
