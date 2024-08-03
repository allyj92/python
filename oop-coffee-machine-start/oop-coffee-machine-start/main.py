from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
coffeMaker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_on:
    choice = input("What would you like? (espresso/latte/capuccino)").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeMaker.report()
    else:
        drink = menu[choice]
        if coffeMaker.is_resource_sufficient(drink):
            payment = money_machine.process_coins()
            if money_machine.make_payment(payment):
                coffeMaker.make_coffee(drink)







