from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Courier, Client, Order, Product, DeliveryRoute, Payment, OrderContent, RouteContent
from config import Config

app = Flask(__name__)

CORS(app)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

russificated = {
    'CourierID': 'Курьер',
    'FullName': 'ФИО',
    'Phone': 'Телефон',
    'WorkExperience': 'Опыт работы',
    'BirthDate': 'Дата рождения',
    'TransportType': 'Транспорт',
    'ClientID': 'Клиент',
    'OrderID': 'Заказ',
    'OrderTime': 'Время заказа',
    'DeliveryCost': 'Стоимость доставки',
    'PaymentStatus': 'Статус оплаты',
    'Comment': 'Комментарий',
    'ProductID': 'Товар',
    'ProductName': 'Наименование',
    'ProductType': 'Тип',
    'Weight': 'Вес',
    'Dimensions': 'Размеры',
    'RouteID': 'Маршрут',
    'StartTime': 'Время начала',
    'EndTime': 'Время окончания',
    'PaymentDate': 'Дата оплаты',
    'OrderCount': 'Количество заказов',
    'ProductCount': 'Количество товаров',
    'RouteCount': 'Количество маршрутов',
    'CourierCount': 'Количество курьеров', 
    'ClientCount': 'Количество клиентов',
    'OrderCount': 'Количество заказов',
    'Address': 'Адрес',}

@app.route('/couriers', methods=['POST'])
def create_courier():
    data = request.json
    required_fields = ['FullName', 'Phone', 'BirthDate', 'TransportType']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    new_courier = Courier(
        FullName=data['FullName'],
        Phone=data['Phone'],
        BirthDate=data['BirthDate'],
        WorkExperience=data.get('WorkExperience'),
        TransportType=data['TransportType']
    )
    db.session.add(new_courier)
    db.session.commit()
    return jsonify({'message': 'ok'}), 201


@app.route('/couriers', methods=['GET'])
def get_couriers():
    couriers = Courier.query.all()
    return jsonify([{'CourierID': c.CourierID, 
                     'FullName': c.FullName, 
                     'Phone': c.Phone, 
                     'WorkExperience': c.WorkExperience,
                     'BirthDate': c.BirthDate,
                     'TransportType': c.TransportType} for c in couriers]), 200


@app.route('/couriers/<int:courier_id>', methods=['PUT'])
def edit_courier(courier_id):
    data = request.json
    required_fields = ['FullName', 'Phone', 'BirthDate', 'TransportType']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    courier = Courier.query.get_or_404(courier_id)
    courier.FullName = data['FullName']
    courier.Phone = data['Phone']
    courier.BirthDate = data['BirthDate']
    courier.WorkExperience = data.get('WorkExperience')
    courier.TransportType = data['TransportType']
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/couriers/<int:courier_id>', methods=['DELETE'])
def delete_courier(courier_id):
    courier = Courier.query.get_or_404(courier_id)
    db.session.delete(courier)
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/couriers_list', methods=['GET'])
def list_courier():
    couriers = Courier.query.all()
    return jsonify([{'value': c.CourierID, 
                     'label': c.FullName } for c in couriers]), 200


@app.route('/clients_list', methods=['GET'])
def list_client():
    clients = Client.query.all()
    return jsonify([{'value': c.ClientID, 
                     'label': c.FullName } for c in clients]), 200


@app.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    required_fields = ['FullName', 'Phone', 'Address']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    new_client = Client(
        FullName=data['FullName'],
        Phone=data['Phone'],
        Address=data['Address']
    )
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'message': 'ok'}), 201


@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([{'ClientID': c.ClientID,
                     'FullName': c.FullName, 
                     'Phone': c.Phone,
                     'Address': c.Address} for c in clients]), 200


