from django.shortcuts import render
from .models import Product


def shop_info():
    return {
        'shop_name': 'Balaji Kirana Store',
        'phone': '9752430891',
        'whatsapp': '9752430891',
        'opening_time': '7:00 AM',
        'closing_time': '9:00 PM',
        'weekly_holiday': 'Open Daily',
        'google_maps_url': 'https://maps.app.goo.gl/E84BkyP67rjcjjfXA',
    }


def home(request):
    products = Product.objects.filter(
        is_featured=True
    )[:3]

    context = {
        'products': products,
        **shop_info(),
    }

    return render(
        request,
        'home.html',
        context
    )


def products(request):
    product_list = Product.objects.filter(
        is_featured=True
    )

    context = {
        'products': product_list,
        **shop_info(),
    }

    return render(
        request,
        'products.html',
        context
    )
def about(request):
    context = shop_info()
    return render(request, 'about.html', context)


def contact(request):
    context = shop_info()

    return render(
        request,
        'contact.html',
        context
    )