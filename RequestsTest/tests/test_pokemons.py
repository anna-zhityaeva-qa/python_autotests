import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '2348086b01d496d3444435d1add5e4c6' 
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '3973'
TRAINER_NAME = 'Ann'

def test_status_codte():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200
    
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Булка'
    
def test_part_id_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_id"] == TRAINER_ID
    
def test_part_name_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_name': TRAINER_NAME})
    assert response_get.json()["data"][0]["trainer_name"] == TRAINER_NAME