from pymongo import MongoClient
from PriceScraping import BeerProgram
import json

class dBCreator:
    def __init__(self, ps):
        self.ps = ps
        self.data = []


    def createData(self):
        self.ps.readFile()
        elements = self.ps.getElements()
        # client = MongoClient('localhost', 27017)
        # db = client.pymongo_test
        for id in elements:
            self.data.append(json.dumps(elements[id].__dict__))
        print(self.data)


