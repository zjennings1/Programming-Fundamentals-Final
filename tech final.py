
# Each product
class Item:
    def __init__(self, name, price, quantity):
        self.name = name  # Name of the item
        self.price = price  # Price per unit
        self.quantity = quantity  # Number of units

    def total_cost(self):
        return self.price * self.quantity  # The total cost of the item



# Manage multiple items
class ShoppingCart:
    def __init__(self):
        self.cart = []  # Stores all items in the cart

    def add_item(self):
        # Get items from shopper
        name = input("Enter item name: ")
        price = float(input("Enter item price: $"))
        quantity = int(input("Enter item quantity: "))
        self.cart.append(Item( name, price, quantity))  # Add new Item to the cart
        print(f"Added {name} to the cart.")

    def checkout(self):
        if not self.cart:  # Check if the cart is empty
            print("Your cart is empty.")
        else:
            total = sum(item.total_cost() for item in self.cart)  # Loop through cart to calculate total
            print(f"Total cost: ${total:.2f}. Thank you for shopping!")
            self.cart.clear()  # Clear the cart



# Main program starts here
cart = ShoppingCart()  # Create a ShoppingCart object

while True:  # Continue until the user chooses to exit
    # Display menu options
    print("\n1. Add Item  2. Checkout  3. Exit")
    choice = input("Choose an option: ")  # Get the users choice

    if choice == "1":  # Add  aitem
        cart.add_item()
    elif choice == "2":  # Checkout
        cart.checkout()
        break  # Exit after the checkout
    elif choice == "3":  # Exit
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")  # bad input