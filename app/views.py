from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator


context={}

def home(request):
    combined = FProducts.objects.filter(trending=1).union(AProducts.objects.filter(trending=1))
    return render(request,"app/index.html",{'products':combined})

def register(request):
    return render(request,"app/register.html")

def collections(request):
    category = Category.objects.filter()
    return render(request,"app/collections.html", {'category': category})

def collectionsview(request,name):
    combined = FProducts.objects.filter(category__name=name).union(AProducts.objects.filter(category__name=name))
    paginator = Paginator(combined, 40)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request,"app/products/index.html",{"products":products,"category_name":name})
  
def product_details(request,cname,pname):
    Fproducts=FProducts.objects.filter(category__name=cname,name=pname).first()
    Aproducts=AProducts.objects.filter(category__name=cname,name=pname).first()
    if Fproducts:
        products=Fproducts
    elif Aproducts:
        products=Aproducts
    return render(request,"app/products/product_details.html",{"products":products})

def notification(request):
    return render(request,"app/notification.html",context)