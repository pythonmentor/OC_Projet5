class DbCreate:
    """ create the database """

    def __init__(self):
        """ init username , password , name of the database and connect"""
        self.db_name = DB_NAME
        self.db_username = DB_USER
        self.db_password = DB_PASS
        self.db = records.Database('mysql://{}:{}@localhost'
                                   .format(self.db_username, self.db_password))

    def create_database(self):
        """ create database """
        self.db.query("SET NAMES utf8;")
        self.db.query("DROP DATABASE IF EXISTS {};".format(self.db_name))
        self.db.query("CREATE DATABASE {}".format(self.db_name))
        self.db.query("USE {};".format(self.db_name))

    def create_table(self):
        """ create table User, product, favourite """
        self.db.query("""CREATE TABLE User(\
                      id INT UNSIGNED AUTO_INCREMENT NOT NULL,\
                      username VARCHAR(40) NOT NULL,\
                      pwd VARCHAR(255) NOT NULL,\
                      email VARCHAR(100) NOT NULL,\
                      PRIMARY KEY (id),\
                      UNIQUE KEY username (username)\
                      )ENGINE=InnoDB;""")

        self.db.query("""CREATE TABLE Favourite(\
                      user_id INT UNSIGNED NOT NULL,\
                      name VARCHAR(250) NOT NULL,\
                      url VARCHAR(250),\
                      nutri_score VARCHAR(250) NOT NULL,\
                      stores VARCHAR(200)\
                      )ENGINE=InnoDB;""")

        self.db.query("""CREATE TABLE Product(\
                      id INT UNSIGNED AUTO_INCREMENT NOT NULL,\
                      name VARCHAR(250) NOT NULL,\
                      url VARCHAR(255) NOT NULL,\
                      nutri_score VARCHAR(250) NOT NULL,\
                      category_id INT UNSIGNED NOT NULL,\
                      stores VARCHAR(200) NOT NULL,
                      PRIMARY KEY (id)\
                      )ENGINE=InnoDB;""")

    def add_contents_to_db(self):
        """ add data to the db using DbManagement class """
        DbManagement().init_cat_list()
        DbManagement().init_all_category()


if __name__ == '__main__':
    app = DbCreate()
    app.create_database()
    app.create_table()
    app.add_contents_to_db()