# Project 5 — Mini Shopping Cart
# Author: Getoar Sopa

menu = {
    1: ("Apple",  0.50),
    2: ("Banana", 0.30),
    3: ("Milk",   1.20),
    4: ("Bread",  2.00),
}

cart = {}   # { item_name: quantity }
total = 0.0

# Display menu
print("--- Shop Menu ---")
for key, (name, price) in menu.items():
    print(f"{key}. {name:<7} ${price:.2f}")
print("5. Done")

# Shopping loop
while True:
    choice = int(input("Choose an item (1-5): "))

    if choice == 5:
        break

    if choice not in menu:
        print("Invalid choice. Try again.")
        continue

    item_name, price = menu[choice]

    # Update cart (handle duplicates)
    if item_name in cart:
        cart[item_name] += 1
    else:
        cart[item_name] = 1

    # Update total
    total += price

    print(f"Added {item_name}. Total: ${total:.2f}")

# Receipt
print("\n--- Receipt ---")
for item, qty in cart.items():
    # get price from menu
    for key, (name, price) in menu.items():
        if name == item:
            item_price = price
            break

    print(f"{item:<7} x{qty}   ${item_price * qty:.2f}")

print("---------------------")
print(f"Total: ${total:.2f}")
print("Thank you!")
