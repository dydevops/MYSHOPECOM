from django.contrib import admin
from .models import*
# Register your models here.



admin.site.register(Item)
admin.site.register(Refund)
admin.site.register(Address)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Coupon)