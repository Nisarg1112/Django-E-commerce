import json
from celery import shared_task
import sys
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

sys.path.append('..')
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact_Message
from django.template import RequestContext
from product.models import Brand
from product.models import Category, Product, Image
from order.models import ShopCart, OrderForm, Order, OrderProduct
from .forms import SearchForm
from user.models import UserProfile
from user.forms import SignUpForm
from time import sleep


@shared_task()
def sleepy(duration):
    sleep(duration)
    return None


# Create your views here.
def index(request):
    sleepy.delay(30)
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:3]
    products_best_sellers = Product.objects.all().order_by('-id')
    products_recommend = Product.objects.all().order_by('?')
    category = Category.objects.all()
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1
    grand_total = total + (total * 0.18)

    context = {'category': category,
               'products_slider': products_slider,
               'products_best_sellers': products_best_sellers,
               'products_recommend': products_recommend,
               'total': total,
               'count': count}
    return render(request, 'shop/index.html', context)


def get_brand(request):
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:3]
    products_best_sellers = Product.objects.all().order_by('-id')
    products_recommend = Product.objects.all().order_by('?')
    category = Category.objects.all()
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1

    context = {'category': category,
               'products_slider': products_slider,
               'products_best_sellers': products_best_sellers,
               'products_recommend': products_recommend,
               'total': total,
               'count': count, 'product': product}
    return render(request, 'shop/index.html', context)


# Create your views here.
def home(request):
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:3]
    products_best_sellers = Product.objects.all().order_by('-id')
    products_recommend = Product.objects.all().order_by('?')
    category = Category.objects.all()
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1

    context = {'category': category,
               'products_slider': products_slider,
               'products_best_sellers': products_best_sellers,
               'products_recommend': products_recommend,
               'total': total,
               'count': count, 'product': product}
    return render(request, 'shop/index.html', context)


def about(request):
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:3]
    products_best_sellers = Product.objects.all().order_by('-id')
    products_recommend = Product.objects.all().order_by('?')
    category = Category.objects.all()
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1

    context = {'category': category,
               'products_slider': products_slider,
               'products_best_sellers': products_best_sellers,
               'products_recommend': products_recommend,
               'total': total,
               'count': count, 'product': product}
    return render(request, 'shop/about-us.html', context)


def contact_us(request):
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:3]
    products_best_sellers = Product.objects.all().order_by('-id')
    products_recommend = Product.objects.all().order_by('?')
    category = Category.objects.all()
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1

    context = {'category': category,
               'products_slider': products_slider,
               'products_best_sellers': products_best_sellers,
               'products_recommend': products_recommend,
               'total': total,
               'count': count, 'product': product}
    return render(request, 'shop/contact.html', context)


def track(request):
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:3]
    products_best_sellers = Product.objects.all().order_by('-id')
    products_recommend = Product.objects.all().order_by('?')
    category = Category.objects.all()
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1

    context = {'category': category,
               'products_slider': products_slider,
               'products_best_sellers': products_best_sellers,
               'products_recommend': products_recommend,
               'total': total,
               'count': count, 'product': product}
    return render(request, 'shop/order-tracking.html', context)


def my_account(request):
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:3]
    products_best_sellers = Product.objects.all().order_by('-id')
    products_recommend = Product.objects.all().order_by('?')
    category = Category.objects.all()
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1

    context = {'category': category,
               'products_slider': products_slider,
               'products_best_sellers': products_best_sellers,
               'products_recommend': products_recommend,
               'total': total,
               'count': count, 'product': product}
    return render(request, 'shop/my-account.html', context)


def wishlist(request):
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:3]
    products_best_sellers = Product.objects.all().order_by('-id')
    products_recommend = Product.objects.all().order_by('?')
    category = Category.objects.all()
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1

    context = {'category': category,
               'products_slider': products_slider,
               'products_best_sellers': products_best_sellers,
               'products_recommend': products_recommend,
               'total': total,
               'count': count, 'product': product}
    return render(request, 'shop/wishlist.html', context)


def compare(request):
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:3]
    products_best_sellers = Product.objects.all().order_by('-id')
    products_recommend = Product.objects.all().order_by('?')
    category = Category.objects.all()
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1

    context = {'category': category,
               'products_slider': products_slider,
               'products_best_sellers': products_best_sellers,
               'products_recommend': products_recommend,
               'total': total,
               'count': count, 'product': product}
    return render(request, 'shop/compare.html', context)


def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            return HttpResponseRedirect('/')
        else:
            print('not')
            messages.warning(request, "Incorrect Username or Password entered!")
            return HttpResponseRedirect('/login')
    return render(request, 'shop/login-register.html')


def contact_submit(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    contact_message = Contact_Message(name=name, email=email, subject=subject, message=message)
    contact_message.save()
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:3]
    products_best_sellers = Product.objects.all().order_by('-id')
    products_recommend = Product.objects.all().order_by('?')
    category = Category.objects.all()
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1

    context = {'category': category,
               'products_slider': products_slider,
               'products_best_sellers': products_best_sellers,
               'products_recommend': products_recommend,
               'total': total,
               'count': count, 'product': product}
    return render(request, 'shop/contact.html', context)


