import products
from store import Store

def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    store_products = best_buy.get_all_products()

    print(best_buy.get_total_quantity())
    print(best_buy.order([(store_products[0], 1), (store_products[1], 2)]))

if __name__ == "__main__":
    main()