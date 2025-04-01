
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})
def primary(request):
    return render(request, 'main/primary.html')
