# WeatherInfo

WeatherInfo is a Python script that fetches weather information for a specified city using the OpenWeatherMap API.

## Usage
1. Ensure you have an API key for the OpenWeatherMap API. If not, sign up for a free account on their website to obtain the API key.
2. Save your API key in a file named `api_key` in the same directory as this script.
3. Replace the `CITY` variable with the name of the city for which you want to retrieve weather information.
4. Run the script.

## Requirements
- Python 3.x
- requests library (can be installed via pip: `pip install requests`)

## Features
- Retrieves current temperature in Celsius and Fahrenheit.
- Displays feels-like temperature in Celsius and Fahrenheit.
- Shows humidity percentage.
- Provides wind speed in meters per second.
- Gives general weather description.
- Shows sunrise and sunset times in UTC.

## Example
$ python WeatherInfo.py
Temperature in Los Angeles: 20.01C or 68.02F
Temperature in Los Angeles feels like: 21.67C or 71.01F
Humidity in Los Angeles: 75%
Wind Speed in Los Angeles: 4.63 m/s
General Weather in Los Angeles: clear sky
Sun rises in Los Angeles: 2024-05-15 12:55:35 UTC time.
Sun sets in Los Angeles: 2024-05-16 01:02:33 UTC time.
