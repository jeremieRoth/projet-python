from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)

#db = client.movie

db = client.projet
def  db():
    base = client.projet
    #collection = client['pr']
    collection = base.movie.find()
    return collection

# import datetime

# post = { "author": "mike",
# 		"text": "My first blog post!",
# 		"tags": ["mongodb", "python", "pymongo"],
# 		"date": datetime.datetime.utcnow()}
