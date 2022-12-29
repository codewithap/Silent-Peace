import pymongo 
from pymongo.server_api import ServerApi

myclient = pymongo.MongoClient("mongodb+srv://speace:sp1234@silentpeace.d2wm9xi.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

db = myclient["silentpeace"]
col = db["Members"]

class database:

  def login(username,passwd):
    udict = { "userName" : username }
    data = list(col.find(udict))

    if len(data)>0:
      if data[0]["passwd"] == passwd:
        return ["Logged in successfully", True]
      elif data[0]["passwd"] != passwd:
        return ['Incorrect Password',False]
    else:
      return [f"No user named ' {username} '",False]
  
  
  def register(name, username, passwd, email, number):
    udict = {
      "name": name,
      "userName": username,
      "passwd" : passwd,
      "email" : email,
      "number" : number,
      "role": "member"
    }
    udict1 = {"userName": username}
    udict2 = {"email" : email}
    udict3 = {"number" : number}
    
    if len(list(col.find(udict1)))>0:
      return ["Username already exists...",False]
    elif len(list(col.find(udict2)))>0:
      return ["Email already exists...", False]
    elif len(list(col.find(udict3)))>0:
      return ["Number already exists....",False]
    else:
      col.insert_one(udict)
      return ["Registered Successfully....",True]




# database.login("ap1 65","Arijit1234#")

# for user in list(col.find()):
#   col.delete_one(user)

# col.delete_many((col.find()[0]))
print(list(col.find()))