
menu = {"pizza": 6.00,
        "nachos": 2.50,
        "popcorn": 4.50,
        "soda": 3.50,
        "fries": 2.50,
        "lemonade": 2.50}

cart = []
total = 0

print("\n-----MENU-----")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------")

while True:
    food = input("Choose an item from the menu (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------YOUR ORDER-----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total: ${total:.2f}")