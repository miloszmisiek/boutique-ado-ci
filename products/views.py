from django.shortcuts import get_object_or_404, render
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

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    # context - to send data back to the template, here products from model are available in the template
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)