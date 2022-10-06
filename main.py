from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_true = True
menus = Menu()
money = MoneyMachine()
coffee_maker = CoffeeMaker()


while is_true:
    options = menus.get_items()
    choice = input(f"what would you like?  ({options}): ")
    if choice == "off":
        is_true = False
    elif choice == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = menus.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
