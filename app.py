from menu import MENU, init_Stats


def report():
    print(f"water: {init_Stats['water']}ml")
    print(f"milk: {init_Stats['milk']}ml")
    print(f"water: {init_Stats['coffee']}g")
    print(f"water: ${init_Stats['money']}")


def check_resource(order):
    """Checks if there is enough ingredients to process the order"""
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        if ingredients[item] > init_Stats[item]:
            return f"Sorry, There is not enough {item}"
        else:
            return "Proceed"


def serve_order(order, pay):
    """deducts quantity of used ingredients from initial stock"""
    # global init_Stats
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        init_Stats[item] -= ingredients[item]
    init_Stats["money"] += pay


def calculate_payment():
    """ calculate the amount of money the user payed and returns the total"""
    quarters = float(input("How many quarters: ")) * 0.25
    dimes = float(input("How many dimes: ")) * 0.10
    nickels = float(input("How many nickel: ")) * 0.05
    pennies = float(input("How many pennies: ")) * 0.01
    pay = (quarters + dimes + nickels + pennies)
    total_pay = float("{:.2f}".format(pay))
    return total_pay


machine_on = True

while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "report":
        report()
    elif user_input == "off":
        machine_on = False
    else:
        availability = check_resource(user_input)
        if availability != "Proceed":
            print(availability)
        else:
            print("Please insert coins")
            payment = calculate_payment()

            order_price = MENU[user_input]["cost"]
            if payment > order_price:
                change = payment - order_price
                serve_order(user_input, order_price)
                print(f"Here is ${change} in change.")
                print(f"Enjoy your {user_input}")
            elif payment == order_price:
                serve_order(user_input, order_price)
                print(f"Enjoy your {user_input}")
            else:
                print("Sorry, that's not enough money. Money refunded.")
