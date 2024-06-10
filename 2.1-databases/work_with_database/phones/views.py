from .models import Phone
from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    field_sort=request.GET.get('sort')
    if field_sort is None:
        res = Phone.objects.all()
    else:
        if field_sort == 'min_price':
            res = Phone.objects.all().order_by('price')
        elif field_sort == 'max_price':
            res = Phone.objects.all().order_by('-price')
        else:
            res = Phone.objects.all().order_by('name')

    context = {'phones': res}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
