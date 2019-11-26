from settings.settings import mots_clef, liste_de_catégories
from models.productdownload import ProductDownloader
from models.categorydownloader import CategoryDownloader

from bdd.connection import Connection
from bdd.dbcreate import DbCreate
from bdd.dbadd  import DbAdd

auth = Connection()
auth.connect()

create_db = DbCreate(auth)
create_db.create_database()
create_db.create_table()

category = CategoryDownloader()
all_categories = category.get_category()

add_db = DbAdd(auth)
# Ajoute les categories a la bdd
add_db.add_category(all_categories)
add_db.add_product(all_categories)
print()