import requests


url = "https://jsonplaceholder.typicode.com/users"
    
resposta = requests.get(url)
print(resposta.text)
