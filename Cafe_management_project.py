import random

# Define the menu of restaurant
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80
}

# Greeting
print("Welcome to Python Restaurant\n")

# Restaurant Menu
print("Menu:")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

order_total = 0

item_1 = input("\nEnter the name of item you want to order: ").strip().capitalize()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added successfully.")
else:
    print(f"Ordered item '{item_1}' is not available yet!")

another_item = input("Do you want to add another item? (Yes/No): ").strip().lower()
if another_item == 'yes':
    item_2 = input("Enter the name of 2nd Item: ").strip().capitalize()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added successfully.")
    else:
        print(f"Ordered item '{item_2}' is not available yet!")

print(f"\nThe total amount to pay is ₹{order_total}")

# Random farewell message
wishes = [
    "Thank you for visiting! We hope you enjoyed your time. Have a great day ahead! ☕😊",
    "Your presence made our café brighter! Hope to see you again soon. Stay happy, stay caffeinated! ☕✨",
    "Great choice! We loved serving you today. Come back soon for more delicious treats! 🍝☕",
    "Thank you for choosing us! We value your time and taste. Looking forward to your next visit! 😊"
]

print("\n" + random.choice(wishes))  # Selecting a random farewell message
