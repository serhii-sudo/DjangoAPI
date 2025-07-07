from django.urls import path

from data.views import Main, Weather, WeatherResult, Currency, GetCurrency, CoinGecko, GetGeckoCoin

urlpatterns = [
    path('', Main.as_view(), name='home'),
    path('weather/', Weather.as_view(), name='weather'),
    path('weather-result/', WeatherResult.as_view(), name='weather-result'),
    path('currency/', Currency.as_view(), name='currency'),
    path('currency-today/', GetCurrency.as_view(), name='currency-today'),
    path('coin/', CoinGecko.as_view(), name='coin'),
    path('coin-today/', GetGeckoCoin.as_view(), name='coin-today')
]
