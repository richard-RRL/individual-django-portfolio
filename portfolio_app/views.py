from django.shortcuts import render
from .models import Portfolio
# Create your views here.

def index(request):
    # return render(request, 'portfolio_app/index.html')
    # Retrieve active portfolios
    active_portfolios = Portfolio.objects.filter(
        is_active = True
    )
    return render(
        request,
        'portfolio_app/index.html',
        {'active_portfolios': active_portfolios}
    )