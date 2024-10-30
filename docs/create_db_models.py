# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# Base class for declarative models
Base = declarative_base()

# Define database connection
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

# Define models with descriptions

class Company(Base):
    """description: Represents a company within the system."""
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)

    # Relationships
    accounts = relationship('Account', backref='company')

class Account(Base):
    """description: Represents an account associated with a company."""
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    account_number = Column(String, nullable=False, unique=True)
    balance = Column(Float, default=0.0)
    account_type = Column(String, nullable=False)

    # Relationships
    transactions = relationship('Transaction', backref='account')

class Product(Base):
    """description: Represents a product offered by the company."""
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)

    # Relationships
    order_items = relationship('OrderItem', backref='product')

class Transaction(Base):
    """description: Records transactions related to accounts."""
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    transaction_date = Column(DateTime, default=datetime.utcnow)
    amount = Column(Float, nullable=False)

class Order(Base):
    """description: Represents an order placed by a company."""
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    order_date = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Float, default=0.0)

    # Relationships
    order_items = relationship('OrderItem', backref='order')

class OrderItem(Base):
    """description: Represents items within an order."""
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

class Inventory(Base):
    """description: Represents the inventory records for products."""
    __tablename__ = 'inventories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    stock_quantity = Column(Integer, nullable=False)

class Supplier(Base):
    """description: Represents suppliers for products."""
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact = Column(String, nullable=True)

class Supply(Base):
    """description: Represents supply records from suppliers to the company."""
    __tablename__ = 'supplies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    supply_date = Column(DateTime, default=datetime.utcnow)
    quantity_supplied = Column(Integer, nullable=False)

class Customer(Base):
    """description: Represents customers of the company."""
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)

    # Relationships
    customer_history = relationship('CustomerHistory', backref='customer')


class CustomerHistory(Base):
    """description: Represents historical interactions of customers."""
    __tablename__ = 'customer_histories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    interaction_date = Column(DateTime, default=datetime.utcnow)
    interaction_detail = Column(String, nullable=True)

class Payment(Base):
    """description: Records payments made to the company."""
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    payment_date = Column(DateTime, default=datetime.utcnow)
    amount = Column(Float, nullable=False)


# Create tables in the database
Base.metadata.create_all(engine)

# Insert sample data
company1 = Company(name='Tech Solutions', address='123 Tech Avenue')
company2 = Company(name='Gadget Works', address='456 Gadget Lane')

product1 = Product(name='Laptop', description='14 inch laptop', price=899.99)
product2 = Product(name='Smartphone', description='5 inch smartphone', price=499.99)

account1 = Account(company_id=1, account_number='ACC123', balance=1200.00, account_type='Checking')
account2 = Account(company_id=2, account_number='ACC456', balance=1500.00, account_type='Saving')

transaction1 = Transaction(account_id=1, transaction_date=datetime.now(), amount=300.00)
transaction2 = Transaction(account_id=2, transaction_date=datetime.now(), amount=450.00)

order1 = Order(company_id=1, order_date=datetime.now(), total_amount=0)
order2 = Order(company_id=2, order_date=datetime.now(), total_amount=0)

order_item1 = OrderItem(order_id=1, product_id=1, quantity=2, price=899.99)
order_item2 = OrderItem(order_id=2, product_id=2, quantity=1, price=499.99)

inventory1 = Inventory(product_id=1, stock_quantity=50)
inventory2 = Inventory(product_id=2, stock_quantity=75)

supplier1 = Supplier(name='Electronics Supplier', contact='supplier_contact@electronicssupplier.com')

supply1 = Supply(supplier_id=1, product_id=1, supply_date=datetime.now(), quantity_supplied=30)
supply2 = Supply(supplier_id=1, product_id=2, supply_date=datetime.now(), quantity_supplied=45)

customer1 = Customer(name='Alice Doe', email='alice@example.com')
customer2 = Customer(name='Bob Smith', email='bob@example.com')

customer_history1 = CustomerHistory(customer_id=1, interaction_date=datetime.now(), interaction_detail='Purchased a laptop')
customer_history2 = CustomerHistory(customer_id=2, interaction_date=datetime.now(), interaction_detail='Inquired about smartphone pricing')

payment1 = Payment(customer_id=1, payment_date=datetime.now(), amount=900.00)
payment2 = Payment(customer_id=2, payment_date=datetime.now(), amount=500.00)

# Add and commit the sample data to the session
session.add_all([company1, company2, product1, product2, account1, account2, transaction1, transaction2, order1, order2, order_item1, order_item2, inventory1, inventory2, supplier1, supply1, supply2, customer1, customer2, customer_history1, customer_history2, payment1, payment2])
session.commit()

# Close the session
session.close()
