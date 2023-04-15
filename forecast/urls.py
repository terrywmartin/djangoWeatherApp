from django.urls import path

from . import views

app_name = 'forecast'

urlpatterns = [
    path('weather', views.ForecastGetWeather.as_view(),name='get_weather'),

    
]