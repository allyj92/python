MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}






# TODO: 5. 음료를 만드는 재료는 다음에서 공제 :
def resource_update():
    global profit
    if(resources["milk"]  not in resources):
        resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
        profit +=  MENU[coffee_choice]["cost"]
    else:
        resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
        profit += MENU[coffee_choice]["cost"]

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"{item}이 부족해서 죄송합니다.")
            return False
    return True


def proccess_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost) :
    global profit
    """Return True when the payment is accepted, or False of money is insufficient."""
    if money_recieved >=drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit +=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")



is_on = True
while is_on:


    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):

    coffee_choice = input("What would you like? (espresso/latte/cappucino):")
    if coffee_choice == "off":
        is_on = False
        break
    elif coffee_choice == "report":
        print(f"Water : {resources['water']}ml \n "
              f"Milk : {resources['milk']}ml \n"
              f"Coffee : {resources['coffee']}g \n"
              f"Money : ${profit}")
    else:

        # TODO: 2. 사용자가 음료를 선택할 때 프로그램은 충분한 양이 있는지 확인:
        drink = MENU[coffee_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = proccess_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(coffee_choice,drink["ingredients"])







