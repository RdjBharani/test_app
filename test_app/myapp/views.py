from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = ProductDetails.objects.all()
    return render(request, 'home.html', {'categories': categories, 'products': products})

def create(request):
    if request.method == "POST":
        print(14)
        category_id = request.POST['categories']
        product_name = request.POST['product_name']
        product_cost = request.POST['product_cost']
        ProductDetails.objects.create(category_id=category_id, name=product_name, cost=product_cost)
        categories = Category.objects.all()
        products = ProductDetails.objects.all()
        return render(request, 'home.html', {'categories': categories, 'products': products})
    else:
        categories = Category.objects.all()
        products = ProductDetails.objects.all()
        return render(request, 'home.html', {'categories': categories, 'products': products})

def edit_product_page(request, id):
    data = ProductDetails.objects.get(id=id)  
    return render(request,'edit_product.html', {'data':data})

def edit_product_details(request, id):
    if request.method=='POST':
        product_name = request.POST['product_name']
        product_cost = request.POST['product_cost']
        ProductDetails.objects.filter(id=id).update(name=product_name, cost=product_cost)
        categories = Category.objects.all()
        products = ProductDetails.objects.all()
        return render(request, 'home.html', {'categories': categories, 'products': products})
    else:
        data = ProductDetails.objects.get(id=id)  
        return render(request,'edit_product.html', {'data':data})

def delete_product(request, id):
    data = ProductDetails.objects.get(id=id)
    data.delete()
    return render(request,'edit_product.html', {'data':data})