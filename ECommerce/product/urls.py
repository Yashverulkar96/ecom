from django.urls import path
from .views import product_list, category_list, product_details

urlpatterns = [
    path('', category_list, name="categories"),
    path('products/<int:category_id>/', product_list, name="product_list_by_category"),
    path('details/<int:product_id>/', product_details, name="product_details"),
]
