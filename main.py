import os
import requests

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-key": API_KEY,
    "x-app-id": APP_ID,
    "x-remote-user-id": "0"
}

params = {
    "query": input("Please enter what exercise you did today: ")
}

response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
print(response.text)
