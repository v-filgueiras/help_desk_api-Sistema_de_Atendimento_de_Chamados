class Client:
    def __init__(self,client_id, name, email, age, active = False):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.age = age 
        self.active = active

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "active": self.active
        }