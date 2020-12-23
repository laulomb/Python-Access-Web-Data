# Assignment 6:  Extracting Data from JSON

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter U.R.L:')
html = urllib.request.urlopen(url, context=ctx).read()     # Para manejar url y leerlo y poder  manejarlo como un archivo.

info = json.loads(html)       # info es un diccionario con 2 key-value pairs.
#print('Info:', info)
Comments=info['comments']     # Comments es una lista, de diccionarios, estos tienen key-value pairs: {'name':pepe,'count':12}
#print('Comments:', Comments)
#print('Length Comments:', len(Comments))   # La lista Comments tiene 50 items=50 diccionarios.

countlist=list()
for d in Comments:     # Variable d itinera por la lista de diccionarios
    counts=d['count']  # Guardo en la variable counts los value de la key ['count'] de cada diccionario d.
    countlist.append(counts)     # Los appendeo en la lista vacia creada anteriormente: countlist.
    #print(counts)
    #print(type(counts))
print('Suma Counts', sum(countlist))