@app.route('/clients/<int:client_id>', methods=['PUT'])
def edit_client(client_id):
    data = request.json
    required_fields = ['FullName', 'Phone', 'Address']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400
    client = Client.query.get_or_404(client_id)
    client.FullName = data['FullName']
    client.Phone = data['Phone']
    client.Address = data['Address']
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    required_fields = ['ClientID', 'OrderTime', 'PaymentStatus']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    new_order = Order(
        ClientID=data['ClientID'],
        OrderTime=data['OrderTime'],
        DeliveryCost=data.get('DeliveryCost'),
        PaymentStatus=data['PaymentStatus'],
        Comment=data.get('Comment')
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'ok'}), 201


@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{'OrderID': o.OrderID,
                     'ClientID': o.ClientID,
                     'DeliveryCost': o.DeliveryCost,
                     'PaymentStatus': o.PaymentStatus,
                     'Comment': o.Comment,
                     'OrderTime': o.OrderTime} for o in orders]), 200


@app.route('/orders/<int:order_id>', methods=['PUT'])
def edit_order(order_id):
    data = request.json
    required_fields = ['ClientID', 'OrderTime', 'PaymentStatus']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400
    order = Order.query.get_or_404(order_id)
    order.ClientID = data['ClientID']
    order.OrderTime = data['OrderTime']
    order.DeliveryCost = data.get('DeliveryCost')
    order.PaymentStatus = data['PaymentStatus']
    order.Comment = data.get('Comment')
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    required_fields = ['ProductName', 'ProductType']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    new_product = Product(
        ProductName=data['ProductName'],
        ProductType=data['ProductType'],
        Weight=data.get('Weight'),
        Dimensions=data.get('Dimensions')
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'ok'}), 201


@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'ProductID': p.ProductID, 
                     'ProductName': p.ProductName,
                     'Weight': p.Weight,
                     'Dimensions': p.Dimensions, 
                     'ProductType': p.ProductType} for p in products]), 200


@app.route('/products/<int:product_id>', methods=['PUT'])
def edit_product(product_id):
    data = request.json
    required_fields = ['ProductName', 'ProductType']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    product = Product.query.get_or_404(product_id)
    product.ProductName = data['ProductName']
    product.ProductType = data['ProductType']
    product.Weight = data.get('Weight')
    product.Dimensions = data.get('Dimensions')
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/delivery_routes', methods=['POST'])
def create_delivery_route():
    data = request.json
    required_fields = ['CourierID', 'StartTime']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    new_route = DeliveryRoute(
        CourierID=data['CourierID'],
        StartTime=data['StartTime'],
        EndTime=data.get('EndTime'),
        OrderCount=data.get('OrderCount')
    )
    db.session.add(new_route)
    db.session.commit()
    return jsonify({'message': 'ok'}), 201


@app.route('/delivery_routes', methods=['GET'])
def get_delivery_routes():
    routes = DeliveryRoute.query.all()
    return jsonify([{'RouteID': r.RouteID,
                     'CourierID': r.CourierID, 
                     'StartTime': r.StartTime, 
                     'EndTime': r.EndTime,
                     'OrderCount': r.OrderCount} for r in routes]), 200


@app.route('/delivery_routes/<int:route_id>', methods=['PUT'])
def edit_delivery_route(route_id):
    data = request.json
    required_fields = ['CourierID', 'StartTime']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    route = DeliveryRoute.query.get_or_404(route_id)
    route.CourierID = data['CourierID']
    route.StartTime = data['StartTime']
    route.EndTime = data.get('EndTime')
    route.OrderCount = data.get('OrderCount')
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/delivery_routes/<int:route_id>', methods=['DELETE'])
def delete_delivery_route(route_id):
    route = DeliveryRoute.query.get_or_404(route_id)
    db.session.delete(route)
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/payments', methods=['POST'])
def create_payment():
    data = request.json
    required_fields = ['OrderID', 'PaymentDate']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    new_payment = Payment(
        OrderID=data['OrderID'],
        PaymentDate=data['PaymentDate']
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'message': 'ok'}), 201


@app.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{'PaymentID': p.PaymentID,
                     'OrderID': p.OrderID, 
                     'PaymentDate': p.PaymentDate} for p in payments]), 200


