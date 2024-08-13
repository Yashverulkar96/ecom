import os
import django
from faker import Faker
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ECommerce.settings')
django.setup()

# Import Django models after setting up the environment
from product.models import Product, Category

def generate_products():
    fake = Faker()
    num_categories = 10
    num_products = 50

    # Create fake categories
    categories = []
    for category_name in ["Electronics", "Kitchen", "Clothing", "Beauty", "Home Accessories", "Footwear", "Bags", "Books", "Grocery", "Toys"]:
        category = Category.objects.create(name=category_name)
        categories.append(category)

    # Create fake products
    for _ in range(num_products):
        Product.objects.create(
            name=fake.word(),
            description=fake.text(),
            price=fake.random_number(digits=4),
            category=random.choice(categories),  # Use Category instance
            stock=fake.random_number(digits=2),
            image=fake.image_url(),  # Assuming you handle image URLs elsewhere
            created_at=fake.date_time_this_year()
        )

    print('Successfully generated fake data')

if __name__ == "__main__":
    generate_products()
