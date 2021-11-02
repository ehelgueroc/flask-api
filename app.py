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

@app.route('/products', methods=['GET', 'POST'])
def addProduct():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify(products)

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product["name"] == product_name]
    if(len(productsFound) > 0):
        product.remove(productsFound[0])
        return jsonify({ 
            "message": "Deleted product", products": products
        })
    return jsonify({ "message": "Product not found"})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product["name"] == product_name]
    if len(productsFound) > 0:
        productsFound[0]["name"] = request.json["name"]
        productsFound[0]["price"] = request.json["price"]
        productsFound[0]["quantity"] = request.json["quantity"]

        return jsonify({ 
            "message": "Updated product", products": products
            })
    return jsonify({ "message": "Product not found"})

