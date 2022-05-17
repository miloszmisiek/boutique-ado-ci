""" This is context processor to handle shopping bag items,
    And its purpose is to make this dictionary available to all templates across the entire application,
    must be included in settings.py.
    
    This context concept is the same as the context we've been using in our views.
    The only difference is we're returning it directly and making it available to all templates by putting it in settings.py. """

from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        # using decimal is preferred when working with money because it's more accurate than float
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context