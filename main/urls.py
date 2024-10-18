from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('blogs/',blogs,name='blogsingle'),
    path('blog/',blog,name='blog'),
    path('cart',cart,name='cart'),
    path('checkout/',checkout,name='checkout'),
    path('contact',contact,name='contact'),
    path('product/<int:id>/',product,name='product'),
    path('shop',shop,name='shop'),
    path('login',log_in,name='log_in'),
    path('reegister',signup,name='signup'),
    path('log_out',log_out,name='log_out'),
    path('profile/',customer_profile,name='customer_profile'),
    path('cart/add/<int:id>/',cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/',item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',item_decrement, name='item_decrement'),
    path('cart/cart_clear/',cart_clear, name='cart_clear'),
    path('cart/cart-detail/',cart_detail,name='cart_detail'),


]
