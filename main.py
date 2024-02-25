# main.py

from orders import Order

if __name__ == "__main__":
    print("Witaj w symulatorze sklepu!")
    print("Dostępne produkty: Chleb, Jabłka, Mleko, Ser")
    print("Aby zakończyć, wpisz 'koniec' jako nazwę produktu.")

    orders = []
    while True:
        product_name = input("Podaj nazwę produktu: ")
        if product_name.lower() == "koniec":
            break
        quantity = int(input("Podaj ilość: "))
        order = Order(product_name, quantity)
        orders.append(order)

    total_cost = sum(order.calculate_total_price() for order in orders)
    print(f"Łączny koszt zakupów wynosi: {total_cost:.2f} zł")