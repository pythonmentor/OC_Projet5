import mysql.connector

class DbAdd:
    
    def __init__(self, connection):
        self.connect = connection
    

    def add_category(self, all_category):
        mySql_insert_query = """INSERT INTO category (name) VALUES (%s)"""
        cursor = self.connect.create_cursor()
        for category in all_category:
            try:
                cursor.execute(mySql_insert_query, (category.name,))
                self.connect.commit()
            except mysql.connector.errors.IntegrityError:
                # Add logging here
                pass

    def add_product(self, all_category):
        mySql_insert_query = """INSERT INTO product (product_name_fr, nutrition_grade_fr, id, brands, id_category) VALUES (%s, %s, %s, %s, %s)"""
        cursor = self.connect.create_cursor()
        for category in all_category:
            query = "SELECT id FROM category WHERE category.name LIKE %s"
            cursor.execute(query, (category.name,))
            cat_id = cursor.fetchone()

            for product in category.products:
                try:
                    cursor.execute(mySql_insert_query, (product.product_name_fr[:499], product.nutrition_grade_fr, product.id, product.brands, cat_id[0]))
                except mysql.connector.errors.IntegrityError:
                    # Add logging here
                    pass

            self.connect.commit()
