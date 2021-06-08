from django.shortcuts import render
import requests
from django.conf import settings

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        #country = request.POST['country']

        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPEN_WEATHER_MAP_API_KEY}'
        

        result = requests.get(url=url)
        print(result.json())
    return render(request, 'index.html')
