"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db
    def index(self):
        return self.load_view('index.html')
    def logincheck(self):
        user_info = {
             "email" : request.form['loginemail'],
             "password" : request.form['loginpassword'],
        }
        login_status = self.models['WelcomeModel'].login_user(user_info)
        if login_status['status'] == True:
            session['id'] = login_status['user']['id']
            session['name']= login_status['user']['first_name']
            session['loggedin'] =1
            return redirect('/dashboard')
        else:
            for message in login_status['errors']:
                flash(message, 'login_errors')
            return redirect('/login')
    
    def login(self):
        return self.load_view('login.html')

    def register(self):
        return self.load_view('register.html')

    def regcheck(self):
        user_info = {
             "first_name" : request.form['firstname'],
             "last_name" : request.form['lastname'],
             "email" : request.form['regemail'],
             "password" : request.form['regpassword'],
             "pw_confirmation" : request.form['regconfpassword']
        }

        create_status = self.models['WelcomeModel'].create_user(user_info)
        if create_status['status'] == True:
            session['id'] = create_status['user']['id'] 
            session['name'] = create_status['user']['first_name']
            session['loggedin'] =1
            return redirect('/dashboard')
        else:
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/register')    


    def logout(self):
        session.clear()
        return self.load_view('index.html')

    def dashboard(self):
        return self.load_view('dashboard.html')
    
    def milestraveled(self):
        return self.load_view('milestraveleddefault.html')

    def calculatemilestraveled(self):
        trip_info = { 
            "start_date": request.form['startdate'],
            "end_date": request.form['enddate'],
            "rating": request.form['rating'],
            "user_id": session['id']
            }
        session['start_date'] = trip_info['start_date']
        session['end_date'] = trip_info['end_date']
        session['rating'] = trip_info['rating']
        milestraveled = self.models['WelcomeModel'].milestraveled(trip_info)
        placesvisited = self.models['WelcomeModel'].placesvisited(trip_info)
        pruned_places_visited=[]
        for element in placesvisited:
            if element not in pruned_places_visited:
                pruned_places_visited.append(element)
        return self.load_view('milestraveled.html', milestraveled = milestraveled, pruned_places_visited=pruned_places_visited)    


    



