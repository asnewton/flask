from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

puppies = []
class Puppy(Resource):
    def get(self, name):
        for pup in puppies:
            if pup['name'] == name:
                return pup
        return {'name': None}

    def post(self, name):
        pup ={'name': name}
        puppies.append(pup)
        return pup

    def delete(self, name):
        for index, pup in enumerate(puppies):
            if pup['name'] == name:
                deleted = puppies.pop(index)
                return {deleted: 'delete success'}


class AllPuppy(Resource):
    def get(self):
        return {'puppies': puppies}


api.add_resource(Puppy, '/puppy/<string:name>')
api.add_resource(AllPuppy, '/puppies')

if __name__ == '__main__':
    app.run(debug=True)
