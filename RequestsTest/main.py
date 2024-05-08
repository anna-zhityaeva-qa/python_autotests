import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '2348086b01d496d3444435d1add5e4c6' 
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "anna1.zhityaeva@yandex.ru",
    "password": "Iloveqa1"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Булка",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change = {
    "trainer_token": TOKEN,
    "pokemon_id": "26291",
    "name": "Батон",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_catch = {
    "trainer_token": TOKEN,
    "pokemon_id": "26291"
}


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)