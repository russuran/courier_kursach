from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Courier(db.Model):
    __tablename__ = 'Courier'
    CourierID = db.Column(db.Integer, primary_key=True)
    FullName = db.Column(db.String(255), nullable=False)
    Phone = db.Column(db.String(20), unique=True, nullable=False)
    BirthDate = db.Column(db.Date, nullable=False)
    WorkExperience = db.Column(db.Integer, nullable=True)
    TransportType = db.Column(db.String(100), nullable=False)


class Client(db.Model):
    __tablename__ = 'Client'
    ClientID = db.Column(db.Integer, primary_key=True)
    FullName = db.Column(db.String(255), nullable=False)
    Phone = db.Column(db.String(20), unique=True, nullable=False)
    Address = db.Column(db.String(255), nullable=False)


class Order(db.Model):
    __tablename__ = 'Order'
    OrderID = db.Column(db.Integer, primary_key=True)
    ClientID = db.Column(db.Integer, db.ForeignKey('Client.ClientID'), nullable=False)
    OrderTime = db.Column(db.Date, nullable=False)
    DeliveryCost = db.Column(db.Numeric(10, 2), nullable=True)
    PaymentStatus = db.Column(db.String(100), nullable=False)
    Comment = db.Column(db.String(255), nullable=True)


class Product(db.Model):
    __tablename__ = 'Product'
    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(255), nullable=False)
    ProductType = db.Column(db.String(100), nullable=False)
    Weight = db.Column(db.Numeric(10, 2), nullable=True)
    Dimensions = db.Column(db.String(100), nullable=True)


class DeliveryRoute(db.Model):
    __tablename__ = 'DeliveryRoute'
    RouteID = db.Column(db.Integer, primary_key=True)
    CourierID = db.Column(db.Integer, db.ForeignKey('Courier.CourierID'), nullable=False)
    StartTime = db.Column(db.DateTime, nullable=False)
    EndTime = db.Column(db.DateTime, nullable=True)
    OrderCount = db.Column(db.Integer, nullable=True)


class Payment(db.Model):
    __tablename__ = 'Payment'
    PaymentID = db.Column(db.Integer, primary_key=True)
    OrderID = db.Column(db.Integer, db.ForeignKey('Order.OrderID'), nullable=False)
    PaymentDate = db.Column(db.Date, nullable=False)


class OrderContent(db.Model):
    __tablename__ = 'OrderContent'
    OrderID = db.Column(db.Integer, db.ForeignKey('Order.OrderID'), primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('Product.ProductID'), primary_key=True)
    Quantity = db.Column(db.Integer, nullable=False)


class RouteContent(db.Model):
    __tablename__ = 'RouteContent'
    RouteID = db.Column(db.Integer, db.ForeignKey('DeliveryRoute.RouteID'), primary_key=True)
    OrderID = db.Column(db.Integer, db.ForeignKey('Order.OrderID'), primary_key=True)
    OrderNumber = db.Column(db.Integer, nullable=False)
