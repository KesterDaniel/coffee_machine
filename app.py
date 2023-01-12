from menu import MENU

init_Stats = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

user_input = input("What would you like? (espresso/latte/cappuccino): ")

if user_input == "report":
    for stat in init_Stats:
        print(f"{stat}: {init_Stats[stat]}")
else:
    pass

