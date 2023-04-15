import requests
import os
from datetime import datetime


def get_geocode_lon_lat(zip_code, country_code):

    geocode_url = os.getenv('GEOCODE_URL')

    API_KEY = os.getenv('API_KEY')    
    full_url = str.format(geocode_url,zip_code=zip_code,country_code=country_code,api_key=API_KEY)
    
    response = requests.get(full_url).json()

    return response['name'], response['lat'], response['lon']

def get_weather(lat, lon):
    
    weather_url = os.getenv('WEATHER_URL')
    API_KEY = os.getenv('API_KEY')
    
    full_url = str.format(weather_url, lat=lat, lon=lon, api_key=API_KEY)
    ICON_URL = os.getenv('ICON_URL')
    icon_size_modifiers = [ "@2x.png", "@4x.png" ]

    response = requests.get(full_url).json()

    current = {
            'name': response['name'],
            'temp': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': ICON_URL + response['weather'][0]['icon'] + icon_size_modifiers[1]
        }
    return current

def get_forecast(lat, lon):
    forecast_url = os.getenv('FORECAST_URL')
    API_KEY = os.getenv('API_KEY')
    
    full_url = str.format(forecast_url, lat=lat, lon=lon, api_key=API_KEY)
    ICON_URL = os.getenv('ICON_URL')
    icon_size_modifiers = [ "@2x.png", "@4x.png" ]
    response = requests.get(full_url).json()

    forecasts = []
    for day in response['list']:
        forecast = {
            "date": str(datetime.fromtimestamp(day['dt']).strftime('%m-%d-%Y  %H:%M:%S')),
            "high" : str(int(day['main']['temp_max'])),
            "low" : str(int(day['main']['temp_min'])),
            "main": day['weather'][0]['main'],
            "icon": ICON_URL + day['weather'][0]['icon'] + icon_size_modifiers[0]
        }
        forecasts.append(forecast)

    return forecasts