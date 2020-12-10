import sys
from django.contrib.auth.decorators import login_required

sys.path.append('..')

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import ShopCart, ShopCartForm


# Create your views here.
def index(request):
    return HttpResponse('Order Page')


@login_required(login_url='/login')
def addtoshopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user

    checkproduct = ShopCart.objects.filter(product_id=id)
    if checkproduct:
        control = 1
    else:
        control = 0

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(product_id=id)
                data.quantity = form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, 'Product added to ShopCart')
        return HttpResponseRedirect(url)

    else:
        if control == 1:
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        messages.success(request, "Product Added To Shop Cart")
        return HttpResponseRedirect(url)


@login_required(login_url='/login')
def deletefromshopcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, 'Item Successfully Deleted!')
    return HttpResponseRedirect('/shopcart')
