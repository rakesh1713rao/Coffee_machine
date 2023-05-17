menu = {"expresso": {"ingredients" :{"water":50,"coffee":18},"cost":1.5 },
        "latte" : {"ingredients":{"water":200, "milk": 150,"coffee":24}, "cost":2.5},
        "cappuccino" : {"ingredients": {"water":250, "milk": 100, "coffee":24 }, "cost":3.0}
        }

resources = { 
              "water":300,
              "milk":200,
              "coffee":100
             }

profit = 0

def resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry Insufficient resources for {item}")
            return False
    return True

def process_coins():
    """ Returns the total calculated from coins inserted. """
    print("Please Insert coins")
    total_amt = int(input("How Many quaters?"))*0.25
    total_amt += int(input("How many dimes?"))*0.10
    total_amt += int(input("How many nickles?"))*0.25
    total_amt += int(input("How many penny?"))*0.01
    return total_amt


def is_transaction_successful(drink_cost, paid_amt):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if paid_amt >= drink_cost:
        change = round(paid_amt - drink_cost,2)
        print(f"Here is your change: ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(ordered_drink, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        if order_ingredients[item] < resources[item]:
            resources[item] -= order_ingredients[item]
            print(f"Here is your {ordered_drink} ☕ , Enjoy!")
            return
        else:
            print("Sorry Insufficient resource")
            return False
    return True
    
    
is_machine_on = True

while is_machine_on:
    customer_order = input("what would you like order? (Expresso/Latte/Cappuccino)").lower()
    if customer_order == "off":
        is_machine = False
    elif customer_order == "report":
       print(f"Water:{resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")
    else:
        drink = menu[customer_order]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(paid_amt=payment, drink_cost=drink["cost"]):
                make_coffee(ordered_drink=customer_order, order_ingredients= drink["ingredients"])


print(resources)

