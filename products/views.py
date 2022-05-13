from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    # context - to send data back to the template, here products from model are available in the template
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)