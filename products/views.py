from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products
    }
    return render(request, 'index.html', context)

def list_products(request):
     
    product_list = Product.objects.order_by('priority')
    product_paginator = Paginator(product_list, 10)
    product_list = product_paginator.get_page(request.GET.get('page', 1))

    context = {
        'products': product_list
    }
    return render(request, 'product.html', context)


def detail_product(request,pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
        
    return render(request, 'product_detail.html', context)
