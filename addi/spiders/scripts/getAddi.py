import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["addi"]
mycol = mydb["tfgs"]

#for x in mycol.find( {} , { "dc-identifier-uri": 1, "dc-date-issued": 1, "date": 1} ).sort([("date", -1)]):
for x in mycol.find( {}, { '_id': 0} ).sort([("date", -1)]):
  print(x)
