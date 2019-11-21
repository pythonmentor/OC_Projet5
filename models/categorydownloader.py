from models.category import Category
from models.productdownload import ProductDownloader

from settings.settings import mots_clef, liste_de_catégories

class CategoryDownloader:
    def __init__(self):
        pass
    
    def get_category(self):
        all_category = []
        for category in liste_de_catégories:
            cat = Category()
            cat.name = category
            get_products = ProductDownloader()
            products = get_products.product_by_category(category)
            cat.products = get_products.filter_product(products)
            all_category.append(cat)
        
        return all_category