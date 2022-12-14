# ////////// Third module //////////
# ////////// Action Fulfillment //////////
# ////////// Calling Weather API //////////

# OpenWeather API: https://openweathermap.org/
# https://youtu.be/lcWfSn6-m_8

import requests

def action_weather_API(cityName):
    api_address = "http://api.openweathermap.org/data/2.5/weather?APPID=12a70ca7649269afee4eccb88387765c&q="
    
    url = api_address + cityName

    json_data = requests.get(url).json()
    #print(json_data)
    weather, temperature = json_data["weather"][0]["main"], (round(json_data["main"]["temp"]-273.15, 0))
    return weather, temperature
    

def action_dispatcher (intent, slots):
    if intent == "Weather" :
        return action_weather_API(slots)