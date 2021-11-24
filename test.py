import requests

BASE = "http://127.0.0.1:5000/"

print('\n')
print('---------------START---------------\n')
patente= input("Dame una patente y retornaré la posición que pertenece: ")
print('\n')
response = requests.get(BASE + "position/"+patente)
print(response.json())
print('\n')
print('----------------------------------------\n')

id= input("Dame un id y retornaré una patente: ")
print('\n')
response2 = requests.get(BASE + "patent/"+id)
print(response2.json())
print('\n---------------END---------------\n')