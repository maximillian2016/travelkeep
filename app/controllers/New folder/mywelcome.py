from system.core.controller import *

class Welcome(Controller):
	def __init__(self, action):
		super(Welcome, self).__init__(action)
		self.load_model('WelcomeModel')
		self.db = self._app.db
	
	def index(self):
		return self.load_view('index.html')	
	def get_fav(self):
		print "ace 1"
		return self.load_view('index.html')
	def test(self,x,y,z):
		print "this is {} and {} and {}".format(x,y,z)
		x = 1
		y = 2
		z = 3
		return self.load_view('index.html',start_date = x,end_date = y,miles = z)
	def another_round(self):
		print "this works ok. "
		return redirect ('/')
	def process(self):
		x = request.args.get('get_fav_textbox')
		print x
		return self.load_view('index.html',start_date = x)
	def get_query(self):
		#query = "select users.first_name, trips.name, trips.start_date, trips.end_date, trips.trip_miles, trips.rating from users  right join favorites on users.id = favorites.user_id right join trips on favorites.trip_id = trips.id where users.first_name like 'norman';"
		query = "select trips.name, trips.start_date, trips.end_date, trips.rating, trips.trip_miles from users right join favorites on users.id = favorites.user_id right join trips on favorites.trip_id = trips.id where users.id = 1;"
		x = self.db.query_db(query)
		print x
		return self.load_view('index.html',miles = x)
	def maps(self):
		return self.load_view('map.html')
	def detailed_trip_routing(self):
		return redirect('/detailed_trip')
	def detailed_trip(self):
		query="select trips.name, trips.start_date, trips.end_date, trips.rating, trips.trip_miles,trips.start_location from users right join favorites on users.id = favorites.user_id right join trips on favorites.trip_id = trips.id where users.id = 1;"
		#query = "select trips.name, trips.start_date, trips.end_date, trips.rating, trips.trip_miles from users right join favorites on users.id = favorites.user_id right join trips on favorites.trip_id = trips.id where users.id = 1;"
		y = self.db.query_db(query)
		return self.load_view('test.html',miles = y)
	def get_place(self): 
		city = request.form['user_input'].replace('  ', ' ')
		url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + city +"&key=AIzaSyCt4WJW2ouRdf_RDR-FnJkcuhVlQrzsexw"
		response = requests.get(url).content
		x =  response
			
		return response