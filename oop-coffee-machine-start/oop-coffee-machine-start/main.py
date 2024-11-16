from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()



while is_on:
   options = menu.get_items()
   choice = input(f"what would you like? ({options})")
   if choice == "off":
    is_on= False
   elif choice == "report":
       coffee_maker.report()
       money_machine.report()
   else:
       drink = menu.find_drink(choice)
       is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
       is_payment_successful = money_machine.make_payment(drink.cost)
       if coffee_maker.is_resource_sufficient(drink):
           if is_payment_successful and is_enough_ingredients:
               coffee_maker.make_coffee(drink)



