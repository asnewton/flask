from flask_jwt import jwt_required
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.secret_key = 'ahmad'
api = Api(app)
jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item

        return {'name': None}, 404

    def post(self, name):
        data = request.get_json()
        item = { 'name': name, 'price': data['price'] }
        items.append(item)
        return item, 201

api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
app.run()
