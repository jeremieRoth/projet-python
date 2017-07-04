from pymongo import MongoClient
from array import array
client = MongoClient()

client = MongoClient('localhost', 27017)

#db = client.movie

db = client.projet
def  getAll():
    base = client.projet
    #collection = client['pr']
    collection = base.inventory.find()
    return collection

def getClass(name):
    base = client.projet
    collection = [base.inventory.find_one({"name" : name})]
    return collection

def getSClass(id):
    base = client.projet
    collection =  [base.inventory.find({ "sClasse : { }" })]
    return collection
        
# import datetime

# post = { "author": "mike",
# 		"text": "My first blog post!",
# 		"tags": ["mongodb", "python", "pymongo"],
# 		"date": datetime.datetime.utcnow()}
