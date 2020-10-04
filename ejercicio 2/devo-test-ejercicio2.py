from flask import Flask, render_template, request
from flask_cors import CORS
import json

import UtilDevo

my_app = Flask('app')
CORS(my_app)

@my_app.route('/datos_grafico1', methods=['GET'])
def datos_grafico1():
    if request.method == 'GET':
        datosByCatYFec = datos.groupby(['categoria','fecha'], sort=True).sum().reset_index()
        labels = datosByCatYFec['fecha'].unique().tolist()
        datosCat1 = datosByCatYFec[datosByCatYFec['categoria'] == 'CAT 1'].to_json(orient="split", index=False)        
        datosCat2 = datosByCatYFec[datosByCatYFec['categoria'] == 'CAT 2'].to_json(orient="split", index=False)        
        datosCat3 = datosByCatYFec[datosByCatYFec['categoria'] == 'CAT 3'].to_json(orient="split", index=False)        
        datosCat4 = datosByCatYFec[datosByCatYFec['categoria'] == 'CAT 4'].to_json(orient="split", index=False)        
        cat1 = json.loads(datosCat1)
        cat2 = json.loads(datosCat2)
        cat3 = json.loads(datosCat3)
        cat4 = json.loads(datosCat4)        
        resultado = {'labels':labels, 'cat1': cat1['data'], 'cat2': cat2['data'], 'cat3': cat3['data'], 'cat4': cat4['data']}
        return json.dumps(resultado)

@my_app.route('/datos_grafico2', methods=['GET'])
def datos_grafico2():
    if request.method == 'GET':
        return datos.groupby(['categoria'], sort=True).sum().reset_index().to_json(orient="split", index=False)    

@my_app.route('/')
def inicio():
    return render_template('graficas.html')

if __name__ == '__main__':   
    datos = UtilDevo.obtenerDatos()
    my_app.run("localhost", "9999", debug=True)
