from flask_crud.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        all_dojos = []
        if len(results) == 0:
            return None
        for data in results:
            all_dojos.append(cls(data))
        return all_dojos
    
    @classmethod
    def insert_dojo(cls, data):
        query = f"INSERT INTO dojos (name,created_at,updated_at)VALUES(%(name)s,NOW(),NOW());"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
        print (results)
        return results
    
    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM dojos WHERE id = %(id)s;"
        data = {'id': id}   
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        return cls(results[0])if len(results)> 0 else None
