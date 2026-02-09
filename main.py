from products import Product

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))     # 12500
print(mac.buy(100))     # 145000
print(mac.is_active())  # False (quantity is now 0)

print(bose.show())
print(mac.show())

bose.set_quantity(1000)
print(bose.show())