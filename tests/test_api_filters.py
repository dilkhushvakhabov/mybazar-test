import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.filter


@pytest.mark.django_db
class TestProductAPI:
    """
    Integration tests for the Product API focusing on filtering, search, and pagination
    """

    @pytest.fixture(autouse=True)
    def setup(self, products):
        """Ensure products are created before running tests"""
        self.products = products

    def test_product_list(self, api_client):
        """Test getting all products"""
        url = reverse('product-list')
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert 'results' in response.data
        assert 'count' in response.data
        assert response.data['count'] == len(self.products)

    def test_pagination(self, api_client):
        """Test pagination works correctly"""
        url = reverse('product-list')
        
        # Test default pagination (10 items per page)
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 10
        assert response.data['count'] == len(self.products)
        
        # Test custom page size
        response = api_client.get(f"{url}?page_size=5")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 5
        
        # Test second page
        response = api_client.get(f"{url}?page=2&page_size=5")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) > 0
        assert response.data['previous'] is not None

    def test_price_filtering(self, api_client):
        """Test filtering products by price range"""
        url = reverse('product-list')
        
        # Test min_price filter
        response = api_client.get(f"{url}?min_price=100")
        assert response.status_code == status.HTTP_200_OK
        for product in response.data['results']:
            assert float(product['price']) >= 100
        
        # Test max_price filter
        response = api_client.get(f"{url}?max_price=50")
        assert response.status_code == status.HTTP_200_OK
        for product in response.data['results']:
            assert float(product['price']) <= 50
        
        # Test price range
        response = api_client.get(f"{url}?min_price=30&max_price=200")
        assert response.status_code == status.HTTP_200_OK
        for product in response.data['results']:
            assert float(product['price']) >= 30
            assert float(product['price']) <= 200

    def test_category_filtering(self, api_client, categories):
        """Test filtering products by category"""
        url = reverse('product-list')
        
        # Test single category filter
        response = api_client.get(f"{url}?category={categories[0].name}")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] > 0
        for product in response.data['results']:
            assert product['category'] == categories[0].id
        
        # Test multiple categories
        response = api_client.get(f"{url}?category={categories[0].name},{categories[1].name}")
        assert response.status_code == status.HTTP_200_OK
        for product in response.data['results']:
            assert product['category'] in [categories[0].id, categories[1].id]
        

    def test_search(self, api_client):
        """Test searching products by name"""
        url = reverse('product-list')
        
        # Search for products with "phone" in the name
        response = api_client.get(f"{url}?search=phone")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] > 0
        for product in response.data['results']:
            assert 'phone' in product['name'].lower()
        
        # Search for products with "book" in the name
        response = api_client.get(f"{url}?search=book")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] > 0
        for product in response.data['results']:
            assert 'book' in product['name'].lower()
        
        # Search for non-existent product
        response = api_client.get(f"{url}?search=nonexistent")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 0

    def test_combined_filters(self, api_client, categories):
        """Test combining multiple filters and search"""
        url = reverse('product-list')
        
        # Combine category, price range, and search
        response = api_client.get(
            f"{url}?category={categories[0].name}&min_price=100&max_price=1000&search=smart"
        )
        assert response.status_code == status.HTTP_200_OK
        
        for product in response.data['results']:
            assert product['category'] == categories[0].id
            assert float(product['price']) >= 100
            assert float(product['price']) <= 1000
            assert 'smart' in product['name'].lower()
        
        # Test combining filters with pagination
        response = api_client.get(
            f"{url}?category={categories[0].name}&page_size=2&page=1"
        )
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) <= 2
        for product in response.data['results']:
            assert product['category'] == categories[0].id


@pytest.mark.django_db
class TestCategoryAPI:
    """
    Integration tests for the Category API
    """
    
    @pytest.fixture(autouse=True)
    def setup(self, categories):
        """Ensure categories are created before running tests"""
        self.categories = categories
    
    def test_category_list(self, api_client):
        """Test getting all categories"""
        url = reverse('category-list')
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert 'results' in response.data  # Check if response is paginated
        assert response.data['count'] == len(self.categories)
        assert len(response.data['results']) == len(self.categories) 