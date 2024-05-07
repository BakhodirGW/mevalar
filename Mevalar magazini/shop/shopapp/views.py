from django.shortcuts import render
from .models import *


def home_page(request):
    return render(request, 'shopapp/index.html')



def chizma(request):
    
    return render(request, "shopapp/chizma.html")

def sent_message(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']

    sent_message_info = Notification(name=name, email=email, phone=phone, message=message)
    sent_message_info.save()
    return render(request, 'shopapp/index.html')


def home_page(request):
    category = Category.objects.all()
    if request.method == 'POST' and request.POST.get('category_id'):
        products = Product.objects.filter(category=request.POST.get('category_id'))
    else:
        category = Category.objects.all()
    products = Product.objects.all()
    context = {
        'products' : products,
        'categories': Category.objects.all()
    }
    return render(request, 'shopapp/index.html', context)