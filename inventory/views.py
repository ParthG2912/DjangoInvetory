from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Products
from collections import defaultdict

# Create your views here.
@login_required
def home(request):
    product_list = Products.objects.order_by("product_name")

    res = defaultdict(lambda: {"total": 0, "available": 0})

    for p in product_list:
        res[p.product_name]["total"] += 1
        res[p.product_name]["available"] += p.is_available

    return render(request, "home.html", {"product_list": dict(res)})

@login_required
def product(request, name):
    products = Products.objects.filter(product_name=name)
    return render(request, "product.html", {"products": products})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})