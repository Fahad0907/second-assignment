class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.data = {}
    
    def get_profile(self):
        return self.data
    
    def update_profile(self, data):
        self.data.update(data)
        return self.data
