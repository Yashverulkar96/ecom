from django.urls import path
from .views import add_to_cart, products_cart

urlpatterns = [
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),  # Ensure this is correct
    path('', products_cart, name='products_cart'),  # The main cart view
]
