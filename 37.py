import requests

city = input(' - Город, в котором интересует температура?\n - ')
api_url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': city
    , 'appid': '11c0d3dc6093f7442898ee49d2430d20'
    , 'units': 'metric'
    , 'lang': 'ru'
}
try:
    res = requests.get(api_url, params).json()
    print(f" - Сейчас в городе {str.title(city)} {round(res['main']['temp'])}*С,"
          f" по ощущениям {round(res['main']['feels_like'])}*С.")
    print(f"   Давление {round(res['main']['pressure'] * .750063783)} мм.рт.ст, влажность {res['main']['humidity']}%. "
          f"{str.title(res['weather'][0]['description'])}")
except KeyError as e:
    print(f'Сожалею, по городу {str.title(city)} нет данных(\n\n', e)

'''Вывод погоды с сайта openweathermap.org через api'''
