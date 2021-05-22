from django.forms import ModelForm
from .models import Product, Order, Cart
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Product_name'}),
            'price': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Price'}),
            'specs': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Specs'}),

        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'text_inp'}),
            'password1': forms.PasswordInput(attrs={'class': 'text_inp'}),
            'password2': forms.PasswordInput(attrs={'class': 'text_inp'}),
            'email': forms.TextInput(attrs={'class': 'text_inp'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_inp', }), label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'text_inp', }), label='Password')


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["user", "product", "address"]
        widgets = {
            'user': forms.TextInput(attrs={'class': 'text-inp', 'placeholder': 'user'}),
            'product': forms.Select(attrs={'class': 'text_inp', 'placeholder': 'product'}),
            'address': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Address'}),
        }


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'
        widgets = {
            'user': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'User'}),
            'product': forms.Select(attrs={'class': 'text_inp', 'placeholder': 'Product'}),
            'quantity': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Quantity'}),
        }
