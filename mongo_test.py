import pymongo
import datetime
from datetime import timedelta

def mongo_connect():
   try:
       conn = pymongo.MongoClient()
       print "Mongo is connected!"
       return conn
   except pymongo.errors.ConnectionFailure, e:
       print "Could not connect to MongoDB: %s" % e

conn = mongo_connect()
db = conn['twitter_stream']
print db  # Database(MongoClient('localhost', 27017), u'twitter_stream')

coll = db.my_collection
print db.collection_names()  # []
print conn.database_names()  # [u'local', u'test']

#If you want to drop
#coll.drop()  # remove the collection

# Adding one
# doc = {"name": "Code", "surname": "Institute", "twitter": "@codersinstitute"}
# coll.insert(doc)
# result = coll.find_one()
# print result
# {u'twitter': u'@codersinstitute', u'_id': ObjectId('5629264db1bae125ac446ba5'),

#Adding multiple
# docs = [{"name": "Henry", "surname": "Moore", "twitter": "@henrymoore"},
#        {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry"}]
# coll.insert_many(docs)
#finding all
#results = coll.find()
#finding with filter
# results = coll.find({"name": "Stephen"})
# print results #<pymongo.cursor.Cursor object at 0x02909C90>
# print(results.count())
# print(coll.count())
# for doc in results:
#     print(doc)

# coll.drop()  # remove the collection to avoid duplicates when testing
# docs = [{"name": "Code", "surname": "Institute", "twitter": "@codersinstitute",
#         "date": datetime.datetime.utcnow()},
#        {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry",
#         "date": datetime.datetime.utcnow() - timedelta(days=2)},
#        {"name": "Stephen", "surname": "Dedalus", "twitter": "@stephend",
#         "date": datetime.datetime.utcnow() + timedelta(days=10)},
#        {"name": "Armand", "surname": "Tanzarian", "twitter": "@armandt",
#         "date": datetime.datetime.utcnow() - timedelta(days=10), "_id": "22"}]
# coll.insert_many(docs)
# date = datetime.datetime.utcnow()
# for doc in coll.find({"date": {"$lt": date}}).sort("name"):  # see  also -  $lte, $gte, $ne
#    print(doc)
