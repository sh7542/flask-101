# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_get_valid_product(self):
        response = self.client.get("/api/v1/products/2")
        self.assertEqual(response.status_code, 200)
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'], 2)
        self.assertEqual(product['name'], 'Socialive.tv')

    def test_get_unknown_product(self):
        response = self.client.get("/api/v1/products/65534")
        self.assertEqual(response.status_code, 404)

    def test_delete_unknown_product(self):
        response = self.client.delete("/api/v1/products/65534")
        self.assertEqual(response.status_code, 404)

    def test_delete_valid_product(self):
        response = self.client.delete("/api/v1/products/3")
        self.assertEqual(response.status_code, 204)
        response = self.client.get("/api/v1/products/3")
        self.assertEqual(response.status_code, 404)

