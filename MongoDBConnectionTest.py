import pymongo
from pymongo import MongoClient
from pprint import pprint
#://user:password@...
client = pymongo.MongoClient("mongodb+srv://JMaki:helpmeplease@nprhatesus.yghzs.mongodb.net/npr?retryWrites=true&w=majority")
db = client.test
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
