import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
VERSION = '1.0.0' #Muy importante, deberéis ir cambiando la versión de vuestra librería según incluyáis nuevas funcionalidades
PACKAGE_NAME = 'WatanaApi' #Debe coincidir con el nombre de la carpeta 
AUTHOR = 'LLAMA.PE' #Modificar con vuestros datos
AUTHOR_EMAIL = 'soporte@llama.pe' #Modificar con vuestros datos
URL = 'https://github.com/youpana/watana-api-py' #Modificar con vuestros datos

LICENSE = 'MIT' #Tipo de licencia
DESCRIPTION = 'Librería para consumir WATANA API para la firma de documentos PDF' #Descripción corta
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') #Referencia al documento README con una descripción más elaborada
LONG_DESC_TYPE = "text/markdown"

#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = ["requests", "jsonschema"]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    requires=INSTALL_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)