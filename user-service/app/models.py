from werkzeug.security import generate_password_hash, check_password_hash

def insert_user(db, username, password):
    hashed = generate_password_hash(password)
    return db.users.insert_one({"username": username, "password": hashed})

def find_user(db, username):
    return db.users.find_one({"username": username})

def verify_password(user_doc, password_plain):
    return check_password_hash(user_doc["password"], password_plain)
