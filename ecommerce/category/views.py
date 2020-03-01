from django.shortcuts import render, redirect
from .models import Product


def all(request):
    context = {
        "title":"Home Page",
        "products":Product.objects.all()
        }
    return render(request,"category/all.html",context)

def create(request):
    return render(request,"category/create.html")

def edit(request):
    return render(request,"category/edit.html")

def delete(request):
    return redirect("cat-home")

