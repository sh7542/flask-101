# wsgi.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World?"

@app.route('/api/v1/products')
def products():
    PRODUCTS = [
            { 'id': 1, 'name': 'Skello' },
            { 'id': 2, 'name': 'Socialive.tv' }
            ]
    return jsonify(PRODUCTS)

