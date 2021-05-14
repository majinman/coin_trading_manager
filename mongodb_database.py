from pymongo import MongoClient
client = MongoClient('localhost:27017',
                  username='root',
                 password='KEY')

db = client.coinsys

# print("db: ", db.portfolio.find())



if __name__ == '__main__':
    print("db: ", db.portfolio.find())
    for res in db.portfolio.find():
        print("res: ", res)
