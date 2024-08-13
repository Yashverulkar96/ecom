from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product.models import Product
from .models import CartItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Check if the product is already in the user's cart
    cart_product, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        # If the product is already in the cart, increase the quantity
        cart_product.quantity += 1
        cart_product.save()
        messages.success(request, "Quantity updated in your cart.")
    else:
        messages.success(request, "Product added to your cart.")

    return redirect('products_cart')

@login_required
def products_cart(request):
    cart_products = CartItem.objects.filter(user=request.user)
    context = {
        'cart_products': cart_products
    }
    return render(request, 'products_cart.html', context)
