import pymongo 
from pymongo.server_api import ServerApi

myclient = pymongo.MongoClient("mongodb+srv://speace:sp1234@silentpeace.d2wm9xi.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

db = myclient["silentpeace"]
col = db["Members"]

#userDict = { "name": "Arijit Paine", "userName":"ap165", "role":"co-founder","mobile":"919434671110","email": "arijitpaine649@gmail.com","passwd":"Arijit1234#"}
#x = col.insert_one(userDict)



query = { "userName": "ap165" }
doc = col.find(query)
print(doc[0])


#print(mycol)
"""
mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
print(x.inserted_id)
print(mydb.list_collection_names())

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)


x = mycol.find_one()
print(x)


for x in mycol.find():
  print(x)
  

for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

for x in mycol.find({},{ "address": 0 }):
  print(x)
myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
  
  """