"""import os
import django
import requests

# Set up Django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'textsearch.settings'
django.setup()

from home.models import Product

# Fetch data from the API
url = "https://dummyjson.com/products?limit=10000"
response = requests.get(url)
data = response.json()

# Save products to the database
for product_data in data['products']:
    try:
        print(product_data.get('brand'))
        product = Product(
            title=product_data['title'],
            description=product_data['description'],
            category=product_data['category'],
            price=product_data['price'],
            brand=product_data.get('brand'),
            sku=product_data['sku'],
            thumbnail=product_data['thumbnail']
        )
        product.save()
    except Exception as e:
        print(f"Error saving product: {e}")
"""

import os
import django
import requests

# Set up Django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'textsearch.settings'
django.setup()

from home.models import Product

# Fetch data from the Fake Store API
url = "https://fakestoreapi.com/products"
response = requests.get(url)
data = response.json()

# Save products to the database
for product_data in data:
    try:
        product = Product(
            title=product_data['title'],
            description=product_data['description'],
            category=product_data['category'],
            price=product_data['price'],
            brand=product_data.get('brand', 'Unknown'),  # Default to 'Unknown' if brand not provided
            sku=product_data.get('id', 'Unknown'),  # Assuming 'id' can serve as SKU
            thumbnail=product_data['image']
        )
        product.save()
    except Exception as e:
        print(f"Error saving product: {e}")
