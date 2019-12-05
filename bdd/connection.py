import mysql.connector
from mysql.connector import Error

class Connection:
    """Class connection db""" 
    
    def __init__(self):
        """Connection information"""
        
        self.host = 'localhost'
        self.database ='openfood'
        self.user = 'root'
        self.password = ''

    def connect(self):
        """Connection method"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host, 
                user=self.user, 
                password=self.password
                )
        
        except mysql.connector.Error as error:
            print(error)

        finally:
            if (self.connection.is_connected()):
                print("Bonjour vous êtes connectés!")

    def create_cursor(self):
        return self.connection.cursor()

    def commit(self):
        return self.connection.commit()
