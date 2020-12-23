# Assignment 2:     Data.txt

import re
hand=open('Data.txt')
numlist=list()

for line in hand:
    line=line.rstrip()
    num=re.findall('[0-9]+',line)   # num es una lista de numeros encontrados en cada linea
    if len(num)<1: continue         # no tengo en cuenta lineas vacias
    for item in num:                # Tengo que convertir cada item de la lista num a float, por separado
        fnum=float(item)
        numlist.append(fnum)

#print(numlist)
total=sum(numlist)
print(total)
