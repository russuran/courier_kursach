"""Initial

Revision ID: 30cf4c88acb5
Revises: 
Create Date: 2024-11-10 05:31:56.215352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30cf4c88acb5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Client',
    sa.Column('ClientID', sa.Integer(), nullable=False),
    sa.Column('FullName', sa.String(length=255), nullable=False),
    sa.Column('Phone', sa.String(length=20), nullable=False),
    sa.Column('Address', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('ClientID'),
    sa.UniqueConstraint('Phone')
    )
    op.create_table('Courier',
    sa.Column('CourierID', sa.Integer(), nullable=False),
    sa.Column('FullName', sa.String(length=255), nullable=False),
    sa.Column('Phone', sa.String(length=20), nullable=False),
    sa.Column('BirthDate', sa.Date(), nullable=False),
    sa.Column('WorkExperience', sa.Integer(), nullable=True),
    sa.Column('TransportType', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('CourierID'),
    sa.UniqueConstraint('Phone')
    )
    op.create_table('Product',
    sa.Column('ProductID', sa.Integer(), nullable=False),
    sa.Column('ProductName', sa.String(length=255), nullable=False),
    sa.Column('ProductType', sa.String(length=100), nullable=False),
    sa.Column('Weight', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('Dimensions', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('ProductID')
    )
    op.create_table('DeliveryRoute',
    sa.Column('RouteID', sa.Integer(), nullable=False),
    sa.Column('CourierID', sa.Integer(), nullable=False),
    sa.Column('StartTime', sa.DateTime(), nullable=False),
    sa.Column('EndTime', sa.DateTime(), nullable=True),
    sa.Column('OrderCount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['CourierID'], ['Courier.CourierID'], ),
    sa.PrimaryKeyConstraint('RouteID')
    )
    op.create_table('Order',
    sa.Column('OrderID', sa.Integer(), nullable=False),
    sa.Column('ClientID', sa.Integer(), nullable=False),
    sa.Column('OrderTime', sa.Date(), nullable=False),
    sa.Column('DeliveryCost', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('PaymentStatus', sa.String(length=100), nullable=False),
    sa.Column('Comment', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['ClientID'], ['Client.ClientID'], ),
    sa.PrimaryKeyConstraint('OrderID')
    )
    op.create_table('OrderContent',
    sa.Column('OrderID', sa.Integer(), nullable=False),
    sa.Column('ProductID', sa.Integer(), nullable=False),
    sa.Column('Quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['OrderID'], ['Order.OrderID'], ),
    sa.ForeignKeyConstraint(['ProductID'], ['Product.ProductID'], ),
    sa.PrimaryKeyConstraint('OrderID', 'ProductID')
    )
    op.create_table('Payment',
    sa.Column('PaymentID', sa.Integer(), nullable=False),
    sa.Column('OrderID', sa.Integer(), nullable=False),
    sa.Column('PaymentDate', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['OrderID'], ['Order.OrderID'], ),
    sa.PrimaryKeyConstraint('PaymentID')
    )
    op.create_table('RouteContent',
    sa.Column('RouteID', sa.Integer(), nullable=False),
    sa.Column('OrderID', sa.Integer(), nullable=False),
    sa.Column('OrderNumber', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['OrderID'], ['Order.OrderID'], ),
    sa.ForeignKeyConstraint(['RouteID'], ['DeliveryRoute.RouteID'], ),
    sa.PrimaryKeyConstraint('RouteID', 'OrderID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('RouteContent')
    op.drop_table('Payment')
    op.drop_table('OrderContent')
    op.drop_table('Order')
    op.drop_table('DeliveryRoute')
    op.drop_table('Product')
    op.drop_table('Courier')
    op.drop_table('Client')
    # ### end Alembic commands ###