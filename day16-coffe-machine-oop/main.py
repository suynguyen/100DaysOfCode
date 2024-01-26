from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if user_choice == "off":
        break
    elif user_choice == "report":
        coffe_maker.report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if coffe_maker.is_resource_sufficient(menu.find_drink(user_choice)):
            if money_machine.make_payment(menu.find_drink(user_choice).cost):
                coffe_maker.make_coffee(menu.find_drink(user_choice))


