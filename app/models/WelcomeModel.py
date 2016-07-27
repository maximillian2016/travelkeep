""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
from datetime import datetime

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

    def milestraveled(self, trip_info):
        sum =0;
        milesforeachmonth=[];
        i=1
        while i<13:
            milesforeachmonth.append(0);
            i= i+1
        #SELECT * from trips join favorites on trips.id = favorites.trip_id join users on users.id=favorites.user_id where users.id =1#    
        totmilestraveled_query ="SELECT * from trips join favorites on trips.id = favorites.trip_id join users on users.id=favorites.user_id where users.id =:user_id and trips.start_date BETWEEN :startdate and :enddate AND trips.rating =:triprating"
        totmilestraveled_data = {'startdate': trip_info['start_date'], 'enddate': trip_info['end_date'], 'triprating': trip_info['rating'], 'user_id': trip_info['user_id']}
        totmilestraveled = self.db.query_db(totmilestraveled_query, totmilestraveled_data)
        print "this is totmilestraveled", totmilestraveled
        for element in totmilestraveled:
            for i in range(0,12):
                if element['end_date'].month == i+1:
                    milesforeachmonth[i]= milesforeachmonth[i]+ int(element['trip_miles'])
        print "This is the milesforeachmonth array ", milesforeachmonth           
        for element in totmilestraveled:
            sum = sum + element['trip_miles']
        return milesforeachmonth

    def placesvisited(self, trip_info):
        #SELECT * from trips join favorites on trips.id = favorites.trip_id join users on users.id=favorites.user_id where users.id =1#    
        placesvisited_query ="SELECT end_location from trips join favorites on trips.id = favorites.trip_id join users on users.id=favorites.user_id where users.id =:user_id and trips.start_date BETWEEN :startdate and :enddate AND trips.rating =:triprating"
        placesvisited_data = {'startdate': trip_info['start_date'], 'enddate': trip_info['end_date'], 'triprating': trip_info['rating'], 'user_id': trip_info['user_id']}
        placesvisited = self.db.query_db(placesvisited_query, placesvisited_data)
        print "this is places visited", placesvisited
        return placesvisited

  
          