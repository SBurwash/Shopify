from PriceScraping import BeerProgram
from dbCreator import dBCreator
from flask import Flask
from flask_restful import Api, Resource, reqparse

fileName = "hopsandamltchb.csv"
ps = BeerProgram(fileName, 2, 6, 7, None)

dbC = dBCreator(ps)
dbC.createData()
data = dbC.data

app = Flask(__name__)
api = Api(app)



class BeerServer(Resource):
    def get(self, name):
        for user in users:
            if (name == data["Name"]):
                return user, 200
        return users


    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("Type")
        parser.add_argument("Price")
        args = parser.parse_args()

        for d in data:
            if (name == d["Name"]):
                return "User with name {} already exists".format(d), 400

        user = {
            "Type": data["Type"],
            "Name": name,
            "Price": data["Price"]
        }
        users.append(data)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("Type")
        parser.add_argument("Price")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200


api.add_resource(User, "/user/<string:name>")

app.run(debug=True)