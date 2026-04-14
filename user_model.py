def create_user(email, password_hash):
    user = {
        'email': email,
        'password': password_hash,
        'created_at': datetime.now()
    }
    db.users.insert_one(user)
    return user
