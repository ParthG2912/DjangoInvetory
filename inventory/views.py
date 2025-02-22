from django.shortcuts import render, get_object_or_404
from .models import Products

# Create your views here.
def home(request):
    product_list = Products.objects.order_by("product_name")
    return render(request, "home.html", {"product_list": product_list})

def product(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, "product.html", {"product": product})