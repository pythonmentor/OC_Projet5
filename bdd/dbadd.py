import mysql.connector

class DbAdd:
    
    def __init__(self, connection):
        self.connect = connection
    

    def add_category(self, all_category):
        mySql_insert_query = """INSERT INTO category (name) VALUES (%s)"""
        cursor = self.connect.create_cursor()
        cursor.execute('USE openfood')

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
                    continue

                for store in product.stores.split(","):                    
                    query = "INSERT INTO openfood.store (name) VALUES (%s) ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id), name=name"                    
                    cursor.execute(query, (store.strip().lower(),))
                    query = "INSERT INTO openfood.product_has_store (id_store, id_product) VALUES (LAST_INSERT_ID(), %s)"
                    cursor.execute(query, (product.id,))
                    
            
            self.connect.commit()
