
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def product_list(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    
    return render(request, 'product_list.html', {'products': products})

def product_details(request, product_id=None):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'product': product})