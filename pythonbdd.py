from pymongo import MongoClient
client = MongoClient()

client = Mo,goClient('localhost', 27017)

db = client.test_database

db = client ['test_database']

collection = db.test_database

# import datetime

# post = { "author": "mike",
# 		"text": "My first blog post!",
# 		"tags": ["mongodb", "python", "pymongo"],
# 		"date": datetime.datetime.utcnow()}