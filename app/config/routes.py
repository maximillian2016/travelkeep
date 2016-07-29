"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes

    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Welcome'
routes['POST']['/logincheck']='Welcome#logincheck'
routes['POST']['/regcheck']='Welcome#regcheck'
routes['GET']['/register']='Welcome#register'
routes['GET']['/login']='Welcome#login'
routes['GET']['/dashboard']='Welcome#dashboard'
routes['GET']['/logout']='Welcome#logout'
routes['GET']['/tripsbydate'] = 'Welcome#tripsbydate'
routes['POST']['/fbcheck'] = 'Welcome#fbcheck'
routes['GET']['/milestraveled']='Welcome#milestraveled'
routes['POST']['/calculatemilestraveled']='Welcome#calculatemilestraveled'
routes['POST']['/createtrip'] = 'Welcome#createtrip'
routes['POST']['/upload/photo'] = 'Welcome#upload_photo'
routes['POST']['/upload/video'] = 'Welcome#upload_video'
routes['POST']['/addtrip'] = 'Welcome#add_trip'
