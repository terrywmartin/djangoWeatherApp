# Display current weather and 5 day forecast

This is a simple app that displays current weather and a 5 day forecast from OpenWeather.  The app will look up a zip code using OpenWeathers Geocode API then look up the current weather and forecast.  To run this project, you'll need to sign up for an API key on OpenWeather.org.  It uses the Current Weather Data and 5 Day / 3 Hour Forecast APIs.

This project uses Django and HTMx.  
 
## To run the project

Create your virtual environment using the method of you choice.  I use venv.

You'll need to create an .env file with the following:

```
SECRETY_KEY=

API_KEY=

WEATHER_URL="https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={api_key}"
FORECAST_URL="https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=imperial&appid={api_key}"
GEOCODE_URL="http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"
ICON_URL="http://openweathermap.org/img/wn/"

```
You'll need to generate a secret key.

For example:

```
python -c "import secrets; print(secrets.token_urlsafe())"
```

Install dependencies in your virtual environment.

```
pip install -r requirements.txt
```

Run the project.

```
py manage.py runserver
```
