 # **Determinación de volúmenes de caudales y su ubicación en Python**
**Campos Rodríguez José Luis (1), Gutiérrez Camacho Reyes Omar (2), Vega Solorio Karla Leticia (3)**

` `(1) Centro de cómputo de la Facultad de Ingeniería Civil, Campus Coquimatlán, Km. 9 Carretera, Colima - Coquimatlán, Jardines del Llano, 28400 Coquimatlán, Col., <jcampos6@ucol.mx>, <rgutierrez34@ucol.mx>, <kvega0@ucol.mx>

Campos Rodríguez José Luis; Gutiérrez Camacho Reyes Omar; Vega Solorio Karla Leticia. *Título: Determinación de volúmenes y su ubicación en Python.* 



**Resumen**

Se generará un programa en Python el cual tiene como propósito leer un archivo de Excel, en el que se encuentran datos de un levantamiento de secciones sobre un canal que se encuentra en el campus Coquimatlán en la Facultad de Ingeniería Civil, para obtener como resultado que el programa genere de manera automática el volumen obtenido de cierto canal proporcionándole ciertos datos clave, también para un mayor entendimiento visual graficar los resultados.

**Palabras clave:** 1. Programa. 2.Python. 3. Canales


 **Introducción**
Apoyándose del trabajo realizado en la materia de proyecto integrador, se idea la elaboración de un código en lenguaje Python que nos sea de ayuda para realizar cálculos sobre volúmenes, velocidad del agua por segundo en los canales así como la graficacion de una sección en particular del canal la cual haría que nosotros lográramos visualizar más o menos la forma en que está construido el canal e identificar si la pendiente es positiva o negativa, como elemento un poco más enfocado a lo geoespacial se tiene planeado realizar un apartado en el código que nos permita que mediante las coordenadas del lugar nos arroje la ubicación del canal en donde se realizó el trabajo. 



**Abstract**

A Python program will be generated whose purpose is to read an Excel file, in which data from a survey of sections on a canal located on the Coquimatlán campus in the Faculty of Civil Engineering are found, to obtain as a result that the program automatically generates the volume obtained from a certain channel, providing you with certain key data, also for a better visual understanding, graph the results.

**Keywords**: 1. Program 2. Python 3. Channels.



 **Desarrollo.**
Primeramente, antes de comenzar la realización de los programas y mostrar el resultado final, se realizan diversas investigaciones en las cuales se tiene como objetivo tener una idea más clara de cuál será el proceso que se deberá seguir para que nuestros códigos de Python sean lo suficientemente satisfactorio.

Hay que destacar que este proyecto tiene gran importancia, ya que se va a evaluar la calidad del producto de una serie de procedimientos que se realizaron para poder así llevarlo a cabo y los resultados que se obtendrán sean favorables. 

Los datos sobre la sección en específico se toman de una práctica topográfica la cual consistía en el levantamiento de secciones transversales justamente de un caudal de interés dentro de las instalaciones de la facultad, con esto obtuvimos los datos más relevantes y de importancia para la realización de este proyecto final. 

Algunas de las herramientas / materiales que utilizamos y fueron fundamentales necesitan para poder llevar a cabo este proyecto final son:

- Nivel de mano
- Estadales
- Longimetro
- Python
- Google Colab.
- Excel

Posterior a esto se procede a investigar a que tipo de canal pertenece el canal en el que realizamos el estudio, esto para saber cómo calcular el volumen y hacer que nuestros datos sean los necesarios para realizar esos cálculos correspondientes en Python.

Se comienza la investigación sobre librerías de Python que se puedan utilizar para poder darnos la ubicación del área de estudio, esto va enfocado más a lo geoespacial, entre estas librerías se encuentran Basemap, Folium, entre otras, las cuales nos pueden marcar mediante un punto donde se encuentra el lugar de trabajo.

 ![](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.001.png)Exportamos los datos obtenidos de las secciones a una hoja de cálculo en Excel, para tener un mejor manejo de los datos.
 
