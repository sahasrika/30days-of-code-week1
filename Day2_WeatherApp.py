# Day2_WeatherApp.py
import requests

city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=%C+%t+%h"  # Simple free endpoint

try:
    res = requests.get(url)
    if res.status_code == 200:
        print(f"Weather in {city}: {res.text}")
    else:
        print("Couldn’t fetch weather details, try again later.")
except Exception as e:
    print("Error:", e)
