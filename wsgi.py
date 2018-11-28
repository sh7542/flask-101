# wsgi.py
from flask import Flask, jsonify, request
app = Flask(__name__)

class Counter:
    def __init__(self):
        self.id = 5

    def next(self):
        self.id += 1
        return self.id


PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'Bidon' },
        { 'id': 4, 'name': 'Pasglop'}
        ]

@app.route('/')
def hello():
    return "Hello World?"

@app.route('/api/v1/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return jsonify(PRODUCTS)
    elif request.method == 'POST':
        payload = request.get_json()
        ID = Counter()
        product_id = ID.next()
        PRODUCTS.append({'id': product_id, 'name' : payload['name']})
        return jsonify([{'id': product_id, 'name' : payload['name']}]), 201
    else:
        return "Unimplemented method {0}".format(request.method), 500

@app.route('/api/v1/products/<int:product_id>', methods=['GET', 'DELETE', 'PATCH'])
def manage_product(product_id):
    if request.method in ['GET', 'DELETE']:
        return get_del_product(product_id)
    elif request.method == 'PATCH':
        return update_product(product_id)
    else:
        return "Unimplemented method {0}".format(request.method), 500

def update_product(product_id):
    for product in PRODUCTS:
        if product['id'] == product_id:
            payload = request.get_json()
            try:
                name = payload['name']
                if name:
                    product['name'] = name
                    return '', 204
                else:
                    return 'Invalid Name in payload', 422
            except KeyError:
                return 'No name in payload', 422

    return 'Product Not Found', 422

def get_del_product(product_id):
    for product in PRODUCTS:
        if product['id'] == product_id:
            if request.method == 'GET':
                return jsonify(product), 200
            else:
                PRODUCTS.remove(product)
                return '', 204
    return 'Product Not Found', 404