![Aspose Words 27374307-8477-4757-971b-f37617b88388 001](https://user-images.githubusercontent.com/119511322/205752692-151a5302-c607-4085-b103-8ea56b936f52.png)
*Imagen 1. Datos del canal.*

 Subimos nuestro archivo Excel a nuestro drive y procedemos a crear el código que nos permitirá graficar la sección de dicho canal ya mencionado, al código tenemos que ponerle el nombre del archivo que subimos a drive y ejecutará los datos de las secciones.

![](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.002.png)
![Aspose Words 27374307-8477-4757-971b-f37617b88388 002](https://user-images.githubusercontent.com/119511322/205753698-080a7c54-a298-4aa7-ac22-670c82a41d1b.png)

*Imagen 2. Código grafico de secciones con el uso de la librería matplotlib.*

 Ejecutamos y nos dará el resultado de la sección referida de dicho canal graficada con el uso de las librerías.

![](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.003.png)
![Aspose Words 27374307-8477-4757-971b-f37617b88388 003](https://user-images.githubusercontent.com/119511322/205754650-4f2334fe-75a9-43a0-9fe2-fe10262cf036.png)

*Imagen 3. Resultado grafico obtenido del código grafico de secciones.*

 Además, este programa nos permitirá conocer dicha ubicación del canal ubicado en la 	Facultad de Ingeniería Civil. 

![](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.004.png)
![Aspose Words 27374307-8477-4757-971b-f37617b88388 004](https://user-images.githubusercontent.com/119511322/205754987-2241d7e9-1a54-4c60-b1a3-259b3bc282c8.png)

*Imagen 4. Código Python geoespacial.*



La ejecución del código mostro lo siguiente:

![](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.005.png)
![Aspose Words 27374307-8477-4757-971b-f37617b88388 005](https://user-images.githubusercontent.com/119511322/205755374-8670ad55-8d65-4dd7-803f-b92cd72261f3.png)

*Imagen 5. Código ejecutado resultado con el uso de las librerías matplotlib y basemap.*

Para el cálculo del volumen del canal en Python realizamos un código que a partir de las características del canal nos permitiera conocer cuál sería su volumen.

 Ya como último paso que realizamos fue crear el programa en Python para poder calcular el volumen (caudal) de dicho canal con los datos obtenidos, para realizar el código tomamos en cuenta las características de los canales y ciertos aspectos que nos parecieron interesantes para poder conocer el volumen (caudal), a partir de ciertos datos a ingresar de forma manual al programa. otra parte interesante que tiene el código de programación es que se pueden integrar los datos de manera manual, para poder así tener el manejo de los datos. 

![Aspose Words 27374307-8477-4757-971b-f37617b88388 006](https://user-images.githubusercontent.com/119511322/205755745-a25f3180-549d-4993-9465-b65ba943031d.png)

![](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.006.png)*Imagen 6. Código Python Volumen canal*


Resultado obtenido después de la ejecución: 

![](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.007.png)
![Aspose Words 27374307-8477-4757-971b-f37617b88388 007](https://user-images.githubusercontent.com/119511322/205756243-f81ce549-8f74-411a-8150-60aa54e76224.png)

*Imagen 7. Resultado código ejecutado cálculo de volúmenes*

 Se realizo también dos códigos en colab los cuales también van de entrada en nuestra parte geoespacial del proyecto realizado, el primer código realizado nos permite obtener la ubicación del lugar de estudio en un mapa interactivo implementando la librería folium.

![Captura de pantalla (32)](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.008.png)
![Aspose Words 27374307-8477-4757-971b-f37617b88388 008](https://user-images.githubusercontent.com/119511322/205756582-9d7801b8-c3cd-4e73-92a2-455ad22b33a8.png)

`         `*Imagen 8. Resultado mapa interactivo con folium.*

Posteriormente se realizó un programa que, mediante las coordenadas del lugar, este te arrogara datos relevantes del sitio, por ejemplo, la calle, código postal, ciudad, etc.

## **3. Manejo de datos**
Las librerías utilizadas para realizar los códigos correspondientes utilizando el lenguaje Python de este proyecto son las siguientes:

- Numpy: La librería NumPy nos permitió una generación y manejo de datos extremadamente rápido. NumPy tiene su propia estructura de datos incorporada llamado arreglo que es similar a la lista normal de Python, pero puede almacenar y operar con datos de manera mucho más eficiente.
- Matplotlib: Esta librería nos ayudó a realizar el grafico de las secciones del canal. Matplotlib es una librería de Python especializada en la creación de gráficos en dos dimensiones. Permite crear y personalizar los tipos de gráficos más comunes, entre ellos: Diagramas de barras.

![](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.009.png)*Imagen 9. Código ejecutado resultado con el uso de las librerías matplotlib.*

- Basemap: Basemap no es exactamente una librería como tal. De hecho, es un conjunto de herramientas, una extensión, de la propia librería Matplotlib de Python.

Esta librería nos fue de gran ayuda ya que nos permitió por medio del código obtener como resultado el mapa con la ubicación de dicho canal.

![](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.010.png)

*Imagen 10. Resultado con el uso de las librerías basemap.*

- Folium: Librería que se utiliza para visualizar los mapas y el manejo mediante el uso de Python.
- Geopandas: GeoPandas es una de las librerías geoespaciales más completas de Python. Podríamos decir que es sencilla a la vez que compleja. 

Esta librería nos ayudó a obtener la ubicación geoespacial del canal, ubicado en la Facultad de Ingeniería Civil.

![](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.011.png)

*Imagen ilustrativa 11. Resultado con el uso de las librerías Geopandas.*

- GeoPy: GeoPy facilita a desarrolladores de Python localizar las coordenadas de direcciones, ciudades, países y puntos de referencia en todo el mundo mediante geocodificadores de terceros y otras fuentes de datos.

La librería nos ayudó a localizar la ubicación del canal. ![](Aspose.Words.22fd89d6-2d91-42b6-84df-92ab45620d4d.012.png)

*Imagen 12. Resultado con el uso de las librerías GeoPy.*

El uso de estas librerías fue esencial para el manejo de los datos en Python.
## **4. Resultados**

Respecto a los resultados, podemos decir que, si se lograron cumplir con los objetivos que nos planteamos para la elaboración de nuestro programa de Python, es decir, se pudo programar y obtener el volumen de dicho canal, se logró graficar las secciones del canal, además de poder geolocalizar el canal por medio de librerías geoespaciales en donde se especifica a detalle la ubicación y las coordenadas de este mismo.

Conforme al procesos del desarrollo de los programas pudimos comprobar que los datos obtenidos eran correctos tanto para el cálculo del volumen del canal y el grafico de las secciones del canal, además el uso de estas librerías nos sirvió de mucha ayuda de acuerdo con el objetivo del proyecto.

Los códigos realizados fueron los siguientes: 

#Codigo para cálculo de volumen Canal.

# Datos de entrada

base = float(input("Base(m) : "))

z = float(float (input("Z : ")))

S = float(input("pendiente de fondo S: "))

n = float(input("rugorosidad : "))

y = float(input("tirante normal (m) : "))

# Cálculos 

A = base\*y+z\*y\*\*2

P = base+2\*y\*(1+z\*\*2)\*\*.5

R = round(A/P,2)

print('El radio hidráulico es (m) : ', R)

#Velocidad

V = round(1/(n)\*R\*\*(2/3)\*S\*\*.5,2)

print('La velocidad del agua es de (m/s) :', V)

Q = round(V\*A,2)

print('El volumen es de (m3):',Q)

# Código para graficar las secciones.

from google.colab import files

from google.colab import drive

import matplotlib.pyplot as plt

import pandas as pd

import xlrd

drive.mount('/gdrive')

df= pd.read\_excel('/gdrive/MyDrive/Colab Notebooks/SECCIONES/SECCIONES.xlsx',sheet\_name= 'Hoja1')

VALORES = df[['Cadenamientos','Cotas']]

ax= VALORES.plot(x='Cadenamientos', y= 'Cotas',rot=0)

plt.xlabel('Cadenamientos')

plt.ylabel('Cotas')

plt.show


# Código para obtener la ubicación mediante las coordenadas.

from geopy.geocoders import Nominatim

geolocalizador = Nominatim()

ubicacion = geolocalizador.reverse("19.211186523699826, -103.80443942468253")

print(ubicacion.address)

print(ubicacion.latitude, ubicacion.longitude)

print(ubicacion.raw)

# Código Geoespacial para obtener la ubicación.

%matplotlib inline

import numpy as np

import matplotlib.pyplot as plt

from mpl\_toolkits.basemap import  Basemap

fig = plt.figure(figsize=(8, 8))

m = Basemap(projection='ortho', resolution=None,

`            `width=8E6, height=8E6, 

`            `lat\_0=45, lon\_0=-100,)

m.etopo(scale=1.0, alpha=1.0)

# Map (long, lat) to (x, y) for plotting

x, y = m(-103.80450468775071,19.21095061186164)

plt.plot(x, y, 'ok', markersize=5)

plt.text(x, y, ' Caudal\_FIC', font size=22);

#Codigo para un mapa interactivo en la ubicacion del lugar

import folium

m = folium.Map( 

`    `location=[19.211249641928656, -103.80451631674501], 

`    `zoom\_start=12, 

`    `tiles='Stamen Terrain' 

) 

tooltip = 'Canal de estudio'

folium.Marker([19.211249641928656, -103.80451631674501], popup='Canal de estudio', tooltip=tooltip).add\_to(m) 

## **5. Conclusiones**
A modo de cierre de este proyecto es importante mencionar que la intención de realizarlo era poder hacer un programa en Python, el cual nos calculara el volumen del canal, graficara las secciones y pudiera geolocalizar el lugar donde se ubica dicho canal. El cual logramos cumplir nuestros objetivos puestos para este proyecto. 

Al ser un éxito este programa, podemos usarlo como una gran herramienta de suma importancia para nosotros estudiantes, futuros ingenieros, y nos servirá de mucho al realizar los cálculos (volúmenes, secciones, ubicación) de un canal de una manera más rápida y sencilla.
## **Referencias**
- Cordova, P. L. A. (2018, 13 marzo). AREAS Y VOLUMENES DE FIGURAS EN PYTHON.
- 6 formas de calcular el volumen. (2019, 13 marzo).
- <https://www.fao.org/fishery/docs/CDrom/FAO_Traning/FAO_Training/General/x6708s/x6708s08.htm>
- Estructuras en Canales. (2003, 31 agosto). oocities.
- El paquete Numpy — Fundamentos de Programación en Python. (s. f.). 
- Gonzalez, L. (2022, 23 septiembre). Introducción a la Librería Matplotlib de Python. Aprende IA. 
- Estévez, R. (2019, 9 agosto). Creando mapas con Python, Matplotlib y Basemap. geomapik.
- Rédac, T. (2022, 2 agosto). Folium: descubra la biblioteca de Python Open Source. Formation Data Science | DataScientest.com.
- Morales, A. (2021, 25 noviembre). GeoPandas: Análisis de datos geográficos en Python. MappingGIS. 
- Morales, A. (2021, 25 noviembre). GeoPandas: Análisis de datos geográficos en Python. MappingGIS.
## **	
