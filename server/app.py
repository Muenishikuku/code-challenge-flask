from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api, Resource
from models import db, Restaurants, Pizzas, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
api = Api(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return("""
           <div style="display: flex; justify-content: center; align-items: center;">
                <h1 style="color:green;">PIZZAS & RESTAURANTS</h1>
           </div>
           """         
        )


class Rests(Resource):
    def get(self):
        rests = [restaurant.to_dict() for restaurant in Restaurants.query.all()]
        response = make_response(jsonify(rests), 200)        
        return response

api.add_resource(Rests, '/restaurants', endpoint='restaurants')

class Rest_by_id(Resource):
    def get(self, id):
        rest = Restaurants.query.filter_by(rest_id = id).first()
        
        response = make_response(jsonify(rest.to_dict()), 200)
        
        return response
    
    def delete(self, id):
        rest = Restaurants.query.filter_by(rest_id = id).first()
        rest_piz = RestaurantPizza.query.filter_by(rest_piz_id = id).all()
        
        if rest:
            if rest_piz:
                for restpiz in rest_piz:
                    db.session.delete(restpiz)
                    db.session.commit()
            db.session.delete(rest)
            db.session.commit()            
            response = make_response({}, 200)
            return response
        else:
            response = make_response({"error": "Restaurant not found"}, 200)
            return response

api.add_resource(Rest_by_id, '/restaurants/<int:id>')

class Handle_Pizzas(Resource):
    def get(self):
        pizzas = [pizza.to_dict() for pizza in Pizzas.query.all()]    
        response = make_response(jsonify(pizzas))
        return response
    
api.add_resource(Handle_Pizzas, '/pizzas')

class Rest_Pizzas(Resource):
    def get(self):
        rest_pizzas = [respiz.to_dict() for respiz in RestaurantPizza.query.all()]
        response = make_response(jsonify(rest_pizzas))
        return response
        pass
    
    def post(self):
        data = request.get_json()
        new_rest_piz = RestaurantPizza(price = data['price'], pizza_id = data['pizza_id'], restaurant_id = data['restaurant_id'])
        # new_rest_piz = RestaurantPizza(price = request.form.get('price'), pizza_id = request.form.get('pizza_id'), restaurant_id = request.form.get('restaurant_id'))
        db.session.add(new_rest_piz)
        db.session.commit()
        
        response = make_response(jsonify(new_rest_piz), 201)
        
        return response
        
api.add_resource(Rest_Pizzas, '/restaurant_pizzas')

if __name__ == "__main__":
    app.run(port = 5500, debug = True)