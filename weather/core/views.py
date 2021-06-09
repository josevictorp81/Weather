from django.shortcuts import render
import requests
from django.conf import settings

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=pt_br&appid={settings.OPEN_WEATHER_MAP_API_KEY}'
        
        result = requests.get(url=url).json()
        #print(result)
        weather = {
            'city': city,
            'temperature': result['main']['temp'],
            'description': result['weather'][0]['description'],
            'icon': result['weather'][0]['icon'],
            'place': result['sys']['country'],
        }

        data = {
            'weather': weather,
        }
        return render(request, 'index.html', data)
    else:
        return render(request, 'index.html')
