import os
import requests
import datetime

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")

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
data = response.json()
daily_exercises = data['exercises']

sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/workoutTracking/workouts"
auth_header = {
    "Authorization": os.environ.get("AUTH_HEADER")
}
current_date = datetime.datetime.now()

for exercise in daily_exercises:
    payload = {
        "workout": {
            "date": current_date.strftime("%d/%m/%Y"),
            "time": current_date.strftime("%X"),
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    print(payload)
    sheety_response = requests.post(url=sheety_endpoint, json=payload, headers=auth_header)
    print(sheety_response.text)