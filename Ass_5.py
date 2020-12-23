# Assignment 5: url con un XML-'arbol'

import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET    # Para manejar formato XML


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter U.R.L:')
html = urllib.request.urlopen(url, context=ctx).read()     # Para manejar url y leerlo y poder  manejarlo como un archivo.
tree = ET.fromstring(html)       # Convierte a una "gran string" la informacion que leyo de la variable html.

Countlist = tree.findall('.//count')    # Busca todas las tags del formato XML llamadas count, y las pone en la lista Countlist
#print('COUNT LIST:', Countlist)
countlist = list()
for count in Countlist:       # Itinera por cada elemento de la lista Countlist
    count = count.text        # y les saca el texto,
    fcount = float(count)     # y lo convierte a float
    countlist.append(fcount)  # y lo agrego a la lista vacia que cree antes, countlist

print('Count:', countlist)    # Lista con elementos numericos, sacados del texto de las count tags del formato XML. 
print('Suma Counts:', sum(countlist))
