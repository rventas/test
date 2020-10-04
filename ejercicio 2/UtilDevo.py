import pandas as pd
import time
import re
import json

def obtenerCat(txt):    
    x = re.search(r'#\w+ \d#', txt)
    return '' if x==None else txt[x.span()[0]+1:x.span()[1]-1]

def leerYTransformarDatos1():
    data1 = pd.read_json('data1.json')
    data1.rename(columns={'cat':'categoria','d':'fecha','value': 'valor'}, inplace=True)
    data1['categoria'] = data1['categoria'].apply(lambda x:x.upper())
    data1['fecha'] = data1['fecha'].apply(lambda x: time.strftime('%Y-%m-%d', time.gmtime(x/1000.0)))
    
    return data1

def leerYTransformarDatos2():
    data2 = pd.read_json('data2.json')
    data2.rename(columns={'categ':'categoria','myDate':'fecha','val': 'valor'}, inplace=True)
    
    return data2

def leerYTransformarDatos3():
    data3 = pd.read_json('data3.json')
    data3['categoria'] = data3['raw'].apply(obtenerCat)
    data3['fecha'] = data3['raw'].apply(lambda x : re.findall(r'\d{4}-\d{2}-\d{2}', x)[0])
    data3.rename(columns={'val':'valor'}, inplace=True)
    data3.drop(['raw'], axis=1, inplace=True)
    
    return data3

def obtenerDatos():
    data1 = leerYTransformarDatos1()
    data2 = leerYTransformarDatos2()
    data3 = leerYTransformarDatos3()
    return pd.concat([data1, data2, data3], sort=True)


