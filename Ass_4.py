# Assignment 4:

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup.find_all('span')        # Lista con todas las span tags??
spantags=list()
fspantags=list()

for span in spans:
    spantag=span.text                # Saco el texto que hay en las span tags
    spantags.append(spantag)         # Agrego cada spantag a la lista vacia que cree spantags.
#print(spantags)                     # spantags ahora es una lista con todos los numeritos str type.
for item in spantags:            # Convierto cada iten de spantags a floats
    fspantag=float(item)
    fspantags.append(fspantag)

print(fspantags)
total=sum(fspantags)
print('Suma:', total)
