from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Customer 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                email = request.POST.get('email')
                address = request.POST.get('address')
                phone = request.POST.get('phone')
                #create user acoount
                user = User.objects.create_user(username=username, password=password, email=email)
                #create customer profile
                customer = Customer.objects.create(user=user, address=address, phone=phone)
                success_message = "User registered successfully"
                messages.success(request, success_message)
        except Exception as e:
            error_message = "Duplicate Username or Email"
            messages.error(request, error_message)


    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
             login(request, user)
             return redirect('products_list/')
        else:
             messages.error(request, 'invalid user credential')
        
    return render(request, 'account.html', context)


def sign_out(request):
    logout(request)
    return redirect('account') 
