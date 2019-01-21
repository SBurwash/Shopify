from PriceScraping import BeerProgram
from dbCreator import dBCreator
from flask import Flask
from flask_restful import Api, Resource, reqparse

fileName = "hopsandamltchb.csv"
ps = BeerProgram(fileName, 2, 6, 7, None)

dbC = dBCreator(ps)
dbC.createData()
dbC.printData()
data = dbC.data

app = Flask(__name__)
api = Api(app)

class Ingredient(Resource):
    def get(self,name):
        for d in data:
           if(name == d["Name"]):
               #Item found
               return d, 200
        return "Item not found"

    # def post(self, name):
    #     for d in data:
    #         if (name == d["Name"]):
    #             # Adding item to cart (there is no cart in this instance
    #             if (d[name].inventory_count > 0):
    #                 d[name].inventory_count -= 1
    #                 return "Item added to cart", 200
    #             else:
    #                 return "No more items in inventory", 400
    #     return "Item not found"

api.add_resource(Ingredient,"/ingredient/<string:name>")
app.run(debug =True)