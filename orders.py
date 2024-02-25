# orders.py

from products import bread, apples, milk, cheese

class Order:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity

    def calculate_total_price(self):
        product = None
        if self.product_name == "Chleb":
            product = bread
        elif self.product_name == "Jabłka":
            product = apples
        elif self.product_name == "Mleko":
            product = milk
        elif self.product_name == "Ser":
            product = cheese

        if product:
            total_price = product.price * self.quantity
            return total_price
        else:
            return 0

if __name__ == "__main__":
    orders = []
    while True:
        product_name = input("Podaj nazwę produktu (Chleb, Jabłka, Mleko, Ser): ")
        if product_name.lower() == "koniec":
            break
        quantity = int(input("Podaj ilość: "))
        order = Order(product_name, quantity)
        orders.append(order)

    total_cost = sum(order.calculate_total_price() for order in orders)
    print(f"Łączny koszt zakupów wynosi: {total_cost:.2f} zł")