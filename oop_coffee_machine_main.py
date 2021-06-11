from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_CoffeeMaker = CoffeeMaker()
my_MoneyMachine = MoneyMachine()

coffee_machine_on = True

while coffee_machine_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()
    print(choice)
    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        my_MoneyMachine.report()
        my_CoffeeMaker.report()
    else:
        drink = my_menu.find_drink(choice)
        my_resource_check = my_CoffeeMaker.is_resource_sufficient(drink)
        print(my_resource_check)
        if my_resource_check:
            print(f"A {choice} costs: £{drink.cost}")
            my_make_payment = my_MoneyMachine.make_payment(drink.cost)
            if my_make_payment:
                my_CoffeeMaker.make_coffee(drink)

# Choose Drink
# proceed = False
# while not proceed:
#     drink_selection = input(f"What would you like to drink? {Menu.get_items(my_menu)}: ").lower()
#     print(drink_selection)
#     if drink_selection == "latte":
#         proceed = True
#         latte = my_menu.menu[0]
#         print(proceed)
#     elif drink_selection == "espresso":
#         proceed = True
#         espresso = my_menu.menu[1]
#         print(proceed)
#     elif drink_selection == "cappuccino":
#         proceed = True
#         cappuccino = my_menu.menu[2]
#         print(proceed)
#     else:
#         proceed = False
#         print(proceed)
#
# my_resource_check = CoffeeMaker.is_resource_sufficient(my_CoffeeMaker, drink_selection)

# # Check enough ingredients to make coffee
# latte = my_menu.menu[0]
# espresso = my_menu.menu[1]
# cappuccino = my_menu.menu[2]
# print(latte.name, latte.cost, latte.ingredients)
# my_resource_check = CoffeeMaker.is_resource_sufficient(my_CoffeeMaker, latte)


# Take payment
# my_make_payment = MoneyMachine.make_payment(my_MoneyMachine, drink_selection.cost)

# # check payment
# if my_make_payment and my_resource_check:
#     CoffeeMaker.make_coffee(my_CoffeeMaker, latte)