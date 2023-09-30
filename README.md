# Examen_final
## TABLE OF CONTENIDOS
1. Información General 
2. Aplicaciones, herramientas y librerías utilizadas
3. Instalación
4. Problemas presentados
5. Sobre mi

1.	 INFORMACIÓN GERENAL
El Proyecto consiste en realizar scrapping a una pagina web, en este caso se selecciono la pagina de EBAY específicamente al apartado de venta de relojes, se trabaja con selenium  y los datos se presentan con Flask haciendo uso de un computador con sistema operativo Windows 10.
Pasos:
a.	Realizar la búsqueda de una página web para realizar la extracción web
Se realiza la selección de la pagina EBAY de venta de relojes
 ![image](https://github.com/lazuniga03/Examen_final/assets/144503813/3579424c-bf98-4cc6-b29c-0f17252e93e9)

Figura 1 Pagina web seleccionada para scrapping https://www.ebay.com/e/latam/luxurywatches?_trkparms=pageci%3Adccab2fb-5f2e-11ee-9e84-f6ec8a7d2116%7Cparentrq%3Ae3a7c31f18a0a56184d7cfe3fffe68ce%7Ciid%3A1
b.	Almacenar datos en la nube o base de datos online.
Se realiza el guardado de la data extraída en MongoDB, en la cual se sincroniza los valores solicitado de Nombre del artículo, Precio y valor de envió.
 ![image](https://github.com/lazuniga03/Examen_final/assets/144503813/f113ea92-c96b-4fbb-a3ed-30dd56d60afa)
Figura 2 Almacenamiento de datos extraido en servidor MongoDB https://cloud.mongodb.com/v2/64ff99d28234ee613f078abf#/metrics/replicaSet/64ffa524f557635b5db3d6a8/explorer/ebay/relojes/find 
c.	Presentación de datos extraídos en un servicio web local Flask para print de datos.
Se trabaja con 
 ![image](https://github.com/lazuniga03/Examen_final/assets/144503813/ab95b112-f219-4a19-9b32-fccf35b8f656)

Figura 3 Print de datos extraídos de EBAY

2.	APLICACIONES, HERRAMIENTAS Y LIBRERIAS UTILIZADAS
PyCharm: Se hace uso del IDE PyCharm para simplificar la escritura del código de Python
PyCharm 2023.V.2.1
Windows 10.0
Memory: 2048M
Cores: 8

Navegador Web: Navegador web de su elección para búsqueda de api de la web seleccionada 
Google Chrome Versión 117.0.5938.132 (64 bits)
Windows 10.0
Un procesador Intel Pentium 4 o superior
Selenium: Es una herramienta de automatización de testing, soportados por los navegadores web el cual se lo programa a través de Python. Cabe indicar que se debe de inicializar el driver para poner a operar la librería.
Flask: Este ofrece un soporte para API siendo un marco web local para presentar datos de python

3.	INSTALACIÓN
Ejecución de requirements.txt
Se debe de ejecutar una línea de comando por consola para instalar los paquetes por cada entorno nuevo que se trabaje:
pip install -r requirements.txt

Configuración de Selenium
Para inicializar el «driver», en su versión más simple, usaremos el siguiente código:
from selenium import webdriver
WebDriver = webdriver.Chrome()
En este caso se inicializa para trabajar sobre el Navegador web Google Chrome

Configuración de Flask 
Para presentación de datos a nivel de servidor local y ver los datos extraídos a través de un navegador se debe de ejecutar líneas de código en pyton de la siguiente manera
from flask import Flask
app = Flask(__name__)
ejemplo:
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
4.	PROBLEMAS PRESENTADOS
Problema: Selección de encabezado para realizar el scrapping de la página web EBAY, ya que al momento de presentar no da información de la data extraida
Solución: Solo se debe de trabajar con un encabezado, del siguiente encabezado “s-item__info clearfix”, se debe de trabajar con el primer encabezado antes del estación, es decir “s-item__info”, al trabajar de esta manera te va a permitir extraer la data que se requiere

Problema: Proteger credenciales para conectar a la base de datos web MongoDB
Solución: Crear dentro de la carpeta principal del proyecto un archivo .env en el cual se darán valor a las variables de usuario y contraseña. De esta forma al omento de desarrollar el código se cita a las variables declaradas en el archivo .env, dando así confidencialidad de las credenciales de acceso. Cabe indicar que este archivo al momento de realizar un commit y push no será subido al GITHUB.
user = os.getenv("MONGO_USER")
 password = os.getenv("MONGO_PASSWORD")
 db_hostname = os.getenv("MONGO_HOST")
 uri = f"mongodb+srv://{user}:{password}@{db_hostname}/?retryWrites=true&w=majority"

5.	SOBRE MI
Mi nombre es Luis Zúñiga, tengo 29 años y vivo actualmente en las Islas Galápagos. Soy ingeniero en Electrónica y telecomunicaciones y trabajo en el área de redes e infraestructura de servidores, actualmente desarrollando una maestría en ciberseguridad para fortalecer las actuales actividades de mi trabajo.
Github @lazuniga03 
