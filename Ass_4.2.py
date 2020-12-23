# Assignment 4.2:

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url18 = input('Enter - ')
html = urllib.request.urlopen(url18, context=ctx).read()

count=0
while count<7:      # De 0 a 6 tengo 7 veces.
    soup = BeautifulSoup(html, 'html.parser')
    anchortags = soup('a')        # Lista de anchor tags:[<a href="http://py4e-data.dr-chuck.net/known_by_Cecilia.html">Cecilia</a>,..etc..]
    anchor18 = anchortags[17]
    href18 = anchor18.get('href', None)    # El .get() es un metodo para una variable.
    html = urllib.request.urlopen(href18, context=ctx).read()
    count = count + 1
    print('count:', count)
    print('url18:', href18)

print('last-url18:', href18)
