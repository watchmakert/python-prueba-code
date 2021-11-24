import requests

BASE = "http://127.0.0.1:5000/"

patente= input("Dame una patente y retornaré la posición que pertenece: ")
id= input("Dame un id y retornaré una patente: ")

response = requests.get(BASE + "position/"+patente)
response2 = requests.get(BASE + "patent/"+id)

print(response.json())
print(response2.json())