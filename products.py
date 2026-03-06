class Product:
    """Represents a product in the store inventory."""

    def __init__(self, name, price, quantity):
        """Create a product with name, price, quantity; set active state; validate inputs."""
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
        """Return current product quantity."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Set product quantity and deactivate when quantity reaches zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return whether the product is active."""
        return self.active

    def activate(self) -> None:
        """Activate the product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivate the product."""
        self.active = False

    def buy(self, quantity: int) -> float:
        """Buy quantity units and return total price; decrease stock; deactivate if stock hits 0."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self.quantity:
            raise ValueError("Not enough stock")

        self.set_quantity(self.quantity - quantity)
        return self.price * quantity

    def show(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
