import products
import store


def print_menu() -> None:
    print("\nStore Menu")
    print("-----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(best_buy: store.Store) -> None:
    for i, product in enumerate(best_buy.get_all_products(), start=1):
        print(f"{i}. {product.show()}")


def show_total_amount(best_buy: store.Store) -> None:
    total = best_buy.get_total_quantity()
    print(f"Total amount in store: {total}")


def get_shopping_list(best_buy: store.Store):
    shopping_list = []
    all_products = best_buy.get_all_products()

    if not all_products:
        print("No active products available.")
        return shopping_list

    for i, product in enumerate(all_products, start=1):
        print(f"{i}. {product.show()}")

    while True:
        product_number = input("Enter product number to buy (or empty to finish): ").strip()
        if product_number == "":
            break

        try:
            product_index = int(product_number) - 1
            if product_index < 0 or product_index >= len(all_products):
                print("Invalid product number.")
                continue

            quantity = int(input("Enter quantity: ").strip())
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue

            product = all_products[product_index]
            if quantity > product.get_quantity():
                print(f"Not enough stock for {product.name}. Available: {product.get_quantity()}.")
                continue

            shopping_list.append((product, quantity))
        except ValueError:
            print("Please enter valid numeric values.")

    return shopping_list


def make_order(best_buy: store.Store) -> None:
    shopping_list = get_shopping_list(best_buy)
    if not shopping_list:
        print("No items were ordered.")
        return

    try:
        total_price = best_buy.order(shopping_list)
        print(f"Order cost: {total_price} dollars.")
    except ValueError as error:
        print(f"Could not complete order: {error}")


def start(best_buy: store.Store):
    while True:
        print_menu()
        choice = input("Please choose a number: ").strip()

        if choice == "1":
            list_products(best_buy)
        elif choice == "2":
            show_total_amount(best_buy)
        elif choice == "3":
            make_order(best_buy)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)
    start(best_buy)
