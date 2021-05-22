from django.shortcuts import render, redirect
from .models import Product, Order, Cart
from .forms import CreateProductForm, UserRegistrationForm, LoginForm, OrderForm, CartForm
from django.contrib.auth import authenticate, logout  # login

from django.contrib.auth import login as djangologin

from .decorators import user_login, admin_only
from .authentication import EmailAuthenticationBackend


# Create your views here.
#@user_login
def base(request):
    if request.user.is_authenticated:
        return render(request, "mobile/base.html")
    else:
        return redirect("logout")


#@admin_only#admin page
#@admin_only
def index(request):
    if request.user.is_superuser:
        return render(request, 'mobile/index.html')
    else:
        return redirect("logout")



# list  all mobiles
# @admin_only
# @user_login
def list_mobiles(request):
    mobiles = Product.objects.all()
    context = {}
    context["mobiles"] = mobiles
    return render(request, "mobile/mobileslist.html", context)


# @admin_only
def admin_mobile(request):
    mobiles = Product.objects.all()
    context = {}
    context['mobiles'] = mobiles
    return render(request, 'mobile/adminlist.html', context)


# to add mobile
@admin_only
def add_product(request):
    form = CreateProductForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = CreateProductForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("adminhome")
        else:
            context["form"]=form
            return render(request,"mobile/createmobile.html", context)

    return render(request, "mobile/createmobile.html", context)


# create a function to get id of each mobile
def get_mobile_object(id):
    return Product.objects.get(id=id)


# to view mobile details
# @user_login
def mobile_details(request, id):
    mobile = get_mobile_object(id)
    context = {}
    context["mobile"] = mobile
    return render(request, "mobile/mobiledetails.html", context)


# admin mobile details
# @admin_only
def admin_mobile_details(request, id):
    mobile = get_mobile_object(id)
    context = {}
    context['mobile'] = mobile
    return render(request, 'mobile/adminmobiledetails.html', context)


# to delete mobile
# @admin_only
def mobile_delete(request, id):
    mobile = get_mobile_object(id)
    mobile.delete()
    return redirect("adminhome")


# update a mobile details
# @admin_only
def update_mobile(request, id):
    mobile = get_mobile_object(id)
    form = CreateProductForm(instance=mobile)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = CreateProductForm(instance=mobile, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("adminlist")
    return render(request, "mobile/mobileupdate.html", context)


# for order
# @user_login
def item_order(request, id):
    product = get_mobile_object(id)
    form = OrderForm(initial={'user': request.user, 'product': product})
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "mobile/vieworders.html")
        else:
            context["form"] = form
            return render(request, "mobile/ordereditem.html", context)

    return render(request, "mobile/ordereditem.html", context)


# to view Your Order
# @user_login
def view_my_orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {}
    context['orders'] = orders
    return render(request, "mobile/vieworders.html", context)


#  cancel Your Order
# @user_login
def cancel_order(request, id):
    order = Order.objects.get(id=id)
    order.status = 'cancelled'
    order.save()
    return redirect("vieworder")


# add to cart
# @user_login
def add_to_cart(request, id):
    product = get_mobile_object(id)
    form = CartForm(initial={'user': request.user, 'product': product})
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listmobiles')
        else:
            context['form'] = form
            return render(request, 'mobile/mobiledetails.html', context)
    return render(request, 'mobile/cartitems.html', context)


# View Cart Item
# @user_login

def mycart_item(request):
    carts = Cart.objects.filter(user=request.user)
    context = {}
    context['carts'] = carts
    return render(request, 'mobile/cartview.html', context)


# remove item from cart
# @user_login
def remove_cart_item(request, id):
    carts = Cart.objects.get(id=id)
    carts.delete()
    return redirect('listmobiles')


# buy from Cart
# @user_login
def checkout(request, id):
    carts = Cart.objects.get(id=id)
    form = OrderForm(initial={'user': request.user, 'product': carts.product})
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            remove_cart_item(request,id)
            return redirect('mycart')
        else:
            context['form'] = form
            return render(request, 'mobile/ordereditem.html', context)
    return render(request, 'mobile/ordereditem.html', context)


# to register
def registration(request):
        form = UserRegistrationForm()
        context = {}
        context["form"] = form
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("login")
            else:
                context["form"] = form
                return render(request, "mobile/userregistration.html", context)

        return render(request, "mobile/userregistration.html", context)

    # form = UserRegistrationForm()
    # context = {}
    # context["form"] = form
    # if request.method == 'POST':
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request, "mobile/login.html", context)
    #     else:
    #         form = UserRegistrationForm(request.POST)
    #         context["form"] = form
    #         return render(request, "mobile/registration.html")
    # return render(request, "mobile/registration.html", context)


# to login
def login(request):
    context = {}
    form = LoginForm()
    context["form"] = form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            # for emailauthentication
            # obj = EmailAuthenticationBackend()
            # user = obj.authenticate(request, username=username, password=password)

            user = authenticate(request, username=username, password=password)
            print("user")
            if user:
                djangologin(request, user)
                #return redirect("userhome")
                if user.is_superuser:
                    return redirect('adminhome')
                # elif user.is_authenticated:
                else:
                     return redirect("userhome")

            else:
                 return render(request, "mobile/login.html", context)
                # context["form"] = LoginForm(request.POST)
            # return render(request, "mobile/index.html")
    return render(request, "mobile/login.html", context)


# to logout
def signout(request):
    logout(request)
    return redirect('login')

# create Product
# list mobiles
# update
# view
# delete

#
# admin==>jyothi
# pswd:lakshmi123
# user:abhimanyu
# sachu123


# register user==>shikha
# ponnu123
#superuser===>athira,athira123