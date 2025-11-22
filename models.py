from typing import List

# ----------------------------- Product Class -----------------------------
class Product:
    """
    Represents a product in the store.
    Attributes:
        name (str): Name of the product.
        price (float): Price of the product.
        stock (int): Quantity available in stock.
    """
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        """Return string representation of the product."""
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"

# ----------------------------- Store Class -----------------------------
class Store:
    """
    Represents the store containing multiple products.
    Attributes:
        products (List[Product]): List of products in the store.
    """
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, name: str, price: float, stock: int):
        """Add a new product to the store."""
        self.products.append(Product(name, price, stock))
        print(f"✅ Product added: {name} - ${price:.2f} (Stock: {stock})")

    def list_products(self):
        """Display all products with their index."""
        if not self.products:
            print("No products available.")
            return
        for idx, product in enumerate(self.products, start=1):
            print(f"[{idx}] {product}")

    def find_product(self, name: str) -> Product | None:
        """Find a product by name. Return Product object or None."""
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

# ----------------------------- CartItem Class -----------------------------
class CartItem:
    """
    Represents a single item in the customer's cart.
    Attributes:
        product (Product): The product object.
        quantity (int): Number of units added to cart.
    """
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

# ----------------------------- Cart Class -----------------------------
class Cart:
    """
    Represents the customer's shopping cart.
    Attributes:
        items (List[CartItem]): List of items in the cart.
    """
    def __init__(self):
        self.items: List[CartItem] = []

    def add_to_cart(self, product: Product, quantity: int):
        """Add a product to the cart with quantity. Updates quantity if already in cart."""
        if quantity > product.stock:
            print(f"❌ Cannot add {quantity} units. Only {product.stock} available in stock.")
            return

        # Check if item already in cart
        for item in self.items:
            if item.product.name.lower() == product.name.lower():
                # Check if combined quantity exceeds stock
                if item.quantity + quantity > product.stock + item.quantity: # Check against original stock
                     print(f"❌ Cannot add {quantity} more. Total request ({item.quantity + quantity}) exceeds stock ({product.stock + item.quantity}).")
                     return
                item.quantity += quantity
                product.stock -= quantity
                print(f"✅ Added {quantity} x {product.name} to cart.")
                return

        # If not in cart, add as new item
        self.items.append(CartItem(product, quantity))
        product.stock -= quantity
        print(f"✅ Added {quantity} x {product.name} to cart.")

    def remove_from_cart(self, product_name: str):
        """Remove a product from the cart and return stock to store."""
        for item in self.items:
            if item.product.name.lower() == product_name.lower():
                item.product.stock += item.quantity
                self.items.remove(item)
                print(f"🗑️ Removed {product_name} from cart.")
                return
        print(f"❌ Product {product_name} not found in cart.")

    def view_cart(self):
        """Display all items in the cart with total price."""
        if not self.items:
            print("🛒 Your cart is empty.")
            return
        print("🛒 Your cart:")
        for item in self.items:
            print(f"- {item.product.name} x{item.quantity} - ${item.product.price * item.quantity:.2f}")
        print(f"💰 Total: ${self.total_price():.2f}")

    def total_price(self):
        """Calculate total price of all items in cart."""
        return sum(item.product.price * item.quantity for item in self.items)