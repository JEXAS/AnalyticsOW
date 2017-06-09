import pandas as pd
import numpy as np
import os
import matplotlib.ticker as mtick
from imgurpython import ImgurClient

def grafica(general, medallas, precision, nombre, sender, heroe):
    time = float(general[5]/general[4])
    winrate = general[3]
    bronze_rate = float(medallas[1]/medallas[0])
    silver_rate = float(medallas[2]/medallas[0])
    gold_rate = float(medallas[3]/medallas[0])
    precision_mira = precision[0]
    precision_sinmira = precision[1]
    lista = [(time*100),winrate,(bronze_rate*100),(silver_rate*100),
             (gold_rate*100),(precision_mira*100),(precision_sinmira*100)]
    nueva_lista = []
    for a in lista:
        a = round(a,2)
        nueva_lista.append(a)
    crear_archivo(nueva_lista,nombre, heroe, sender)

def crear_archivo(porcentajes, nombre, heroe, user_id):

    mycolors = ['black','green','brown','grey','yellow','purple','red']
    raw_data = {'label': ['Time','Win Rate','Bronze','Silver','Gold','Scoped','Unscoped'],
                heroe:  [porcentajes[0], porcentajes[1], porcentajes[2],
                          porcentajes[3], porcentajes[4], porcentajes[5],
                          porcentajes[6]]}

    df = pd.DataFrame(raw_data)
    plt = df.plot(x='label',kind='bar',fontsize=6, color=mycolors)
    for p in plt.patches:
        plt.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    grf = plt.get_figure()
    grf.savefig(str(nombre)+'.png')
    fichero = open(str(nombre)+'.png', 'rb')
    to_upload = fichero.read()
    nombre = str(nombre)+'.png'
    subir(grf, nombre, user_id, heroe)

def subir(grafica, nombre, user_id, heroe):
    client_id = '...'
    client_secret = '...'
    client = ImgurClient(client_id, client_secret)
    id_ = client.upload_from_path(nombre)
    print('Gráfica subida a: ', id_['link'])
    archivo = open('graficas.txt', 'a')
    os.remove(nombre)
    archivo.write(id_['link']+' '+str(user_id)+' '+heroe+'\n')
    archivo.close()
