
##  Pizza & Restaurant API

This project implements a simple API using Flask, Flask-Migrate, Flask-CORS, and Flask-RESTful for managing restaurants and pizzas.

## Installation

Clone the repository:

git clone <https://github.com/Muenishikuku/code-challenge-flask>

- Install dependencies:

pip install -r requirements.txt

- Run the application:

python app.py

- The API will start running on port 5500.

## Endpoints

GET /restaurants: Retrieves a list of all restaurants.
GET /restaurants/{id}: Retrieves details of a specific restaurant by ID.
DELETE /restaurants/{id}: Deletes a restaurant by ID.
GET /pizzas: Retrieves a list of all pizzas.
GET /restaurant_pizzas: Retrieves a list of all restaurant-pizza associations.
POST /restaurant_pizzas: Creates a new restaurant-pizza association.

## Sample Usage

- To retrieve a list of all restaurants:

curl http://localhost:5500/restaurants

- To retrieve details of a specific restaurant with ID 1:

curl http://localhost:5500/restaurants/1

- To delete a restaurant with ID 1:

curl -X DELETE http://localhost:5500/restaurants/1

- To retrieve a list of all pizzas:

curl http://localhost:5500/pizzas

- To retrieve a list of all restaurant-pizza associations:

curl http://localhost:5500/restaurant_pizzas

- To create a new restaurant-pizza association:

curl -X POST -H "Content-Type: application/json" -d '{"price": 10.99, "pizza_id": 1, "restaurant_id": 1}' http://localhost:5500/restaurant_pizzas

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## MIT License

Copyright (c) [2024]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Acknowledgments

This project was built as part of a code challenge. Thanks to the challenge organizers for the opportunity.

## Author
Mueni Shikuku
charlesmueni2@gmail.com
