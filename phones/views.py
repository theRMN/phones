from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = list(Phone.objects.values())
    sort_by_name = list(Phone.objects.order_by('name').values())
    sort_by_min_price = list(Phone.objects.order_by('price').values())
    sort_by_max_price = Phone.objects.order_by('-price').values()

    if sort == 'name':
        context = {
            'phones': sort_by_name
        }
    elif sort == 'min_price':
        context = {
            'phones': sort_by_min_price
        }
    elif sort == 'max_price':
        context = {
            'phones': sort_by_max_price
        }
    elif not sort:
        context = {
            'phones': phones
        }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = list(Phone.objects.values())

    for phone in phones:
        if slug == phone['slug']:
            context = {
                'phone': phone
            }
    return render(request, template, context)



