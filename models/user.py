from db.connection import get_database

db = get_database()
users = db["users"]

def create_user(name: str, email: str):
    result = users.insert_one({"name": name, "email": email})
    return str(result.inserted_id)

def list_users():
    return list(users.find({}, {"_id": 0, "name": 1, "email": 1}))

def update_user(name: str, new_email: str):
    result = users.update_one({"name": name}, {"$set": {"email": new_email}})
    return result.modified_count

def delete_user(name: str):
    result = users.delete_one({"name": name})
    return result.deleted_count
