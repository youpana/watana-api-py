# WatanaApi Python


Nuestra Biblioteca Python oficial de WatanaApi, es compatible con la [v1.0](https://ayuda.llama.pe/integracion/) de Watana API, con el cual tendrás la posibilidad de crear carpetas, consultarlas, eliminarlas, firmar pdfs, validarlos, y aplicarles sello de tiempo.


## Requisitos 

* Python3.
* Registrate [aquí](https://watana.pe/registro).
* Una vez registrado, si vas a realizar pruebas obtén tus llaves desde [aquí](https://watana.pe/auths).

> Recuerda que para obtener tus llaves debes ingresar a tu Watana.pe > WATANA API > ***Autenticacion***.

![alt tag](https://i.imgur.com/6i1moyJ.png)



## Instalación

```py
from watana import WatanaApi
ruta = '<RUTA>'
token = '<TOKEN>'
api = WatanaApi(ruta, token)

```

## Enviar Carpeta

[Ver ejemplo completo](/examples/enviar_carpeta.py)

Puedes enviar una carpeta con archivos para ser firmada a Watana App.

```py
# Crear el diccionario de datos
data = {
    'carpeta_codigo': 'DOC001',
    'titulo': 'Carpeta o archivo de pruebas',
    'descripcion': 'Descripcion de la carpeta'
    .....
}
# Llamar a la función 
try:
    response = api.enviar_carpeta(data)
    print(response)
except Exception as e:
    print(str(e))
```

## Consultar Carpeta

[Ver ejemplo completo](/examples/consultar_carpeta.py)

```py
# Crear el diccionario de datos
data = {
    'carpeta_codigo': 'DOC001'
}
# Llamar a la función 
try:
    response = api.consultar_carpeta(data)
    print(response)
except Exception as e:
    print(str(e))
```

## Descargar Carpeta

```py
# Crear el diccionario de datos
data = {
    'carpeta_codigo': 'DOC001'
}
# Llamar a la función 
try:
    response = api.descargar_carpeta(data)
    print(response)
except Exception as e:
    print(str(e))
```

## Eliminar Carpeta

```py
# Crear el diccionario de datos
data = {
    'carpeta_codigo': 'DOC001'
}
# Llamar a la función 
try:
    response = api.eliminar_carpeta(data)
    print(response)
except Exception as e:
    print(str(e))
```

## Validar PDF

```py
# Crear el diccionario de datos
data = {
    'zip_base64': 'XXXXXX'
}
# Llamar a la función 
try:
    response = api.validar_pdf(data)
    print(response)
except Exception as e:
    print(str(e))
```

## Firmar PDF

```py
# Crear el diccionario de datos
data = {
    'zip_base64': 'XXXXXX'
}
# Llamar a la función 
try:
    response = api.firmar_pdf(data)
    print(response)
except Exception as e:
    print(str(e))
```

## Sellar PDF

```py
# Crear el diccionario de datos
data = {
    'zip_base64': 'XXXXXX'
}
# Llamar a la función 
try:
    response = api.sellar_pdf(data)
    print(response)
except Exception as e:
    print(str(e))
```
    
## Pruebas

Antes de pasar tu cuenta a producción, te recomendamos realizar pruebas de integración. Así garantizarás un correcto despliegue.



## Documentación
¿Necesitas más información para integrar `watana-api-py`? La documentación completa se encuentra en [https://ayuda.llama.pe/integracion](https://ayuda.llama.pe/integracion)


