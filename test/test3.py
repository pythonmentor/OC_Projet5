import requests

mots_clef = ["product_name_fr", "nutrition_grade_fr", "id", "brands", "stores"]

liste_de_catégories = ['pizzas', 'fromages', 'biscuits et gâteaux', 'yaourts']

class Product:
    def __init__(self, **article):
        self.product_name_fr = article['product_name_fr']
        self.stores = article['stores']
        self.nutrition_grade_fr = article['nutrition_grade_fr']
        self.id = article['id']
        self.brands = article['brands']
    
    @classmethod
    def is_valid(cls, article):
        is_valid = True
        for mot in mots_clef:
      
      # On vérifie que le dictionnaire contient la clé
            if mot not in article:
                is_valid = False
                break
      
      # On vérifie que ça contient un truc
            if not article[mot]:
                is_valid = False
                break

        return is_valid

            
class ProductDownloader:
    def __init__(self):
        self.url = 'https://fr.openfoodfacts.org/cgi/search.pl'

    def product_by_category(self, category):

        parametres = {
            "action": "process",
            "json": 1,
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": category,
            "page_size": 20
            }

        reponse = requests.get(self.url, params=parametres)
        return reponse.json()

    
    def filter_product(self, product_list):
        produits_triés = []
        for article in product_list['products']:
            if Product.is_valid(article):
              produits_triés.append(Product(**article))

        return produits_triés


for category in liste_de_catégories:
  print('=' * 100)
  test = ProductDownloader()
  produits = test.product_by_category(category)
  produits_triés = test.filter_product(produits)

  for article in produits_triés:
    print('\n')
    for mot in mots_clef:
      print(mot, ':', vars(article)[mot])
