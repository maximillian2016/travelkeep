from system.core.controller import *
import googlemaps
from datetime import datetime

# google api key DO NOT PUSH TO GITHUB
gmaps = googlemaps.Client(key='AIzaSyCTcTq9pMo7BiQGeMYo64S_vElVFRoqVr4')

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
        # redirect user to login if session doesnt exist
        if not 'id' in session:
            flash("You must first log in to access the site")
            return redirect('/')
        else:
            allParticipants = self.models['WelcomeModel'].getAllUsers()

            return self.load_view('dashboard.html', allParticipants=allParticipants)


    def viewmilestraveled(self):
        # redirect user to login if session doesnt exist
        if not 'id' in session:
            flash("You must first log in to access the site")
            return redirect('/')
        else:
            return self.load_view('milestraveled.html')

    def tripsbydate(self):

        # redirect user to login if session doesnt exist
        if not 'id' in session:
            flash("You must first log in to access the site")
            return redirect('/')
        else:
            allTrips = self.models['WelcomeModel'].getAllTrips()
            allParticipants = self.models['WelcomeModel'].getAllParticipants()

            return self.load_view('tripsbydate.html', allTrips=allTrips, allParticipants=allParticipants)


    def milestraveled(self):
        # redirect user to login if session doesnt exist
        if not 'id' in session:
            flash("You must first log in to access the site")
            return redirect('/')
        else:
            return self.load_view('milestraveleddefault.html')

    def calculatemilestraveled(self):

        # redirect user to login if session doesnt exist
        if not 'id' in session:
            flash("You must first log in to access the site")
            return redirect('/')
        else:

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


    def createtrip(self):

        trip_details = request.form

        origins = [trip_details['start_loc']]
        destinations = [trip_details['end_loc']]
        trip_api_info = gmaps.distance_matrix(origins, destinations, mode="driving",units="imperial")

        self.models['WelcomeModel'].add_trip_m(trip_details, trip_api_info)
        return self.load_view('ongoing.html')

    def upload_photo(self):
        file = request.files['photo']
        if file:
            # create random file name
            if not os.path.exists('uploads'):
                os.mkdir('uploads')
            if not os.path.exists('uploads/photos'):
                os.mkdir('uploads/photos')
            salt = uuid.uuid4().hex
            filename = hashlib.md5(str(uuid.uuid4()) + 'iclin294rit').hexdigest()
            up_photo = os.path.join('uploads/photos', filename)
            # file.save(os.path.join('uploads/', filename))
            file.save(up_photo)
            self.models['WelcomeModel'].up_photo_m(up_photo)
            return self.load_view('ongoing.html')

    def upload_video(self):
        file = request.files['video']
        if file:
            # create random file name
            if not os.path.exists('uploads'):
                os.mkdir('uploads')
            if not os.path.exists('uploads/videos'):
                os.mkdir('uploads/videos')
            salt = uuid.uuid4().hex
            filename = hashlib.md5(str(uuid.uuid4()) + 'iclin294rit').hexdigest()
            up_video = os.path.join('uploads/videos', filename)
            print "VVVVVV", up_video
            # file.save(os.path.join('uploads/', filename))
            file.save(up_video)
            self.models['WelcomeModel'].up_video_m(up_video)
            return self.load_view('ongoing.html')

    def add_trip(self):
        pass
