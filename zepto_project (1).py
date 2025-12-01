#!/usr/bin/env python
# coding: utf-8

# In[1]:


cart = {}

def display_products():
    """Return and display the list of available products."""
    products = {
        "apple": 120,
        "bananas": 60,
        "milk": 50,
        "oil": 150,
    }
    print("\nAvailable Products:")
    for product, price in products.items():
        print(f"{product.capitalize()} - {price}")
    return products

def add_to_cart(product_name, quantity=1):
    """Add a product with given quantity to the cart."""
    products = display_products()

    product_name = product_name.lower()

    if product_name not in products:
        print(" Product not found!\n")
        return

    if product_name in cart:
        cart[product_name]["quantity"] += quantity
    else:
        cart[product_name] = {"price": products[product_name], "quantity": quantity}

    print(f" Added {quantity} {product_name} to cart.\n")

def remove_from_cart(product_name):
    """Remove a product completely from the cart."""
    product_name = product_name.lower()

    if product_name in cart:
        del cart[product_name]
        print(f"Removed {product_name} from cart.\n")
    else:
        print(" Product not in cart.\n")

def view_cart():
    """Display cart items and return total price."""
    if not cart:
        print("Your cart is empty\n")
        return 0

    print("\nYour Cart:")
    total = 0
    for product, item in cart.items():
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{product.capitalize()} x{item['quantity']} = {subtotal}")

    print(f"Total: ₹{total}\n")
    return total

def payment_options(total):
    """Show payment method options and process choice."""
    print("\nChoose Payment Method:")
    print("1. Cash on Delivery (COD)")
    print("2. Online Payment")

    choice = input("Enter option: ").strip()

    if choice == "1":
        cod_payment()
    elif choice == "2":
        online_payment(total)
    else:
        print("Invalid option!\n")

def cod_payment():
    """Complete order using Cash on Delivery."""
    print("Order placed successfully, Pay cash on delivery.\n")
    cart.clear()

def online_payment(total):
    """Process on online payment for the given total."""
    print(f"Processing online payment of {total}...")
    input("Enter card details (card number): ")
    print(" Payment successful, Order placed.\n")
    cart.clear()

customer_info = {}

def checkout():
    """Handle full checkout process including payment and customer details."""
    if not cart:
        print("Nothing to checkout! Add items first.\n")
        return

    print("Please provide your details for delivery:")
    customer_info["name"] = input("Name: ").strip()
    customer_info["location"] = input("Location/Address: ").strip()
    customer_info["phone"] = input("Phone number: ").strip()

    
    print("\nDelivery Details:")
    print(f"Name: {customer_info['name']}")
    print(f"Location: {customer_info['location']}")
    print(f"Phone: {customer_info['phone']}")


    total = view_cart()
    payment_options(total)


def main():
    while True:
        print("\n--- Welcome to Mini Cart ---")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_products()
        elif choice == "2":
            display_products()  
            product = input("Enter product name to add: ")
            qty = int(input("Enter quantity: "))
            add_to_cart(product, qty)
        elif choice == "3":
            product = input("Enter product name to remove: ")
            remove_from_cart(product)
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice! Try again.\n")
main()


# In[ ]:




