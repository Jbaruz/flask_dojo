from flask_crud.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojos.id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data
    
    
    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(id)s;" 
        data = {'id': id }
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        return cls(results[0])if len(results) > 0 else None
    

