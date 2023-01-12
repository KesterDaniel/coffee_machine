from menu import MENU

init_Stats = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_resource(order):
    """Checks if there is enough ingredients to process the order"""
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        if init_Stats[item] - ingredients[item] < 0:
            return f"Sorry, There is not enough {item}"
        else:
            return "Proceed"


user_input = input("What would you like? (espresso/latte/cappuccino): ")

if user_input == "report":
    for stat in init_Stats:
        print(f"{stat}: {init_Stats[stat]}")
else:
    availability = check_resource(user_input)
    if availability != "Proceed":
        print(availability)
    else:
        print("Please insert coins")
        quarters = float(input("How many quarters: ")) * 0.25
        dimes = float(input("How many dimes: ")) * 0.10
        nickels = float(input("How many nickel: ")) * 0.05
        pennies = float(input("How many pennies: ")) * 0.01
        cost = (quarters + dimes + nickels + pennies)
        total_cost = "{:.2f}".format(cost)
        print(total_cost)



