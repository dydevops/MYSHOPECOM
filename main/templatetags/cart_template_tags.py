from django import template
from main.models import Order

register=template.Library()

@register.filter
def cart_items_count(user):
    if user.is_authenticated:
        query=Order.objects.filter(user=user, ordered=False)
        if query.exists():
            return query[0].items.count()
    return 0