from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Pizzas(db.Model, SerializerMixin):
    __tablename__ = "pizzas"
    
    serialize_rules = ('-rest_pizzas.pizza', )
      
    piz_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    
    rest_pizzas = db.relationship("RestaurantPizza", backref = 'pizza')
    
    
class Restaurants(db.Model, SerializerMixin):
    __tablename__ = "restaurants"
    
    serialize_rules = ('-rest_pizzas.restaurant', )
    
    rest_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    address = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    
    rest_pizzas = db.relationship("RestaurantPizza", backref = 'restaurant')    
    
class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = "restaurant_pizza"
    
    serialize_rules = ('-pizza.rest_pizzas', '-restaurant.rest_pizzas')
    
    rest_piz_id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.piz_id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.rest_id'))
    
    @validates(price)
    def validate_price(self, key, value):
        if not 1 <= value <= 30:
            raise ValueError("Price must be between 1 and 30")