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

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
     if order_ingredients[item]>=resources[item]:
         print(f"we do not have enough {item} resources to make coffee")
         return False
     return True
def transaction_succesful(money_recieved,drink_coats):
    if money_recieved>=drink_coats:
        global profit
        change = money_recieved-drink_coats
        print(f"the money {change} change")
        profit+=drink_coats
        return True
    else:
        print("u do not have enough money ")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here your drink name {drink_name}")




def process_coins():
    total=0
    print("please insert coins : ")
    total+=int(input("how many quarters :")) * 0.25
    total+=int(input("how many dimmes "))*0.10
    total += int(input("how many nickels:"))*0.05
    total += int(input("how many pennies :"))*0.01
    return total

is_on=True
while is_on:
    choice=input("what would u like ? (espresso/latte/cappuccino : ")
    if choice=="off":
        is_on=False
    elif choice=="report":
       print(f"water : {resources['water']} ml")
       print(f"milk : {resources['milk']}ml")
       print(f"coffe : {resources['coffee']} g")
       print(f"money : $ {profit}")
    else:
        drink=MENU[choice]
        print(drink)
        if is_resources_sufficient(drink["ingredients"]):
         payment=process_coins()
         if transaction_succesful(payment, drink["cost"]):
           make_coffee(choice, drink["ingredients"])




