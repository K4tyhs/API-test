import requests
import json

url = "http://127.0.0.1:5000/matricula"

data = {
    'ra': '23011355',
    'nome': 'Katiely',
    'idade': '17'
}

response = requests.post(url, json=data)

print('StatusCode:', response.status_code)
print('Response Json:', response.json())