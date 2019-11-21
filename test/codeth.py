import requests

class Product:
    def __init__(self, product_name, categories, stores, nutrition_grade_fr, url, **kwargs):
        # TODO 
        raise NotImplementedError("à implémenter")

    @classmethod
    def is_valid(cls, data):
        # TODO: returns True if the product is valid or False otherwise.
        raise NotImplementedError("à implémenter")

class ProductDownloader:
    def __init__(self):
        self.url = 'https://fr.openfoodfacts.org/cgi/search.pl'

    def get_products_by_category(self, quantity, category):
        """Returns a list of products by category."""
        payload = {
            "action": "process",
            "json": 1,
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": category,
            "page_size": quantity if quantity < 1000 else 1000
        }
        response = requests.get(
            self.url,
            params=payload
        )
        products = response.json()['products']

        # return [
        #     Product(**data) for data in products
        #     if Product.is_valid(data)
        # ]

        print(products)

test = ProductDownloader()
test.get_products_by_category(0, 'pizzas')
