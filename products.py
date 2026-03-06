class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self.quantity:
            raise ValueError("Not enough stock")

        self.set_quantity(self.quantity - quantity)
        return self.price * quantity

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
