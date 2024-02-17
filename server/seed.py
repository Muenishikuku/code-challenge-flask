from app import app
from models import db, Restaurants, Pizzas, RestaurantPizza
from faker import Faker
from random import choice as rc, randint as ri

fake = Faker()

with app.app_context():
# """ RESTAURANTS """
    Restaurants.query.delete()
    for i in range(0, 10):
        new_rest = Restaurants(name = fake.company(), address = fake.address(), rating = ri(0, 10))
        db.session.add(new_rest)
        db.session.commit()

# """ PIZZAS """
    pizza_names = ["Cheese Pizza", "Veggie Pizza",
                   "Pepperoni Pizza", "Meat Pizza",
                   "Margherita Pizza", "BBQ Chicken Pizza",
                   "Hawaiian Pizza", " Buffalo Pizza",
                   "Supreme Pizza", "The Works Pizza"
                   ]
    pizza_ingredients = ["Cheese", "Veggies",
                   "Pepperoni", "Meat",
                   "Margherita", "BBQ Chicken",
                   "Oregano"
                   ]
    Pizzas.query.delete()    
    for pizza in pizza_names:    
        new_pizza = Pizzas(name = pizza, ingredients = rc(pizza_ingredients))
        
        db.session.add(new_pizza)
        db.session.commit()

# """ RESTAURANT_PIZZA """
    RestaurantPizza.query.delete()
    for i in range(0, 10):
        new_rest_piz = RestaurantPizza(price = ri(1, 30), pizza_id = rc(Pizzas.query.all()).piz_id, restaurant_id = rc(Restaurants.query.all()).rest_id)
        db.session.add(new_rest_piz)
        db.session.commit()