
class DbCreate:

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

        cursor.execute("USE `openfood`")

        create_query = """
                        CREATE TABLE IF NOT EXISTS `openfood`.`category` (
                        id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                        name VARCHAR(100) NOT NULL,            
                        PRIMARY KEY (id))
                        """
        cursor.execute(create_query)

        create_query = """
                        CREATE TABLE IF NOT EXISTS `openfood`.`store` ( 
                        id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                        name VARCHAR(100) NOT NULL,                                                
                        PRIMARY KEY (id)
                        );                        
                        """
        cursor.execute(create_query)

        create_query = """
                        CREATE TABLE IF NOT EXISTS `openfood`.`product` ( 
                        id INT UNSIGNED NOT NULL,
                        id_category SMALLINT UNSIGNED NOT NULL,                                                
                        product_name_fr VARCHAR(100) NOT NULL,                        
                        brands VARCHAR(80) NOT NULL,
                        id_stores SMALLINT UNSIGNED NOT NULL,
                        nutrition_grade_fr VARCHAR(10) NOT NULL,
                        PRIMARY KEY (id),
                        CONSTRAINT `fk_id_category`
                            FOREIGN KEY (`id_category`) REFERENCES `category` (`id`),
                        CONSTRAINT `fk_id_stores`
                            FOREIGN KEY (`id_stores`) REFERENCES `store` (`id`)
                        );                        
                        """
        cursor.execute(create_query)

        create_query = """
                        CREATE TABLE IF NOT EXISTS `openfood`.`favorite` (
                        id_compared INT UNSIGNED NOT NULL,
                        id_result INT UNSIGNED NOT NULL,
                        PRIMARY KEY (id_compared),
                        CONSTRAINT `fk_id_compared` 
                            FOREIGN KEY (`id_compared`) REFERENCES `product` (`id`),
                        CONSTRAINT `fk_id_result` 
                            FOREIGN KEY (`id_result`) REFERENCES `product` (`id`)
                        );                        
                        """
        cursor.execute(create_query)
