from models import Store, Cart

# ----------------------------- Manager Menu -----------------------------
def store_manager_menu(store: Store):
    """CLI menu for Store Manager to add products."""
    print("\n--------------------------------")
    print("🔐 Store Manager Login")
    print("--------------------------------")
    username = input("Username: ")
    password = input("Password: ")
    if username != "admin" or password != "1234":
        print("❌ Login failed! Please try again or return to main menu.")
        return

    print("✅ Login successful! Welcome, Manager.\n")
    while True:
        print("--------------------------------")
        print("📦 Add Products")
        print("--------------------------------")
        name = input("Enter product name (or 'done' to finish): ")
        if name.lower() == "done":
            print("Returning to main menu...\n")
            break
        try:
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock quantity: "))
            if price < 0 or stock < 0:
                print("❌ Price and stock must be non-negative.")
                continue
        except ValueError:
            print("❌ Invalid input. Try again.")
            continue
        store.add_product(name, price, stock)

# ----------------------------- Customer Menu -----------------------------
def customer_menu(store: Store):
    """CLI menu for Customer to browse and shop."""
    cart = Cart()
    print("\n--------------------")
    print("🛍️ CUSTOMER PORTAL")
    print("--------------------")
    print("Hello, dear customer!")

    while True:
        print("\nAvailable products:")
        store.list_products()
        print("\nWhat would you like to do?")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Return to main menu")
        choice = input("Enter choice: ")

        if choice == "1":
            pname = input("Enter product name: ")
            product = store.find_product(pname)
            if not product:
                print(f"❌ Product '{pname}' not found.")
                continue
            try:
                qty = int(input("Enter quantity: "))
                if qty <= 0:
                    print("❌ Quantity must be positive.")
                    continue
            except ValueError:
                print("❌ Invalid quantity.")
                continue
            cart.add_to_cart(product, qty)

        elif choice == "2":
            pname = input("Enter product name to remove: ")
            cart.remove_from_cart(pname)

        elif choice == "3":
            cart.view_cart()

        elif choice == "4":
            if not cart.items:
                print("❌ Your cart is empty. Cannot checkout.")
                continue
            print("\n🧾 Final Checkout:")
            cart.view_cart()
            print("🎉 Thank you for shopping with us!")
            cart.items.clear() # Clear cart after checkout
        elif choice == "5":
            # Return items to stock if user exits without checkout
            for item in cart.items:
                 item.product.stock += item.quantity
            print("Returning to main menu (cart cleared and stock restored)...\n")
            break
        else:
            print("❌ Invalid choice. Try again.")

# ----------------------------- Main Function -----------------------------
def main():
    """Main menu loop to select role and exit program."""
    store = Store()
    while True:
        print("=================================")
        print("🛍️ MINI STORE MANAGEMENT SYSTEM")
        print("=================================")
        print("\n👋 Welcome! Please select your role:")
        print("1. Store Manager")
        print("2. Customer")
        print("3. Exit Program")
        choice = input("Enter choice: ")

        if choice == "1":
            store_manager_menu(store)
        elif choice == "2":
            customer_menu(store)
        elif choice == "3":
            print("👋 Goodbye! See you next time.")
            break
        else:
            print("❌ Invalid choice. Try again.\n")