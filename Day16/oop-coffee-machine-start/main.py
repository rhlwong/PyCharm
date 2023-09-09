from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myMachine = CoffeeMaker()
myMenu = Menu()
myMenuItem = MenuItem('name', 'water', 'milk', 'coffee', 'cost')
myMoneyMachine = MoneyMachine()

print(myMenu.get_items())
is_on = True

while is_on:
    selection = input(f"Input Your Choice({myMenu.get_items()}):")
    if selection == "off":
        print("GoodBye")
        is_on = False
    elif selection == "report":
        myMachine.report()
        myMoneyMachine.report()
    else:
        print(f"it is your choice {selection}")