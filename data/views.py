from django.shortcuts import render
from .models import Our_business, Our_products, Our_Team
# Create your views here.


def home_page(request):
    context = {
        'Our_business': Our_business.objects.all(),
        'Our_products': Our_products.objects.all()
    }
    return render(request, 'pages/home.html', context)


def Our_business_Page(request):
    context = {
        'Our_business': Our_business.objects.all()
    }
    return render(request, 'pages/our_business.html', context)


def Our_Product_Page(request):
    context = {
        'Our_products': Our_products.objects.all()
    }
    return render(request, 'pages/our_product.html', context)


def About_us_Page(request):
    context = {
        'Our_products': Our_products.objects.all(),
        'Our_team': Our_Team.objects.all()
    }
    return render(request, 'pages/aboutus.html', context)
