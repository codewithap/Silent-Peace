import pymongo 
from pymongo.server_api import ServerApi

myclient = pymongo.MongoClient("mongodb+srv://speace:sp1234@silentpeace.d2wm9xi.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

db = myclient["silentpeace"]
col = db["Members"]

class database:
  def __init__(self,name,username,passwd):
    # self.name = name
    # self.username = username
    # self.passwd = passwd
    pass

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


# database.login("ap1 65","Arijit1234#")

# for user in list(col.find()):
#   col.delete_one(user)

# col.delete_many((col.find()[0]))
# print(list(col.find()))