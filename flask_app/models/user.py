
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class User:
    db = "users_two_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Users Models

    @classmethod
    def create_user(cls, user_info):
        query = """
        INSERT INTO users_two (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s)
        ;"""
        results = connectToMySQL(cls.db).query_db(query, user_info)
        return int(results)
        print(results)

    # Read Users Models

    @classmethod
    def get_user_by_id(cls, id):
        data = { 'id' : id }
        query = """
        SELECT * 
        FROM users_two
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
        print(results)


    @classmethod
    def get_all_users(cls):
        query = """
        SELECT *
        FROM users_two
        ;"""
        results_all = connectToMySQL(cls.db).query_db(query)
        users = []
        for user1 in results_all:
            users.append(cls(user1))
        print('list of persons', results_all)
        print('list of instances', users)
        return users
        
        
        
    # Update Users Models

    @classmethod
    def update_user(cls, user_data):
        query = """
        UPDATE users_two 
        SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, user_data)
        print(query)
        return


    # Delete Users Models
    
    @classmethod
    def delete_user_by_id(cls, id):
        data = { 'id' : id }
        query = """
        DELETE FROM users_two
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return