from django.db import models
from products.models import Product
from customers.models import Customer

# Orders.

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = (( LIVE, 'Live'), (DELETE, 'Delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3 
    ORDER_CANCELLED = 4
    STATUS_CHOICE = ( (ORDER_PROCESSED, 'Order Processed'), 
                      (ORDER_DELIVERED, 'Order Delivered'), 
                      (ORDER_CANCELLED, 'Order Cancelled'))
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    total_price = models.FloatField(default=0.0)


    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')


    delete_status = models.IntegerField(choices=DELETE_CHOICE, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.owner:
            return 'order-{}-{}'.format(self.id, self.owner.user.username)
        else:
            return 'order-{}-No Owner'.format(self.id)


class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')



