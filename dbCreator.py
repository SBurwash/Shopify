from pymongo import MongoClient
from PriceScraping import BeerProgram
import json

class dBCreator:
    def __init__(self, ps):
        self.ps = ps
        self.data = []


    def createData(self):
        self.ps.readFile()
        self.ps.printElement()
        elements = self.ps.getElements()
        self.data.append(json.dumps(elements["coffee malt"].__dict__))

        # for id in elements:
        #     elements[id].Name.encode('latin-1').decode('latin-1')
        #     elements[id].Type.encode("latin-1")
        #     print(id)
        #     print(type)
        #     print(elements[id].Price)
        #     self.data.append(json.dumps(elements["coffee malt"].__dict__))

    def printData(self):
        print(self.data)


