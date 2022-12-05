# -*- coding: utf-8 -*-
"""Proyecto semestral.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MAvoju-J0Yvr86Hpzcr2jKOf1FzKilpA

**Elementos**

*   Radio hidraulico (R)
*   Pendiente de fondo (S)
*   Base (b)
*   Tirante (y)
*   Velocidad (V)
*   Volumen (Q)
*   Coeficiente de rugosidad (n)
"""

# Datos de entrada respectivos del Canal.
base = float(input("Base(m) : "))
z = float(float (input("Z : ")))
S = float(input("pendiente de fondo S: "))
n = float(input("rugorosidad : "))
y = float(input("tirante normal (m) : "))

# Calculos 
A = base*y+z*y**2
P = base+2*y*(1+z**2)**.5
R = round(A/P,2)
print('El radio hidraulico es (m) : ', R)

#Velocidad
V = round(1/(n)*R**(2/3)*S**.5,2)
print('La velocidad del agua es de (m/s) :', V)
Q = round(V*A,2)
print('El volumen es de (m3):',Q, '\n')

#Imprimir localizacion del lugar
from geopy.geocoders import Nominatim
geolocalizador = Nominatim()
ubicacion = geolocalizador.reverse("19.211186523699826, -103.80443942468253")#Coordenadas del canal donde se realizo el area de estudio
print('La direccion es:', ubicacion.address)
print('Latitud y Longitud:', ubicacion.latitude, ubicacion.longitude)
print(ubicacion.raw)

"""**A partir de aqui son programas de visualizacion del area de estudio los cuales son:**


---


1.   Codigo que grafica la forma del poligono, que es la seccion de canal donde 
se trabajo. 
2.  Codigo que realiza la graficacion de la ubicacion del area donde se trabajo en un mapa, el cual contiene proyeccion ortografica.
3.   Codigo que arroja un mapa interactivo para desplazar alrededor de donde nos marca la ubicacion del canal. **texto en negrita**
**Recomendacion.**

---

Se aconseja instalar las librerias que estan al principio de este apartado, para que los programas corran satisfactoriamente.
"""

!pip install folium

!pip install xlrd

!pip install basemap

# GRAFICOS REPRESENTATIVOS DEL CANAL.
from google.colab import files
from google.colab import drive
import matplotlib.pyplot as plt
import pandas as pd
import xlrd

#Representacion del canal en 2D
drive.mount('/gdrive')
df= pd.read_excel('/gdrive/MyDrive/Colab Notebooks/SECCIONES/SECCIONES.xlsx',sheet_name= 'Hoja1')

VALORES = df[['Cadenamientos','Cotas']]
ax= VALORES.plot(x='Cadenamientos', y= 'Cotas',rot=0)
plt.xlabel('Cadenamientos')
plt.ylabel('Cotas')
plt.show

#Ubicacion del canal en un mapa con proyeccion ortografica.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None,
            width=8E6, height=8E6, 
            lat_0=45, lon_0=-100,)
m.etopo(scale=1.0, alpha=1.0)

# Map (long, lat) to (x, y) for plotting
x, y = m(-103.80450468775071,19.21095061186164)
plt.plot(x, y, 'ok', markersize=5)
plt.text(x, y, ' Caudal_FIC', fontsize=22);

#Codigo para un mapa interactivo en la ubicacion del lugar
import folium
m = folium.Map( 
    location=[19.211249641928656, -103.80451631674501], 
    zoom_start=12, 
    tiles='Stamen Terrain' 
) 
tooltip = 'Canal de estudio'
folium.Marker([19.211249641928656, -103.80451631674501], popup='Canal de estudio', tooltip=tooltip).add_to(m) 
m