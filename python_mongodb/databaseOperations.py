import pymongo

connection = pymongo.MongoClient('localhost', 27017)

database = connection['mydb_01']

collection = database['mycol_01']

data = {'Name': 'Aarushi'}

collection.insert_one(data)