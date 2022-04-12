import requests

url = "https://webhook.site/"
payload = {"plato": "pasta", "cantidad": 2}
query_params = {"nombre": "Paco"}
response = requests.post(url, data=payload, params=query_params)