@app.route('/payments/<int:payment_id>', methods=['PUT'])
def edit_payment(payment_id):
    data = request.json
    required_fields = ['OrderID', 'PaymentDate']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    payment = Payment.query.get_or_404(payment_id)
    payment.OrderID = data['OrderID']
    payment.PaymentDate = data['PaymentDate']
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/order_contents', methods=['POST'])
def create_order_content():
    data = request.json
    required_fields = ['OrderID', 'ProductID', 'Quantity']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    new_order_content = OrderContent(
        OrderID=data['OrderID'],
        ProductID=data['ProductID'],
        Quantity=data['Quantity']
    )
    db.session.add(new_order_content)
    db.session.commit()

    return jsonify({'message': 'ok'}), 201


@app.route('/order_contents', methods=['GET'])
def get_order_contents():
    order_contents = OrderContent.query.all()
    return jsonify([{'OrderID': oc.OrderID, 
                     'ProductID': oc.ProductID, 
                     'Quantity': oc.Quantity} for oc in order_contents]), 200


@app.route('/order_contents/<int:order_id>/<int:product_id>', methods=['PUT'])
def edit_order_content(order_id, product_id):
    data = request.json
    required_fields = ['OrderID', 'ProductID', 'Quantity']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    order_content = OrderContent.query.get_or_404((order_id, product_id))
    order_content.OrderID = data['OrderID']
    order_content.ProductID = data['ProductID']
    order_content.Quantity = data['Quantity']
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/orders_list', methods=['GET'])
def orders_list():
    orders = Order.query.all()
    return jsonify([{'label': od.OrderID, 
                     'value': od.OrderID } for od in orders]), 200


@app.route('/products_list', methods=['GET'])
def products_list():
    products = Product.query.all()
    return jsonify([{'label': p.ProductName, 
                     'value': p.ProductID } for p in products]), 200


@app.route('/delivers_list', methods=['GET'])
def delivers_list():
    delivers = DeliveryRoute.query.all()
    return jsonify([{'label': d.RouteID, 
                     'value': d.RouteID } for d in delivers]), 200


@app.route('/order_contents/<int:order_id>/<int:product_id>', methods=['DELETE'])
def delete_order_content(order_id, product_id):
    order_content = OrderContent.query.get_or_404((order_id, product_id))
    db.session.delete(order_content)
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/route_contents', methods=['POST'])
def create_route_content():
    data = request.json
    required_fields = ['RouteID', 'OrderID', 'OrderNumber']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    new_route_content = RouteContent(
        RouteID=data['RouteID'],
        OrderID=data['OrderID'],
        OrderNumber=data['OrderNumber']
    )
    db.session.add(new_route_content)
    db.session.commit()
    return jsonify({'message': 'ok'}), 201


@app.route('/route_contents', methods=['GET'])
def get_route_contents():
    route_contents = RouteContent.query.all()
    return jsonify([{'RouteID': rc.RouteID, 
                     'OrderID': rc.OrderID, 
                     'OrderNumber': rc.OrderNumber} for rc in route_contents]), 200


@app.route('/route_contents/<int:route_id>/<int:order_id>', methods=['PUT'])
def edit_route_content(route_id, order_id):
    data = request.json
    required_fields = ['RouteID', 'OrderID', 'OrderNumber']
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f'Заполните поле: {russificated[field]}'}), 400

    route_content = RouteContent.query.get_or_404((route_id, order_id))
    route_content.RouteID = data['RouteID']
    route_content.OrderID = data['OrderID']
    route_content.OrderNumber = data['OrderNumber']
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


@app.route('/route_contents/<int:route_id>/<int:order_id>', methods=['DELETE'])
def delete_route_content(route_id, order_id):
    route_content = RouteContent.query.get_or_404((route_id, order_id))
    db.session.delete(route_content)
    db.session.commit()
    return jsonify({'message': 'ok'}), 200


if __name__ == '__main__':
    app.run(debug=True)
