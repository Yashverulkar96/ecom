from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/', default='category_images/default.jpg')


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Discount(models.Model):
    # DISCOUNT_TYPE_CHOICES = (
    #     ('Percentage', 'Percentage'),
    #     ('Fixed Amount', 'Fixed Amount'),
    # )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discounts')
    # discount_type = models.CharField(max_length=50, choices=DISCOUNT_TYPE_CHOICES)
    discount_value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.discount_value}% off on {self.product.name}"