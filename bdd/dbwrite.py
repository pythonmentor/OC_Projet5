
class DbWrite:

    def __init__(self, connection):
        self.connect = connection

    def create_database(self):

        cursor = self.connect.create_cursor()
        create_query = """
                        CREATE DATABASE IF NOT EXISTS openfood CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
                        """

        result = cursor.execute(create_query)

    def create_table(self):
        cursor = self.connect.create_cursor()
        create_query = """
                        CREATE TABLE IF NOT EXISTS category ( 
                        id SMALLINT USIGNED NOT NULL AUTO_INCREMENT,
                        name VARCHAR(100) NOT NULL,                        
                        PRIMARY KEY (id)
                        );                        
                        """
        cursor.execute(create_query)

        create_query = """
                        CREATE TABLE IF NOT EXISTS product ( 
                        id SMALLINT USIGNED NOT NULL AUTO_INCREMENT,
                        name VARCHAR(100) NOT NULL,                        
                        brands VARCHAR(80) NOT NULL,
                        stores VARCHAR(100) NOT NULL,
                        score VARCHAR(10) NOT NULL,
                        bar_code INT(10) NOT NULL,
                        PRIMARY KEY (bar_code)
                        );                        
                        """
        cursor.execute(create_query)

        create_query =  """
                        CREATE TABLE IF NOT EXISTS favorite ( 
                        id SMALLINT USIGNED NOT NULL AUTO_INCREMENT,
                        name VARCHAR(100) NOT NULL,                        
                        brands VARCHAR(80) NOT NULL,
                        stores VARCHAR(100) NOT NULL,
                        score VARCHAR(10) NOT NULL,
                        bar_code INT(10) NOT NULL,
                        PRIMARY KEY (bar_code)
                        );                        
                        """
        cursor.execute(create_query)

        create_query = """
                        CREATE TABLE IF NOT EXISTS stores ( 
                        id SMALLINT USIGNED NOT NULL AUTO_INCREMENT,
                        name VARCHAR(100) NOT NULL,                                                
                        PRIMARY KEY (id)
                        );                        
                        """
        cursor.execute(create_query)
