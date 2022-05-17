from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
# special object from Django to generate a search query
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    # query set to none to avoid errors when loading a page without any query
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        if 'category' in request.GET:
            # checking if category parameter is passed in the url
            """
            Double underscore syntax is common when making queries in django.
            Using it here means we're looking for the name field of the category model.
            And we're able to do this because category and product are related with a foreign key.
            """
            categories = request.GET['category'].split(',')

            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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

    # return the current sorting methodology to the template; both the sort and the direction variables stored -> do that with string formatting.
    current_sorting = f'{sort}_{direction}'

    # context - to send data back to the template, here products from model are available in the template
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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