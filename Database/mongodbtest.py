import pymongo

client = pymongo.MongoClient("mongodb+srv://kdabi:8009@cluster0.np7eg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
mydb = client["mydatabase"]
mycol = mydb["customers"]

my_dict = {
    'name': 'kamlesh',
    'email': 'dabikamlesh@gmail.com',
    'surname': 'dabi'
}
x = mycol.insert_one(my_dict)