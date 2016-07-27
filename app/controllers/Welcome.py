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

# login controllers
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
            session['picture'] = login_status['user']['picture']
            session['loggedin'] =1
            return redirect('/dashboard')
        else:
            for message in login_status['errors']:
                flash(message, 'login_errors')
            return redirect('/')

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
            session['picture'] = create_status['user']['picture']
            session['loggedin'] =1
            return redirect('/dashboard')
        else:
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')

    def fbcheck(self):
        fb_user_info = {
             "FBid" : request.form['FBid'],
             "FBtoken" : request.form['FBtoken'],
             "FBfirst_name" : request.form['FBfirst_name'],
             "FBlast_name" : request.form['FBlast_name'],
             "FBemail" : request.form['FBemail'],
             "FBpicture" : request.form['FBpicture']
        }

        # run fb login or register fb user
        fbcheck_status = self.models['WelcomeModel'].fb_login(fb_user_info)

        if fbcheck_status['status'] == True:
            session['id'] = fbcheck_status['user']['id']
            session['name'] = fbcheck_status['user']['first_name']
            session['picture'] = fbcheck_status['user']['picture']
            session['loggedin'] =1
            session['token'] = fbcheck_status['token']
            session['untoken'] = request.form['FBtoken']
            print "the token is:"
            print session['token']
            return redirect('/dashboard')
        else:
            for message in fbcheck_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')





    def logout(self):
        session.clear()
        return self.load_view('index.html')


# dashbnoard controllers

    def dashboard(self):
        return self.load_view('dashboard.html')

    def viewmilestraveled(self):
        return self.load_view('milestraveled.html')

    def tripsbydate(self):

        if not 'id' in session:
            flash("You must first log in to access the site")
            return redirect('/')
        else:
            allTrips = self.models['WelcomeModel'].getAllTrips()
            allParticipants = self.models['WelcomeModel'].getAllParticipants()

            return self.load_view('tripsbydate.html', allTrips=allTrips, allParticipants=allParticipants)
