from pymongo import MongoClient
from PriceScraping import BeerProgram
import json_encoder
import jsonpickle
import json

fileName = "hopsandamltchb.csv"
ps = BeerProgram(fileName, 2, 6, 7, None)
ps.readFile()

elements = ps.getElements()

client = MongoClient('localhost', 27017)


db = client.pymongo_test

with open('data.txt', 'w') as outfile:
    for m in elements:
        frozen = jsonpickle.encode(m)
        json.dump(frozen, outfile)

posts = db.posts
post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}

