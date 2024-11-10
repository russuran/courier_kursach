from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Courier, Client, Order, Product, DeliveryRoute, Payment, OrderContent, RouteContent
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/couriers', methods=['POST'])
def create_courier():
    data = request.json
    new_courier = Courier(
        FullName=data['FullName'],
        Phone=data['Phone'],
        BirthDate=data['BirthDate'],
        WorkExperience=data.get('WorkExperience'),
        TransportType=data['TransportType']
    )
    db.session.add(new_courier)
    db.session.commit()
    return jsonify({'message': 'Courier created successfully!'}), 201


@app.route('/couriers', methods=['GET'])
def get_couriers():
    couriers = Courier.query.all()
    return jsonify([{'CourierID': c.CourierID, 'FullName': c.FullName, 'Phone': c.Phone} for c in couriers]), 200


@app.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    new_client = Client(
        FullName=data['FullName'],
        Phone=data['Phone'],
        Address=data['Address']
    )
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'message': 'Client created successfully!'}), 201


@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([{'ClientID': c.ClientID, 'FullName': c.FullName, 'Phone': c.Phone} for c in clients]), 200


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    new_order = Order(
        ClientID=data['ClientID'],
        OrderTime=data['OrderTime'],
        DeliveryCost=data.get('DeliveryCost'),
        PaymentStatus=data['PaymentStatus'],
        Comment=data.get('Comment')
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully!'}), 201


@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{'OrderID': o.OrderID, 'ClientID': o.ClientID, 'OrderTime': o.OrderTime} for o in orders]), 200


@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(
        ProductName=data['ProductName'],
        ProductType=data['ProductType'],
        Weight=data.get('Weight'),
        Dimensions=data.get('Dimensions')
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully!'}), 201


@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'ProductID': p.ProductID, 'ProductName': p.ProductName, 'ProductType': p.ProductType} for p in products]), 200


@app.route('/delivery_routes', methods=['POST'])
def create_delivery_route():
    data = request.json
    new_route = DeliveryRoute(
        CourierID=data['CourierID'],
        StartTime=data['StartTime'],
        EndTime=data.get('EndTime'),
        OrderCount=data.get('OrderCount')
    )
    db.session.add(new_route)
    db.session.commit()
    return jsonify({'message': 'Delivery route created successfully!'}), 201


@app.route('/delivery_routes', methods=['GET'])
def get_delivery_routes():
    routes = DeliveryRoute.query.all()
    return jsonify([{'RouteID': r.RouteID, 'CourierID': r.CourierID, 'StartTime': r.StartTime} for r in routes]), 200


@app.route('/payments', methods=['POST'])
def create_payment():
    data = request.json
    new_payment = Payment(
        OrderID=data['OrderID'],
        PaymentDate=data['PaymentDate']
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'message': 'Payment created successfully!'}), 201


@app.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{'PaymentID': p.PaymentID, 'OrderID': p.OrderID, 'PaymentDate': p.PaymentDate} for p in payments]), 200


@app.route('/order_contents', methods=['POST'])
def create_order_content():
    data = request.json
    new_order_content = OrderContent(
        OrderID=data['OrderID'],
        ProductID=data['ProductID'],
        Quantity=data['Quantity']
    )
    db.session.add(new_order_content)
    db.session.commit()
    return jsonify({'message': 'Order content created successfully!'}), 201


@app.route('/order_contents', methods=['GET'])
def get_order_contents():
    order_contents = OrderContent.query.all()
    return jsonify([{'OrderID': oc.OrderID, 'ProductID': oc.ProductID, 'Quantity': oc.Quantity} for oc in order_contents]), 200


@app.route('/route_contents', methods=['POST'])
def create_route_content():
    data = request.json
    new_route_content = RouteContent(
        RouteID=data['RouteID'],
        OrderID=data['OrderID'],
        OrderNumber=data['OrderNumber']
    )
    db.session.add(new_route_content)
    db.session.commit()
    return jsonify({'message': 'Route content created successfully!'}), 201


@app.route('/route_contents', methods=['GET'])
def get_route_contents():
    route_contents = RouteContent.query.all()
    return jsonify([{'RouteID': rc.RouteID, 'OrderID': rc.OrderID, 'OrderNumber': rc.OrderNumber} for rc in route_contents]), 200


if __name__ == '__main__':
    app.run(debug=True)
