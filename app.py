import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()
CITY = "Los Angeles"

def Kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = Kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = Kelvin_to_celsius_fahrenheit(feels_like_kelvin) 
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'])

print(f"Temperature in {CITY}: {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed} m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sun rises in {CITY}: {sunrise_time} UTC time.")
print(f"Sun sets in {CITY}: {sunset_time} UTC time.")
