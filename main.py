# coffee making machine


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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#
# def is_resources_sufficient(order_ingredients):
#     for item in order_ingredients:
#      if order_ingredients[item]>=resources[item]:
#          print(f"we do not have enough {item} resources to make coffe")
#          return False
#      return True
# def transaction_succesful(money_recieved,drink_coats):
#     if money_recieved>=drink_coats:
#         global profit
#         change = money_recieved-drink_coats
#         print(f"the money {change} change")
#         profit+=drink_coats
#         return True
#     else:
#         print("u do not have enough money ")
#         return False
#
# def make_coffee(drink_name, order_ingredients):
#     for item in order_ingredients:
#         resources[item]-=order_ingredients[item]
#     print(f"here your drink name {drink_name}")
#
#
#
#
# def process_coins():
#     total=0
#     print("please insert coins : ")
#     total+=int(input("how many quaters :")) * 0.25
#     total+=int(input("how many dimmes "))*0.10
#     total += int(input("how many nickes:"))*0.05
#     total += int(input("how many pennies :"))*0.01
#     return total
#
# is_on=True
# while is_on:
#     choice=input("what would u like ? (espresso/latte/cappuccino : ")
#     if choice=="off":
#         is_on=False
#     elif choice=="report":
#        print(f"water : {resources['water']} ml")
#        print(f"milk : {resources['milk']}ml")
#        print(f"coffe : {resources['coffee']} g")
#        print(f"money : $ {profit}")
#     else:
#         drink=MENU[choice]
#         print(drink)
#         if is_resources_sufficient(drink["ingredients"]):
#          payment=process_coins()
#          if transaction_succesful(payment, drink["cost"]):
#            make_coffee(choice, drink["ingredients"])

def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item]>order_ingredients[item]:
            return True
        return False

def process_coins():
    total=0
    total+=int(input("enter the number of quaters : "))*0.25
    total+=int(input("enter the number of dimmes : "))*0.10
    total+=int(input("enter the number of nickle : "))*0.05
    total+=int(input("enter the number of pennies:  "))*0.01
    return total

def payment_successful(payment,cost):
    if payment>cost:
        change=payment-cost

is_on=True
while is_on:
    choice=input("what would u like to drink (espresso/latte/capuccino): ")
    if choice=="report":
        print(f"water : {resources['water']}")
        print(f"water : {resources['milk']}")
        print(f"water : {resources['coffee']}")
    elif choice =="off":
        is_on=False
    else:
        drink=MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            payment =process_coins()
            if payment_successful(payment , drink['cost']):



