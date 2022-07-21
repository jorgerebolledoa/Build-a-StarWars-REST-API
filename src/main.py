"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, People
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(lambda User: User.serialize(), users))
    return jsonify(users), 200

@app.route('/users/<int:users_id>', methods=['GET'])
def get_user_by_id(users_id):
    users = User.query.get(users_id)
    return jsonify(users.serialize()), 200



@app.route('/users', methods=['POST'])
def create_users():
    users = User()
    users.email = request.json.get('email') 
    users.password = request.json.get('password') 
    users.is_active= request.json.get("is_active")
    users.save()
    return jsonify(users.serialize()), 201




@app.route("/planets", methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    planets = list(map(lambda Planet: Planet.serialize(), planets))
    return jsonify(planets), 200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_planets_by_id(planets_id):
    planets = Planet.query.get(planets_id)
    return jsonify(planets.serialize()), 200



@app.route('/planets', methods=['POST'])
def create_planets():
    planets = Planet()
    planets.name = request.json.get('name')
    planets.description = request.json.get('description')
    planets.thumbnail = request.json.get('thumbnail')
    planets.image = request.json.get('image')
    planets.save()
    return jsonify(planets.serialize()), 201


@app.route('/planets/<int:planets_id>', methods=['PUT'])
def update_planets(planets_id):
    planets = Planet.query.get(planets_id)
    planets.name = request.json.get('name')
    planets.description = request.json.get('description')
    planets.thumbnail = request.json.get('thumbnail')
    planets.image = request.json.get('image')
    planets.update()
    return jsonify(planets.serialize()), 201


@app.route('/planets/<int:planets_id>', methods=['DELETE'])
def delete_planets(planets_id):
    planets = Planet.query.get(planets_id)
    planets.delete()
    return jsonify(planets.serialize()), 201

@app.route("/peoples", methods=['GET'])
def get_peoples():
    peoples = People.query.all()
    peoples = list(map(lambda People: People.serialize(), peoples))
    return jsonify(peoples), 200


@app.route('/peoples/<int:peoples_id>', methods=['GET'])
def get_peoples_by_id(peoples_id):
    peoples = People.query.get(peoples_id)
    return jsonify(peoples.serialize()), 200


@app.route('/peoples', methods=['POST'])
def create_peoples():
    peoples = People()
    peoples.name = request.json.get('name')
    peoples.description = request.json.get('description')
    peoples.thumbnail = request.json.get('thumbnail')
    peoples.image = request.json.get('image')
    peoples.save()
    return jsonify(peoples.serialize()), 201


@app.route('/peoples/<int:peoples_id>', methods=['PUT'])
def update_peoples(peoples_id):
    peoples = People.query.get(peoples_id)
    peoples.name = request.json.get('name')
    peoples.description = request.json.get('description')
    peoples.thumbnail = request.json.get('thumbnail')
    peoples.image = request.json.get('image')
    peoples.update()
    return jsonify(peoples.serialize()), 201


@app.route('/peoples/<int:peoples_id>', methods=['DELETE'])
def delete_peoples(peoples_id):
    peoples = People.query.get(peoples_id)
    peoples.delete()
    return jsonify(peoples.serialize()), 201










# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
