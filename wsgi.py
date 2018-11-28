# wsgi.py
from flask import Flask, jsonify
app = Flask(__name__)

PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'Bidon' }
        ]

@app.route('/')
def hello():
    return "Hello World?"

@app.route('/api/v1/products')
def products():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:product_id>')
def get_product(product_id):
    for product in PRODUCTS:
        if product['id'] == product_id:
            return jsonify(product), 200
    return 'Product Not Found', 404
