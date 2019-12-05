

class Category:
    """"""
    
    def __init__(self):
        self.name = ""
        self.products = []
    
    @property
    def count(self):
        return len(self.products)
    
    def __repr__(self):
        return f"Category({self.name})"