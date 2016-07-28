"""
<<<<<<< HEAD
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
	def get_fav(self):
		print "ace 1"
		return self.load_view('myindex.html')
		
	def get_query(self):
		query = "select trips.name, trips.start_date, trips.end_date, trips.rating, trips.trip_miles from users right join favorites on users.id = favorites.user_id right join trips on favorites.trip_id = trips.id where users.id = 1;"
		x = self.db.query_db(query)
		print x
		return self.load_view('index.html',miles = x)
		
	def maps(self):
		return self.load_view('mymap.html')
#===================================
	def detailed_trip_routing(self):
		return redirect('/detailed_trip')
		
	def detailed_trip(self):
		query="select trips.name, trips.start_date, trips.end_date, trips.rating, trips.trip_miles,trips.start_location from users right join favorites on users.id = favorites.user_id right join trips on favorites.trip_id = trips.id where users.id = 1;"
		#query = "select trips.name, trips.start_date, trips.end_date, trips.rating, trips.trip_miles from users right join favorites on users.id = favorites.user_id right join trips on favorites.trip_id = trips.id where users.id = 1;"
		y = self.db.query_db(query)
		return self.load_view('myviews.html',miles = y)
#=======================================
	def get_place(self): 
		city = request.form['user_input'].replace('  ', ' ')
		url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + city +"&key=AIzaSyCt4WJW2ouRdf_RDR-FnJkcuhVlQrzsexw"
		response = requests.get(url).content
		x =  response
			
		return response
		
	
		
#=================================================MAX=====================================#
# dashbnoard controllers

    def dashboard(self):
        # redirect user to login if session doesnt exist
   #   if not 'id' in session:
           # flash("You must first log in to access the site")
           # return redirect('/')
        #else:
         #   return self.load_view('dashboard.html')
		 return self.load_view('dashboard.html')

    def viewmilestraveled(self):
		
        # redirect user to login if session doesnt exist
       # if not 'id' in session:
        #    flash("You must first log in to access the site")
            #return redirect('/')
        #else:
         return self.load_view('milestraveled.html')

    def tripsbydate(self):

        # redirect user to login if session doesnt exist
        #if not 'id' in session:
            #flash("You must first log in to access the site")
            #return redirect('/')
        #else:
        allTrips = self.models['WelcomeModel'].getAllTrips()
        allParticipants = self.models['WelcomeModel'].getAllParticipants()

        return self.load_view('tripsbydate.html', allTrips=allTrips, allParticipants=allParticipants)


    def milestraveled(self):
        # redirect user to login if session doesnt exist
        #if not 'id' in session:
            #flash("You must first log in to access the site")
            #return redirect('/')
        #else:
        return self.load_view('milestraveleddefault.html')

    def calculatemilestraveled(self):

        # redirect user to login if session doesnt exist
       # if not 'id' in session:
            #flash("You must first log in to access the site")
            #return redirect('/')
        #else:

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
