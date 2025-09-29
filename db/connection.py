from pymongo import MongoClient

def get_database():
    # conecta ao mongodb local (padrão)
    client = MongoClient("mongodb://localhost:27017/")
    return client["meu_banco"]
