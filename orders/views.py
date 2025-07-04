from django.shortcuts import render, redirect
from . models import Order, OrderedItem
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj,created = Order.objects.get_or_create(owner=customer, order_status=Order.CART_STAGE)
    context = {'cart': cart_obj}
    return render(request, 'cart.html', context)

@login_required(login_url='account')
def view_orders(request):
    user = request.user
    customer = user.customer_profile
    all_orders = Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context = {'orders': all_orders}
    return render(request, 'orders.html', context)

def remove_from_cart(request, pk):
    item = OrderedItem.objects.get(pk=pk)
    item.delete()
    return redirect('cart')

def checkout_cart(request):
    # Logic to add an item to the cart
    if request.POST:
        try:
            user = request.user
            customer = user.customer_profile
            # Assuming you have a customer profile linked to the user
            total = float(request.POST.get('total'))
            product_id = request.POST.get('product_id') 
            order_obj = Order.objects.get(owner=customer, order_status=Order.CART_STAGE)
            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.save()
                status = 'Order Confirmed Your order will be delivered within 2-3 days'
                messages.success(request, status)
            else:
                status = 'No items in the cart'
                messages.error(request, status)

        except Exception as e:
            status = 'Error in processing your order'
            messages.error(request, status)
        return redirect('orders')
    

@login_required(login_url='account')
def add_to_cart(request):
    # Logic to add an item to the cart
    if request.POST:
        user = request.user
        customer = user.customer_profile
        # Assuming you have a customer profile linked to the user
        quantity = int(request.POST.get('quantity'))
        
        product_id = request.POST.get('product_id') 

        cart_obj,created = Order.objects.get_or_create(owner=customer, order_status=Order.CART_STAGE)
        product = Product.objects.get(pk=product_id)
        ordered_item,created = OrderedItem.objects.get_or_create(product=product, owner=cart_obj)
        if created:
            ordered_item.quantity = quantity
            ordered_item.save()
        else:
            ordered_item.quantity += quantity
            ordered_item.save()
        return redirect('cart')
