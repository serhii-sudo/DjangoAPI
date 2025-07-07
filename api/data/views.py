from django.shortcuts import render

from django.views import View

from django.core.cache import cache

from data.data_api import weather_city, exchange_rate, coin_gecko


# высокоуровневое кэширование

class Main(View):
    template_name = 'data/home.html'

    # @method_decorator(cache_page(10))
    def get(self, request):
        return render(request, self.template_name)


class Weather(View):
    template_name = 'data/weather.html'

    def get(self, request):
        return render(request, self.template_name)


class WeatherResult(View):
    template_name = 'data/weather-result.html'

    def post(self, request):
        city = request.POST.get('item_text')
        result = weather_city(city)
        cache_page = cache.get(f'{city}_weather')
        if cache_page:
            return cache_page
        response = render(
            request,
             self.template_name,
            {'city': city, 'result': result}
        )
        cache.set(f'{city}_weather', response, 100)
        return response


class Currency(View):
    template_name = 'data/currency.html'

    def get(self, request):
        return render(request, self.template_name)


class GetCurrency(View):
    template_name = 'data/currency_today.html'

    def post(self, request):
        currency = request.POST.get('currency')
        result = exchange_rate(currency)
        print(result)
        currency_cache = cache.get(currency)
        print(currency_cache)
        if currency_cache:
            print(f'взято из кэша {currency_cache}')
            return currency_cache

        response = render(request,
                          self.template_name,
                          {'currency': currency, 'result': result})
        cache.set(currency, response, 100)
        return response


class CoinGecko(View):
    template_name = 'data/coin.html'

    def get(self, request):
        return render(request, self.template_name)


class GetGeckoCoin(View):
    template_name = 'data/coin_result.html'

    def post(self, request):
        result_coin = request.POST.get('coin')
        currency_coin = list(coin_gecko(result_coin).values())[0]['usd']
        gecko_cache = cache.get(result_coin)
        print(gecko_cache)
        if gecko_cache:
            return gecko_cache

        response = render(request,
                          self.template_name, {'gecko': currency_coin,
                                               'crypto_coin': result_coin})
        cache.set(result_coin, response, 45)
        return response
