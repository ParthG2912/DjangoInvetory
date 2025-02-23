from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Products

# Create your views here.
@login_required
def home(request):
    product_list = Products.objects.order_by("product_name")
    return render(request, "home.html", {"product_list": product_list})

@login_required
def product(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, "product.html", {"product": product})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})