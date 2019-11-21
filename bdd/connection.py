import mysql.connector
from mysql.connector import Error

class Connection:
     
    def __init__(self):
        self.host = 'localhost'
        self.database ='openfood'
        self.user = 'root'
        self.password = ''

    def connect(self):
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
