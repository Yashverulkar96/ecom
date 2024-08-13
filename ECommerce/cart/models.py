
from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)  # To track when the item was added

    def __str__(self):
        return f"{self.product.name} - {self.quantity} pcs in {self.user.username}'s cart"

    class Meta:
        unique_together = ('user', 'product')  # Ensures a user cannot have the same product in the cart more than once
