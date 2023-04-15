from django.urls import path

from . import views

app_name = 'forecast'

urlpatterns = [
    path('forecast', views.ForecastGetForecast.as_view(),name='get_forecast'),
    path('weather', views.ForecastGetWeather.as_view(),name='get_weather'),
    path('geocode', views.ForecastGetGeocode.as_view(),name='get_geocode'),

    
]