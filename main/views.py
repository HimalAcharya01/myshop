from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Product,Category,Profile,Brand,Review,Order
from django.core.paginator import Paginator
from .forms import ProfileUpdateForm,ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
# Create your views here.
def index(request):
    product=Product.objects.all()
    Cate=Category.objects.all()
    brand=Brand.objects.all()
    
    cateid=request.GET.get('category')
    if cateid:
        product=Product.objects.filter(Subcategory=cateid)
    else:
        product=Product.objects.all()
    paginator=Paginator(product,3)
    num_page=request.GET.get('page')
    data=paginator.get_page(num_page)
    total=data.paginator.num_pages
    contex={
        'product':product,
        'cate':Cate,
        'data':data,
        'num':[i+1 for i in range(total)],
        'brand':brand,
        
                }
    return render(request,'main/index.html',contex)
def shop(request):
    return render(request,'main/shop.html')
def cart(request):
    return render(request,'main/cart.html')
def product(request,id):
    product=get_object_or_404(Product,id=id)
    products=Product.objects.filter(Category=product.Category).exclude(id=id)
    cmt_all=request.GET.get('cmt_all')
    if cmt_all:
        reviews=product.reviews.all()
    else:
        reviews=product.reviews.all()[:3]
    
    form=ReviewForm()
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.product=product
            review.user=request.user
            review.save()
    contex={
        'product':product,
        "products":products,
        'form':form,
        'reviews':reviews,
        'cmt_all':cmt_all,
        'range':range(1,6)

    }
    
    return render(request,'main/product-details.html',contex)
def contact(request):
    return render(request,'main/contact-us.html')
def checkout(request):
    if request.method=='POST':
        phone=request.POST['phone']
        address=request.POST['address']
        cart=request.session.get('cart')
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(pk=uid)
        print(cart)
        for i in cart:
            a=cart[i]['price']
            b=cart[i]['quantity']
            total=float(a)*b

            order=Order(
                product=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                total=total,
                user=user,
                image=cart[i]['image'],
                phone=phone,
                address=address

            )
            order.save()
            request.session['cart']={}
    return redirect('index')
def blog(request):
    return render(request,'main/blog.html')
def blogs(request):
    return render(request,'main/blog-single.html')
def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'your password or email is incorrect')
            return redirect('log_in')
    return render(request,'auth/login.html')
def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password1==password:
            if User.objects.filter(email=email).exists():
                messages.error(request,'your email is already register ')
            elif User.objects.filter(username=name).exists():
                messages.error(request,'your username is already taken ')
            else:
                User.objects.create_user(first_name=fname,last_name=lname,username=name,email=email,password=password)
                return redirect('log_in')
        else:
            messages.error(request,'your pasword does not matches')
            return redirect('signup')

    return render(request,'auth/register.html')
def log_out(request):
    pass

@login_required(login_url='log_in')
def customer_profile(request):
    profile,created=Profile.objects.get_or_create(user=request.user)
    profile_form=ProfileUpdateForm(instance=profile)
    if request.method=='POST':
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('customer_profile')

    contex={
        'profile_form':profile_form,
        'user':request.user,
        'profile':request.user.profile
    }
    return render(request,'main/customer_profile.html',contex)
'''
--------------------->>>>>>>>>
'''

@login_required(login_url="log_in")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="log_in")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="log_in")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="log_in")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="log_in")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="log_in")
def cart_detail(request):
    return render(request, 'main/cart.html')