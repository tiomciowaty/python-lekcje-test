# products.py

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

# Dostępne produkty
bread = Product("Chleb", 10, 2.50)
apples = Product("Jabłka", 20, 1.80)
milk = Product("Mleko", 15, 3.20)
cheese = Product("Ser", 8, 5.50)