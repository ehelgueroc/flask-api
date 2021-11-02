from flask import Flask, jsonify
app = Flask(__name__)

from products import products

@app.route('/')
def home():
    return 'Flask with docker 1!'

@app.route('/products')
def getProducts():
    return jsonify({ "products": products})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product["name"] == product_name]
    if(len(productsFound) > 0):
        return jsonify({ "products": productsFound})
    else:
        return jsonify({ "message": "Product not found"})