from data import MENU, resources

print(MENU, resources)

money = 0
machine_in_on = True
enough_money = True
enough_ingredients = True


def calculate_money(drink):
    global money
    quarter = int(input("Insert quarter\n"))
    dimes = int(input("Insert dimes\n"))
    nickel = int(input("Insert nickel\n"))
    pennies = int(input("Insert pennies\n"))
    sum_money_inserted = 0.25 * quarter + 0.1 * dimes + 0.05 * nickel + 0.01 * pennies
    if sum_money_inserted < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif sum_money_inserted == MENU[drink]["cost"]:
        money += MENU[drink]["cost"]
        return True
    elif sum_money_inserted > MENU[drink]["cost"]:
        change = sum_money_inserted - MENU[drink]["cost"]
        print(f"Here is the change {round(change, 2)}")
        money += MENU[drink]["cost"]
    return True


def make_drink(drink):
    if check_ingredients(drink) & calculate_money(drink=drink):
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        if drink != "espresso":
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        print("Enjoy your coffee")
        print_report()


def check_ingredients(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    if drink != "espresso":
        if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
    return True


def print_report():
    print(f"Water: {resources["water"]} ml"
          f"\nMilk: {resources["milk"]} ml\nCoffer: {resources["coffee"]}g \nMoney: ${money}")


while machine_in_on:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "off":
        print("Coffee machine is shutting down, See ya!")
        break
    elif user_input == "report":
        print_report()
    elif user_input == "espresso":
        make_drink(drink="espresso")
    elif user_input == "latte":
        make_drink(drink="latte")
    elif user_input == "cappuccino":
        make_drink(drink="cappuccino")
