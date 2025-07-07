import os

from dotenv import load_dotenv

load_dotenv()
import requests


def weather_city(city):
    api_key_weather = os.getenv("api_key_weather")
    request_city = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key_weather}&units=metric'
    result = requests.get(request_city)
    weather = dict(result.json())
    return round(weather.get('main').get('temp_min'))


def exchange_rate(currency):  # currency -> rub, usd, eur

    api_key_currency = os.getenv("api_key_currency")  # фильтр по валюте
    request_currency = f'https://api.minfin.com.ua/summary/{api_key_currency}'
    result = requests.get(request_currency)

    data = {'usd': {'bid': '41.3250', 'ask': '41.9000', 'trendAsk': 0.049999999999997, 'trendBid': 0.025000000000006},
            'eur': {'bid': '45.1000', 'ask': '45.7000', 'trendAsk': 0, 'trendBid': 0},
            'rub': {'bid': '0.3000', 'ask': '0.4500', 'trendAsk': 0, 'trendBid': 0},
            }
    bid = round(float(data.get(currency).get('bid')), 2)
    ask = round(float(data.get(currency).get('ask')), 2)
    return f'покупка: {bid}, продажа: {ask}'


print(exchange_rate('eur'))


def coin_gecko(coin):
    currency = 'usd'
    api_key_gecko = os.getenv("api_key_gecko")
    request_url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies{currency}'

    params = {
        'accept': 'application/yaml',
        'x-cg-demo-api-key': api_key_gecko,
        'vs_currencies': 'usd'
    }
    response = requests.get(request_url, params=params)
    return response.json()

# print(coin_gecko('tether'))
