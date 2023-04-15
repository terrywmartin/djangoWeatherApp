from django.shortcuts import render
from django.views import View

from .utils import get_geocode_lon_lat, get_weather, get_forecast

# Create your views here.

class ForecastGetWeather(View):

    def post(self, request):
        zip_code = request.POST.get('zip', None)

        if zip_code == None:
            return render(request, 'partials/failure.html', { 'msg': 'Please enter a Zip Code.'})
        
        name, lat, lon = get_geocode_lon_lat(zip_code, 'US')
        current = get_weather(lat, lon)
        forecasts = get_forecast(lat,lon)

        context = {
            'current': current,
            'forecasts': forecasts
        }
        return render(request, 'forecast/partials/weather.html', context)
