from numbers import Real
from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_Date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)

def about(request):
    mvps = Realtor.objects.all().filter(is_mvp=True)

    realtors = Realtor.objects.order_by('-hire_date')

    context = {
        'mvps': mvps,
        'realtors': realtors
    }

    return render(request, 'pages/about.html', context)

# def listings(request):
#     return render(request, 'pages/listings.html')