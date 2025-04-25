import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from app.models.store import Category, Product


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def categories():
    categories = [
        Category.objects.create(name="Electronics"),
        Category.objects.create(name="Clothing"),
        Category.objects.create(name="Books"),
    ]
    return categories


@pytest.fixture
def products(categories):
    products = [
        Product.objects.create(
            name="Smartphone",
            description="Latest smartphone model",
            price=1000.00,
            category=categories[0],
        ),
        Product.objects.create(
            name="Laptop",
            description="Powerful laptop",
            price=1500.00,
            category=categories[0],
        ),
        Product.objects.create(
            name="T-shirt",
            description="Cotton t-shirt",
            price=20.00,
            category=categories[1],
        ),
        Product.objects.create(
            name="Jeans",
            description="Blue jeans",
            price=50.00,
            category=categories[1],
        ),
        Product.objects.create(
            name="Python Book",
            description="Learn Python programming",
            price=35.00,
            category=categories[2],
        ),
        Product.objects.create(
            name="Django Book",
            description="Learn Django framework",
            price=40.00,
            category=categories[2],
        ),
        Product.objects.create(
            name="SmartTV",
            description="4K Smart TV",
            price=800.00,
            category=categories[0],
        ),
        Product.objects.create(
            name="Phone Case",
            description="Protective smartphone case",
            price=15.00,
            category=categories[0],
        ),
        Product.objects.create(
            name="Dress",
            description="Summer dress",
            price=60.00,
            category=categories[1],
        ),
        Product.objects.create(
            name="REST API Book",
            description="Learn REST API development",
            price=45.00,
            category=categories[2],
        ),
        Product.objects.create(
            name="Smart Watch",
            description="Fitness tracking smart watch",
            price=200.00,
            category=categories[0],
        ),
        Product.objects.create(
            name="Headphones",
            description="Noise cancelling headphones",
            price=150.00,
            category=categories[0],
        ),
    ]
    return products 