"""MobileProject URL Configuration

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
from django.urls import path
from django .shortcuts import render

from .views import base,index ,list_mobiles,admin_mobile,admin_mobile_details,add_product,mobile_details,mobile_delete,update_mobile,\
    registration,login,signout,item_order,view_my_orders,cancel_order ,add_to_cart,\
    mycart_item,remove_cart_item,checkout



urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",lambda request:render(request,"mobile/base.html"))
    path('userhome', base, name="userhome"),
    path("adminhome",index,name="adminhome"),
    path("listmobiles",list_mobiles,name="listmobiles"),
    path('adminlist',admin_mobile,name='adminlist'),
    path('admindetails/<int:id>', admin_mobile_details, name='adminmobdetails'),
    path("addproduct",add_product,name="addproduct"),
    path("details/<int:id>",mobile_details,name="details"),
    path("update/<int:id>",update_mobile,name="update"),
    path("delete/<int:id>",mobile_delete,name='delete'),
    path("itemordered/<int:id>",item_order,name='order'),
    path('addcart/<int:id>', add_to_cart, name='addcart'),
    path('mycart',mycart_item,name='mycart'),
    path('remove/<int:id>',remove_cart_item,name='remove'),
    path('vieworder',view_my_orders,name='vieworder'),
    path('checkout/<int:id>', checkout, name='checkout'),
    path("cancelorder/<int:id>",cancel_order,name='cancelorder'),
    path("register",registration,name="register"),
    path("login",login,name="login"),
    path("logout",signout,name="logout")
]
