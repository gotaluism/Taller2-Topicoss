from flask import Flask, jsonify, request, render_template
import random
import os
from pokeneas import lista_pokeneas

app = Flask(__name__)

@app.route('/json')
def archivoJson():
    pokenea_aleatorio=random.choice(lista_pokeneas) 
    container_id = os.getenv("HOSTNAME", "local")  
    #return render_template('datos.html',id=pokenea_aleatorio["id"],nombre=pokenea_aleatorio["nombre"],altura=pokenea_aleatorio["altura"],habilidad=pokenea_aleatorio["habilidad"])
    return jsonify( {
    "id": pokenea_aleatorio["id"],
    "nombre": pokenea_aleatorio["nombre"],
    "altura": pokenea_aleatorio["altura"],
    "habilidad": pokenea_aleatorio["habilidad"],
    "container_id": container_id
    })
    
@app.route('/img')
def imagen():
    pokenea_aleatorio=random.choice(lista_pokeneas)
    container_id = os.getenv("HOSTNAME", "local")
    return render_template('image.html', image=pokenea_aleatorio["imagen"], phrase=pokenea_aleatorio["frase_filosofica"], container_id=container_id)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    