# # ask for type of drink
# # if latte, expresso and capuccino -> check resources and if there are enough, make drink
# # if report - print resources left

# # check resources sufficient
# # when user chooses a drink check if resources are sufficient
# # if type of drink == latte
# # if ok -> run
# # if not -> print ("Sorry not suffiecient etc..")

# # ask for coins

# # process coins
# # check that the user has inserted enough coins to purchase the drink
# # transform it into dollar amount
# # continue with transaction
# # add cost to resources

# # transaction successful
# # if not enough money - print("sorry not enough")
# # if enough - deduct the resources used from main resource
# # if too much money inserted, offer change


# from tabnanny import check
# from data import resources, MENU

# # print(resources["water"])


# def print_report():
#     print(f"Water: {resources['water']}ml")
#     print(f"Milk: {resources['milk']}ml")
#     print(f"Coffee: {resources['coffee']}g")

#     # print(resources["money"])
# # print_report()


# def process_coins():

#     quarters = int(input("How many quarters? "))
#     dimes = int(input("How many dimes? "))
#     nickels = int(input("How many nickels? "))
#     pennies = int(input("How many pennies? "))

#     quarters_amount = quarters * 0.25
#     dimes_amount = dimes * 0.1
#     nickels_amount = nickels * 0.05
#     pennies_amount = pennies * 0.01

#     # print(quarters_amount + dimes_amount + nickels_amount + pennies_amount)
#     return quarters_amount + dimes_amount + nickels_amount + pennies_amount


# # process_coins()

# def check_resources():
#     # print("resources")
#     for drink in MENU:

#         # water = MENU[drink][ingredient]
#         # coffee = MENU[drink][ingredient]
#         # milk = MENU[drink][ingredient]
#         print(drink, ingredient)


# def pick_drink():
#     drink_choice = input("What would you like? (espresso/latte/capuccino): ")

#     if drink_choice == "report":
#         print_report()

#     for drink in MENU:
#         if drink_choice == drink:
#             # print(drink_choice)
#             check_resources()
#         else:
#             return


# pick_drink()


# check_resources()
