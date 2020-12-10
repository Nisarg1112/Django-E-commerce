"""mac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import sys

sys.path.append('..')
from django.urls import path
from . import views
from order import views as OrderViews

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('about-us/', views.about, name='AboutUs'),
    path('contact/', views.contact_us, name='contact_us'),
    path('tracker/', views.track, name='track'),
    path('checkout/', views.checkout, name='checkout'),
    path('addtoshopcart/', views.shopcart, name='shopcart'),
    path('my_account/', views.my_account, name='my_account'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('compare/', views.compare, name='compare'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_func, name='logout_func'),
    path('signup/', views.signup, name='signup'),
    path('contact_submit/', views.contact_submit, name='contact_submit'),
    path('home/', views.home, name='home'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
]
