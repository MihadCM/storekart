from django.contrib import admin
from orders.models import Order, OrderedItem

class OrderAdmin(admin.ModelAdmin):
    list_filter = [
        'owner',
        'order_status',
        'created_at',
        'delete_status'
    ]
    search_fields = [
        'owner__user__username',
        'id',
        'order_status',
        'created_at',
        'updated_at',
        'delete_status'
    ]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedItem)

# Register your models here.
