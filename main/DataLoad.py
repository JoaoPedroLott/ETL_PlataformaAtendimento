import pymongo
import os


def get_database():
    client = pymongo.MongoClient(os.environ['MONGO_URL'])
    # client = pymongo.MongoClient('mongodb://root:root@localhost:27017/')
    return client['Elo']


def quit_database(client):
    client.close()


def insert(item):
    db = get_database()
    collection = db["DadosAtendimento"]
    collection.insert_one(item)
    # quit_database(db)
