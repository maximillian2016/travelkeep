"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()
    def login_user(self, user_info):
        errors=[]
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user_data = {'email': user_info['email']}
        user = self.db.query_db(user_query, user_data)
        if user:
           # check_password_hash() compares encrypted password in DB to one provided by user logging in
            if self.bcrypt.check_password_hash(user[0]['password'], user_info['password']):
                return {"status": True, "user": user[0]}
        errors.append('User was not found in database. Please try a different user name/password combination or click on register below')
        # Whether we did not find the email, or if the password did not match, either way return False
        return {"status": False, "errors": errors}

    def create_user(self, info):
        # We write our validations in model functions.
        # They will look similar to those we wrote in Flask
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        if not info['first_name']:
            errors.append('First name cannot be blank')
        if not info['last_name']:
            errors.append('Last name cannot be blank')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif info['password'] != info['pw_confirmation']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        if errors:
            return {"status": False, "errors": errors}
        else:
            password = info['password']
        # bcrypt is now an attribute of our model
        # we will call the bcrypt functions similarly to how we did before
        # here we use generate_password_hash() to generate an encrypted password
            email = info['email']
            user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            query_data = { 'email': email }
            user = self.db.query_db(user_query, query_data)
            if user != []:
                errors.append("An account is already associated with that e-mail address, please login instead")
                return {"status": False, "errors": errors}
            else:
                user_query ="SELECT * FROM users LIMIT 1"
                user = self.db.query_db(user_query)
                if user !=[]:
                    hashed_pw = self.bcrypt.generate_password_hash(password)
                    create_query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :password, NOW())"
                    create_data = {'first_name': info['first_name'], 'last_name': info['last_name'], 'email': info['email'], 'password': hashed_pw, 'share_w_friends': 0}
                    self.db.query_db(create_query, create_data)# Code to insert user goes here...
            # Then retrieve the last inserted user.
                    get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
                    users = self.db.query_db(get_user_query)
                    return { "status": True, "user": users[0] }
                else:
                    hashed_pw = self.bcrypt.generate_password_hash(password)
                    create_query = "INSERT INTO users (first_name, last_name, email, password, share_w_friends, created_at) VALUES (:first_name, :last_name, :email, :password, :share_w_friends, NOW())"
                    create_data = {'first_name': info['first_name'], 'last_name': info['last_name'], 'email': info['email'], 'password': hashed_pw, 'share_w_friends': 0}
                    self.db.query_db(create_query, create_data)# Code to insert user goes here...
            # Then retrieve the last inserted user.
                    get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
                    users = self.db.query_db(get_user_query)
                    return { "status": True, "user": users[0] }

    def get_all_users(self):
        return self.db.query_db("SELECT id, first_name, last_name, email, user_level, created_at FROM users ORDER BY created_at DESC")

    def get_user_by_id(self, user_id):
        # pass data to the query like so
      query = "SELECT id, first_name, last_name, email FROM users WHERE id = :user_id"
      data = { 'user_id': user_id}
      return self.db.query_db(query, data)
     #begin update_user no validation
    #def update_user(self, user):
      # Building the query for the update
      #query = "UPDATE users SET first_name=:first_name, last_name=:last_name, email=:email, user_level=:user_level WHERE id = :user_id"
      # we need to pass the necessary data
      #data = {'first_name': user['first_name'], 'last_name': user['last_name'], 'email': user['email'], 'user_id': user['id'], 'user_level': user['user_level']}
      # run the update
      #return self.db.query_db(query, data)
      #end update_user no validation

    def getAllTrips(self):
        query = "SELECT * FROM trips ORDER BY start_date DESC"
        return self.db.query_db(query)


    def getAllParticipants(self):
        query = "SELECT p.*, u.first_name, u.last_name FROM participants p JOIN users u ON p.user_id = u.id"
        return self.db.query_db(query)
