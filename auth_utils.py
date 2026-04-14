import bcrypt
from datetime import datetime

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password, hash):
    return bcrypt.checkpw(password.encode(), hash)
