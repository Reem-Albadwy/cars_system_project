import re
from datetime import datetime

pre_loggedin_users = {
    "reem": "123",
    "aya": "333#",
    "ali": "723$"
}

available_cars = {
    "budget": [
        {"brand": "Toyota", "model": "Corolla", "price": 20000},
        {"brand": "Honda", "model": "Civic", "price": 22000},
        {"brand": "Nissan", "model": "Sentra", "price": 19000}
    ],
    "midrange": [
        {"brand": "BMW", "model": "3 Series", "price": 41000},
        {"brand": "Audi", "model": "A4", "price": 39000},
        {"brand": "Mercedes-Benz", "model": "C-Class", "price": 42000}
    ],
    "luxury": [
        {"brand": "Tesla", "model": "Model S", "price": 79990},
        {"brand": "Porsche", "model": "911", "price": 99990},
        {"brand": "Jaguar", "model": "F-Type", "price": 73000}
    ],
    "suv": [
        {"brand": "Ford", "model": "Escape", "price": 26000},
        {"brand": "Chevrolet", "model": "Tahoe", "price": 49000},
        {"brand": "Jeep", "model": "Grand Cherokee", "price": 34000}
    ],
    "electric": [
        {"brand": "Tesla", "model": "Model 3", "price": 39990},
        {"brand": "Nissan", "model": "Leaf", "price": 31200},
        {"brand": "Chevrolet", "model": "Bolt EV", "price": 37495}
    ]
}
cart = []

def display_categories():
    print("Available Car Categories:")
    for category in available_cars:
        print(f"- {category.capitalize()}")

def display_models(category):
    if category in available_cars:
        print(f"\nModels available in {category.capitalize()}:")
        for i, car in enumerate(available_cars[category]):
            print(f"{i + 1}. {car['brand']} - {car['model']} - ${car['price']}")
    else:
        print("Invalid category selected.")

def add_to_cart(category, model_index):
    if category in available_cars and 0 <= model_index < len(available_cars[category]):
        selected_model = available_cars[category][model_index]
        cart.append(selected_model)
        print(f"{selected_model['brand']} {selected_model['model']} added to cart.")
    else:
        print("Invalid selection.")

def display_cart():
    global cart  # Ensure we're modifying the global cart
    if cart:
        while True:
            print("\nShopping Cart:")
            total_price = 0
            for idx, item in enumerate(cart):
                print(f"{idx + 1}. {item['brand']} - {item['model']} - ${item['price']}")
                total_price += item['price']
            print(f"Total Price: ${total_price}")

            choice = input("Enter the number of the car to remove from cart (or 'back' to return): ")
            if choice.lower() == "back":
                break
            else:
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(cart):
                        removed_item = cart.pop(idx)
                        print(f"{removed_item['brand']} {removed_item['model']} removed from cart!")
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid input!")
    else:
        print("\nYour shopping cart is empty.")

def calculate_total_cart_price():
    total_price = sum(item['price'] for item in cart)
    return total_price

def logout():
    print("Logged out successfully. Thank you for shopping with us!")

def confirm_func():
    google_account = input("Enter your Google account for confirmation: ")
    is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com)", google_account)
    if is_email:
        print("Thank you for providing your email address. We will send a confirmation of your order to this email very soon.")
    else:
        print("Sorry, invalid format for your email.")
        return confirm_func()

def credit_card_payment():
    print("Only credit card payments are allowed.")
    print("Please enter your shipping information")
    
    cardholder_name = input("Enter your name as it appears on the card: ")
    card_number = input("Enter your credit card number: ")
    cvv = input("Enter your card CVV: ")
    city = input("Enter your city: ")
    country = input("Enter your country: ")
    expiry_date = input("Enter expiry date of the card (YYYY-MM-DD): ")

    try:
        expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")
    except ValueError:
        print("Incorrect date format. Please use YYYY-MM-DD.")
        return credit_card_payment()

    if expiry_date < datetime.now():
        print("Card is expired.")
        return credit_card_payment()

    if not card_number.isdigit() or not cvv.isdigit():
        print("Only integers are allowed for card number and CVV.")
        return credit_card_payment()

    if not cardholder_name.strip() or not country.strip() or not city.strip() or not card_number.strip() or not cvv.strip():
        print("Error: Please fill in all fields.")
        return credit_card_payment()

    # Check if the credit card has enough budget for the cart total
    total_price = calculate_total_cart_price()
    while total_price > 0 and total_price > 70000:  #assuming that user budget is 70000$
        print(f"The total price  ${total_price} exceeds your budget of $70000.")
        print("Please remove items from your cart to reduce the total price.")
        display_cart()
        try:
            item_num = int(input("Enter the number of the item to remove (or 0 to proceed with the current total): "))
            if 0 < item_num <= len(cart):
                removed_item = cart.pop(item_num - 1)
                print(f"{removed_item['brand']} {removed_item['model']} removed from cart.")
                total_price = calculate_total_cart_price()
            elif item_num == 0:
                break
            else:
                print("Invalid item number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if total_price <= 70000:  
        print(f"The total price of ${total_price} is within your budget. Payment successful!")
        confirm_func()
    else:
        print("Your shopping cart is empty or insufficient budget. Payment cannot be processed.")

while True:
    print("Welcome to the Login System!")
    username = input("Enter your username: ")
    if username in pre_loggedin_users:
        password = input("Enter your password: ")
        if password == pre_loggedin_users[username]:
            print(f"Welcome, {username}, to Our Online Car Store! You have successfully logged in.")
            while True:
                print("\nMenu:")
                print("1. View Car Categories")
                print("2. View Models in the Category")
                print("3. Add Model to Cart")
                print("4. View Cart")
                print("5. Shipping Info")
                print("6. Logout")
                choice = input("Enter your choice (1-6): ")
                if choice == "1":
                    display_categories()
                elif choice == "2":
                    category = input("Enter category name (budget, midrange, luxury, suv, electric): ").lower()
                    display_models(category)
                elif choice == "3":
                    category = input("Enter category name: ").lower()
                    model_index = int(input("Enter model index: ")) 
                    add_to_cart(category, model_index)
                elif choice == "4":
                    display_cart()
                elif choice == "5":
                    credit_card_payment()
                elif choice == "6":
                    logout()
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 6.")
            break
        else:
            print("Invalid password. Please try again.")
    else:
        print("Username not found. Please check your username or register if you are a new user.")
        user_name = input("Enter the username to register: ")
        user_pass = input("Enter the password to register: ")
        pre_loggedin_users.update({user_name: user_pass})
        print("You are added to the system.")

