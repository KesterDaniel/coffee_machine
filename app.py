from menu import MENU

init_Stats = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
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
    print(check_resource(user_input))


