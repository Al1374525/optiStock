from django.shortcuts import render
from .models import Stock
from .api_client import AlphaVantageClient

# Create your views here.
def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/stock_list.html', {'stocks': stocks})

def home(request):
    return render(request, 'home.html')


def stock_detail(request, symbol):
    client = AlphaVantageClient()
    data = client.get_daily_stock_data(symbol)
    return render(request, 'stocks/stock_detail.html', {'stock_data': data})  # ,