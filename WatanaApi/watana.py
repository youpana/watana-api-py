import json
import requests

class WatanaApi:
    def __init__(self, url, token):
        self.api_url = url
        self.auth_token = token


    def send_post_request(self, data):
        if not self.api_url or not self.auth_token:
            raise ValueError('URL y token no configurados. Por favor, configúralos utilizando el método configure(url, token).')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.auth_token
        }

        response = requests.post(self.api_url, json=data, headers=headers)
        response.raise_for_status()
        
        return response.json()

    def consultar_carpeta(self, data):
        if data.get('operacion') != 'consultar_carpeta':
            data['operacion'] = 'consultar_carpeta'
        if not data.get('carpeta_codigo'):
            raise ValueError('"carpeta_codigo" debe existir')
        
        return self.send_post_request(data)

    def descargar_carpeta(self, data):
        if data.get('operacion') != 'descargar_carpeta':
            data['operacion'] = 'descargar_carpeta'
        if not data.get('carpeta_codigo'):
            raise ValueError('"carpeta_codigo" debe existir')
        
        return self.send_post_request(data)

    def eliminar_carpeta(self, data):
        if data.get('operacion') != 'eliminar_carpeta':
            data['operacion'] = 'eliminar_carpeta'
        if not data.get('carpeta_codigo'):
            raise ValueError('"carpeta_codigo" debe existir')
        
        return self.send_post_request(data)

    def enviar_carpeta(self, data):
        if data.get('operacion') != 'enviar_carpeta':
            data['operacion'] = 'enviar_carpeta'
        if not data.get('carpeta_codigo'):
            raise ValueError('"carpeta_codigo" debe existir')
        if not data.get('titulo'):
            raise ValueError('"titulo" debe existir')
        if not data.get('descripcion'):
            raise ValueError('"descripcion" debe existir')
        if not data.get('vigencia_horas'):
            raise ValueError('"vigencia_horas" debe existir')
        if not data.get('reemplazar'):
            raise ValueError('"reemplazar" debe existir')
        if not data.get('firmante'):
            raise ValueError('"firmante" debe existir')
        if not data['firmante'].get('email'):
            raise ValueError('"firmante.email" debe existir')
        if not data['firmante'].get('nombre_completo'):
            raise ValueError('"firmante.nombre_completo" debe existir')
        if not data.get('archivos'):
            raise ValueError('"archivos" debe existir')
        
        for i, archivo in enumerate(data['archivos']):
            if not archivo.get('nombre'):
                raise ValueError(f'"archivos[{i}].nombre" debe existir')
            if not archivo.get('zip_base64'):
                raise ValueError(f'"archivos[{i}].zip_base64" debe existir')
        
        return self.send_post_request(data)

    def validar_pdf(self, data):
        if data.get('operacion') != 'validar_pdf':
            data['operacion'] = 'validar_pdf'
        if not data.get('zip_base64'):
            raise ValueError('"zip_base64" debe existir')
        
