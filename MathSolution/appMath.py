from flask import Flask, request
from flask_restful import Resource, Api
import re


app = Flask(__name__)
api = Api(app)

pairing = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def getID(placa):
    if not len(placa) == 7:
        return "Error, tamaño inválido"
    if not placa[0:4].isalpha():
        return "Error, formato incorrecto"
    if not placa[4::].isdigit():
        return "Error, formato incorrecto"
    placa = placa.upper()
    if placa[0] in pairing:
        k = pairing[placa[0]]
    else:
        return "Error, formato incorrecto"
    if placa[1] in pairing:
        l = pairing[placa[1]]
    else:
        return "Error, formato incorrecto"
    if placa[2] in pairing:
        x = pairing[placa[2]]
    else:
        return "Error, formato incorrecto"
    if placa[3] in pairing:
        y = pairing[placa[3]]
    else:
        return "Error, formato incorrecto"
    n = int(placa[4::])
    ecu = ((k-1)*(26**3) + (l-1)*(26**2) + (x-1)*(26) + (y-1))*(10**3) + n + 1
    return ecu

def getPlaca(id):
    if id > 456976000 or id < 0:
        return "id fuera de rango"
    k = (id//((26**3)*(10**3))) + 1
    id = id % ((26**3)*(10**3))
    l = (id//((26**2)*(10**3))) + 1
    id = id % ((26**2)*(10**3))
    x = (id//((26)*(10**3))) + 1
    id = id % ((26)*(10**3))
    y = (id//(10**3)) + 1
    id = id % (10**3)
    n = id-1
    k1 = k
    l1 = l
    x1 = x
    y1 = y
    if n == -1:
        if(k1!=1):
            k -= 1
            l = 26
            x = 26
            y = 26
            n = 999
        elif(l1!=1):
            l -= 1
            x = 26
            y = 26
            n = 999
        elif(x1!=1):
            x -= 1
            y = 26
            n = 999
        elif(y1!=1):
            y -= 1
            n = 999
    if n<10:
        n = '00' + str(n)
    elif n<100:
        n = '0' + str(n)
    else:
        n = str(n)
    
    return get_key(k) + get_key(l) + get_key(x) + get_key(y) + n

def get_key(val):
    for key, value in pairing.items():
        if val == value:
            return key
    return "key doesn't exist"

class GetPosition(Resource):
    def get(self,patent):
        return getID(patent)

class GetPatent(Resource):
    def get(self,id):
        if not id.isdigit():
            return "id inválido"
        id = int(id)
        return getPlaca(id)

api.add_resource(GetPosition, "/position/<string:patent>")
api.add_resource(GetPatent, "/patent/<string:id>")

if __name__ == "__main__":
    app.run(debug=True)