def category_products(request, id, slug):
    products = Product.objects.filter(category_id=id)
    category = Category.objects.all()
    catdata = Category.objects.get(pk=id)
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1
    context = {'category': category,
               'products': products,
               'catdata': catdata,
               'total': total,
               'count': count, 'product': product
               }
    return render(request, 'shop/shop.html', context)


def search(request):
    category = Category.objects.all()
    catdata = Category.objects.get(pk=id)
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1

    context = {'category': category,
               'catdata': catdata,
               'total': total,
               'count': count, 'product': product
               }
    if request.method == 'POST':
        print('post')
        form = SearchForm(request.POST)
        print(form)
        if form.is_valid():
            query = form.cleaned_data['query']

            products = Product.objects.filter(title__icontains=query)

            context = {'products': products}
            print('form valid')

            return render(request, 'shop/search_products.html', context)
        else:
            print('not valid')
            return render(request, 'shop/index.html')
    else:
        print('request not recieved')
        return render(request, 'shop/search_products.html', context)


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        results = []
        for rs in products:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def product_detail(request, id, slug):
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    product = Product.objects.all()
    total = 0
    count = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
        count += 1
    product = Product.objects.get(pk=id)
    category = Category.objects.all()
    image = Image.objects.filter(product_id=id)
    context = {'category': category,
               'product': product,
               'image': image,
               'total': total,
               'count': count,
               }
    return render(request, 'shop/product_details.html', context)


def shopcart(request):
    category = Category.objects.all()
    print(category)
    current_user = request.user
    print(current_user)
    cart = ShopCart.objects.filter(user_id=current_user.id)
    print(cart)
    total = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
    print(total)

    grand_total = total + (total * 0.18)
    context = {
        'category': category,
        'shopcart': cart,
        'total': total,
        'grand_total': grand_total

    }
    return render(request, 'shop/cart.html', context)


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = r'C:\Users\Nisarg Trivedi\PycharmProjects\MyAwesomeCart\mac\shop\static\user.png'
            data.save()
            messages.success(request, 'Your Account Has Been Created')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')
    else:
        form = SignUpForm()

    return render(request, 'shop/signup.html', {'form': form})


@shared_task()
def order(request_):
    category = Category.objects.all()
    current_user = request_.user
    print(current_user)
    cart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
    print(total)
    grand_total = total + (total * 0.18)
    if request_.method == 'POST':
        print('post recived')
        form = OrderForm(request_.POST)
        print(form)
        if form.is_valid():
            print('valid')
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.country = form.cleaned_data['country']
            data.zip = form.cleaned_data['zip_code']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request_.META.get('REMOTE_ADDR')
            ordercode = get_random_string(7).upper()
            data.code = ordercode
            print(ordercode)
            data.save()

            shop_cart = ShopCart.objects.filter(user_id=current_user.id)
            total_cart = 0
            for rs in shop_cart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.price
                detail.amount = rs.amount
                total_cart += rs.amount
                print(detail.amount)
                detail.save()

                # reduce quantity of sold product from amount of product
                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()
            request_.session['cart_items'] = 0
            messages.success(request_, "Your Order Has Been Completed Successfully, Thank You!")

            send_mail('Your Order Has Been Received!',
                      'Thanks For Shopping With Us, Your order will be delivered in 5-6 working days! Your Order No. :' +
                      ordercode,
                      'Django_Ecommerce_web@gmail.com', ['nisargtrivedi054@gmail.com'], fail_silently=False
                      )
            print('mail sent')

            return render(request_, 'shop/order_completed.html', {'ordercode': ordercode, 'category': category})
    return None


@shared_task()
def send_mail_task(code):
    order_code = code
    print(order_code)
    send_mail('Your Order Has Been Received!',
              'Thanks For Shopping With Us, Your order will be delivered in 5-6 working days! Your Order No. :' +
              order_code,
              'Django_Ecommerce_web@gmail.com', ['nisargtrivedi054@gmail.com'], fail_silently=False
              )
    print('mail done')
    return None


def checkout(request):
    category = Category.objects.all()

    current_user = request.user
    print(current_user)
    cart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in cart:
        total += rs.product.price * rs.quantity
    print(total)
    grand_total = total + (total * 0.18)
    form = OrderForm()
    context = {
        'category': category,
        'shopcart': cart,
        'total': total,
        'grand_total': grand_total,
        'form': form

    }
    if request.method == 'POST':
        print('post recived')
        form = OrderForm(request.POST)
        print(form)
        if form.is_valid():
            print('valid')
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.country = form.cleaned_data['country']
            data.zip = form.cleaned_data['zip_code']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(7).upper()
            data.code = ordercode
            print(ordercode)
            data.save()

            shop_cart = ShopCart.objects.filter(user_id=current_user.id)
            total_cart = 0
            for rs in shop_cart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.price
                detail.amount = rs.amount
                total_cart += rs.amount
                print(detail.amount)
                detail.save()

                # reduce quantity of sold product from amount of product
                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Your Order Has Been Completed Successfully, Thank You!")

            send_mail_task.delay(ordercode)
            sleepy.delay(30)

            print('mail sent')

            return render(request, 'shop/order_completed.html', {'ordercode': ordercode, 'category': category})

    return render(request, 'shop/checkout.html', context)
