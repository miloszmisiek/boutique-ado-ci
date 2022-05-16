from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
# special object from Django to generate a search query
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    # query set to none to avoid errors when loading a page without any query
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # 'i' before 'contains' makes the queries case insensitive, and '|' (pipe) generates 'or' statement
            # IMPORTANT!! DOUBLE UNDERSCORE !!!
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # with queries constracted they can be used to filter products
            products = products.filter(queries) 

    # context - to send data back to the template, here products from model are available in the template
    context = {
        'products': products,
        'search_term': query,
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