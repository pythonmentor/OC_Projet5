import requests

mots_clef = ["product_name_fr", "nutrition_grade_fr", "id", "brands", "stores"]

url = 'https://fr.openfoodfacts.org/cgi/search.pl'
#liste_de_catégories = ['pizzas', 'fromages', 'biscuits et gâteaux', 'yaourts']

for catégorie in liste_de_catégories:
  print('=' * 100)
  parametres = {
          "action": "process",
          "json": 1,
          "tagtype_0": "categories",
          "tag_contains_0": "contains",
          "tag_0": catégorie,
          "page_size": 20
      }

  reponse = requests.get(url, params=parametres)
  produits = reponse.json()

  # On veut afficher pour chaque produit, certaines données :
  # product_name_fr, nutrition_grade_fr, id, 

  # On utilise une boucle:
  # pour chaque (élément:variable) dans object
  # for article in produits['products']:

  # Boucle qui trie les produits
  # Entrée : liste de produits

  # produits = {
  #   'products':
  #     [
  #       {
  #       'nutrition_grade_fr' : 'a',
  #       'product_name_fr' : 'test',
  #       'id': 45
  #       },
  #       {
  #       'nutrition_grade_fr' : 'r',
  #       'product_name_fr' : 'test2',
  #       'id' : 80
  #       }
  #     ]
  #   }

  def is_valid(article):
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

  produits_triés = []
  for article in produits['products']:
    if is_valid(article):
      produits_triés.append(article)

  # Sortie : liste de produits triés

  # print(produits_triés)
  # Boucle qui affiche les données
  for article in produits_triés:
    print('\n')
    for mot in mots_clef:
      print(mot, ':', article[mot])
