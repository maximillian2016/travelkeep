"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()

    def getAllTrips(self):
        query = "SELECT * FROM trips ORDER BY start_date DESC"
        return self.db.query_db(query)


    def getAllParticipants(self):
        query = "SELECT p.*, u.first_name, u.last_name FROM participants p JOIN users u ON p.user_id = u.id"
        return self.db.query_db(query)

        
