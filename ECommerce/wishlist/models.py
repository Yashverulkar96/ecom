
from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)  # To track when the item was added

    def __str__(self):
        return f"{self.product.name} in {self.user.username}'s wishlist"

    class Meta:
        unique_together = ('user', 'product')  # Ensures a user cannot have the same product in their wishlist more than once
