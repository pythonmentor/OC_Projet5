from settings.settings import mots_clef, liste_de_catégories
from models.productdownload import ProductDownloader
from models.categorydownloader import CategoryDownloader

from bdd.connection import Connection
from bdd.dbcreate import DbCreate
from bdd.dbadd  import DbAdd
from bdd.dbreading import DbReading

auth = Connection()
auth.connect()


# Creation of the comic, creation of the tables
create_db = DbCreate(auth)
print('On crée la base de données !')
create_db.create_database()
print('On crée les tables !')
create_db.create_table()

# Download the categories then the ranges
category = CategoryDownloader()
print('On télécharge les catégories et les produits !')
all_categories = category.get_category()

add_db = DbAdd(auth)
# Add the categories to the database

print('On ajoute les catégories en base de données !')
add_db.add_category(all_categories)
print('On ajoute les produits de chaque catégorie en base de données !')
add_db.add_product(all_categories)

"""
# Reading the db
db_read = DbReading(auth)
db_read.get_all_categories()
db_read.get_category_products(4)
"""
