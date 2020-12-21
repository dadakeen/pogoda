import datetime
import requests


while True:
    city = input()
    city_coords = requests.get(
        'http://search.maps.sputnik.ru/search/addr?',
        params={'q': city},
    )
    try:
        coords = city_coords.json()['result']['address'][0]['features'][0]['geometry']['geometries'][0]['coordinates']
        break
    except KeyError as e:
        print('Такого города нет, пожалуйста введите другой город')


time = int((datetime.datetime.now()
            .replace(hour=12, minute=0, second=0, microsecond=0) - datetime.timedelta(days=4))
           .timestamp())
for i in range(5):
    city_temp = requests.get(
        'https://api.openweathermap.org/data/2.5/onecall/timemachine?',
        params={'lat': coords[1], 'lon': coords[0], 'dt': time, 'appid': 'e5611d5fdfc09f51f3516bbdb88b84cf'}
    )
    temp = city_temp.json()
    print(datetime.datetime.fromtimestamp(temp['current']['dt']).strftime('%d.%m.%Y'), ': ',
          round(temp['current']['temp'] - 273.15, 1), '°C', sep='')
    time = int((datetime.datetime.fromtimestamp(time) + datetime.timedelta(days=1)).timestamp())
