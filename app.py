from settings.settings import mots_clef, liste_de_catégories
from models.productdownload import ProductDownloader
from models.categorydownloader import CategoryDownloader

from bdd.connection import Connection
from bdd.dbwrite import DbWrite

auth = Connection()
auth.connect()

create_db = DbWrite(auth)
create_db.create_database()
create_db.create_table()

#   for article in produits_triés:
#     print('\n')
#     for mot in mots_clef:
#       print(mot, ':', vars(article)[mot])

category = CategoryDownloader()
all_categories = category.get_category()
print()
