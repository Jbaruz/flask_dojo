from flask_crud.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        print(data)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data
    
    
    @classmethod
    def add_ninja(cls, data):
        query = f"INSERT INTO ninjas (first_name, last_name, age,dojo_id,created_at,updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s,NOW(),NOW());" 
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        print("aqui--->", data)
        print("quiero ver results--->", results)
        return results
    

