import requests

BASE = "http://127.0.0.1:5000/"

id= input("Dame un id y retornaré una posicion: ")
patente= input("Dame una posicion y retornaré la placa que pertenece: ")
response = requests.get(BASE + "position/"+id)
response2 = requests.get(BASE + "patent/"+patente)

print(response.json())
print(response2.json())