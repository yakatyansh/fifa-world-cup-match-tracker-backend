import requests

BASE_URL = "https://worldcup26.ir"

def get_teams():
    response = requests.get(f"{BASE_URL}/get/teams")
    return response.json()

def get_games():
    response = requests.get(f"{BASE_URL}/get/games")
    return response.json()

def get_stadiums():
    response = requests.get(f"{BASE_URL}/get/stadiums")
    return response.json()