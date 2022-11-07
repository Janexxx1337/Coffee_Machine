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
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']

total = profit

def checkFor(data, flavor, ing, liquid):
    cup = data[flavor][ing][liquid]

    return cup


checkFor(MENU, 'espresso', "ingredients", 'coffee')


def math_operation(liquid1, liquid2, liquid3, flavor):
    liquid1 -= flavor
    liquid2 -= flavor
    liquid3 -= flavor
    bank = 0
    bank += flavor

    return bank


def welcome(data=MENU, liquid_w=water, liquid1_m=milk, liquid2_c=coffee):
    global total, water, coffee, milk

    espresso_price = data['espresso']["cost"]
    latte_price = data['latte']["cost"]
    cappuccino_price = data['cappuccino']["cost"]

    choose_one = input("What would you like? espresso/latte/cappuccino ")
    if choose_one == 'espresso':
        print(f'Espresso price is {espresso_price} $!')

    elif choose_one == 'off':
        return

    elif choose_one == 'latte':
        print(f'Latte price is {latte_price} $!')

    elif choose_one == 'report':
        print(f'Remaining in the bank water:{water}, milk:{milk}, coffee:{coffee}, money: {total}')
        welcome(MENU, water, milk, coffee)



    elif choose_one == 'cappuccino':
        print(f'Cappuccino price is {cappuccino_price} $!')
    print('Insert coins please!')
    quarts = int(input('How many quarts?')) * 0.25
    dimes = int(input('How many dimes?')) * 0.10
    nickles = int(input('How many nickles?')) * 0.5
    pennies = int(input('How many pennies?')) * 0.1

    insert = round(dimes + quarts + nickles + pennies, 1)

    if choose_one == 'latte':
        latte_water = int(checkFor(MENU, 'latte', "ingredients", 'water'))
        latte_coffee = int(checkFor(MENU, 'latte', "ingredients", 'coffee'))
        latte_milk = int(checkFor(MENU, 'latte', "ingredients", 'coffee'))

        if water < latte_water:
            print(f'Not enough water! In machine: {water}ml.You need: {latte_water}ml')

            # print(f'Not enough resources!\n You need {cappuccino_water} ml of water and {cappuccino_coffee}coffee gr, and {cappuccino_milk}milk ml ')
            # print(f'But machine have: {water} ml, {coffee} gr, {milk} ml')

        elif coffee < latte_coffee:
            print(f'Not enough water! In machine: {coffee}ml.You need: {latte_coffee}ml')


        elif milk < latte_milk:
            print(f'Not enough water! In machine: {milk}ml.You need: {latte_milk}ml')




        elif insert < latte_price:
            print('Not enough money!')
            welcome(MENU, water, milk, coffee)


        else:
            res = round(latte_price - insert, 1)
            print('Enjoy your coffee ☕')
            print(f'That is your change {-res} $')
            cap_cost = MENU['latte']['cost']
            total += math_operation(water, milk, coffee, cap_cost)

            water -= latte_water
            coffee -= latte_coffee
            milk -= latte_milk

            print(f'Remaining in the bank water:{water}, milk:{milk}, coffee:{coffee}, money: {total}')
            while True:
                welcome(MENU, water, milk, coffee)
    elif choose_one == 'espresso':

        espresso_water = int(checkFor(MENU, 'espresso', "ingredients", 'water'))

        espresso_coffee = int(checkFor(MENU, 'espresso', "ingredients", 'coffee'))


        if water < espresso_water:

            print(f'Not enough water! In machine: {water}ml.You need: {espresso_water}ml')


        elif coffee < espresso_coffee:

            print(f'Not enough water! In machine: {coffee}ml.You need: {espresso_coffee}ml')



        elif insert < espresso_price:

            print('Not enough money!')

            welcome(MENU, water, milk, coffee)



        else:

            res = round(espresso_price - insert, 1)
            print('Enjoy your coffee ☕')
            print(f'That is your change {-res} $')

            cap_cost = MENU['espresso']['cost']

            total += math_operation(water, milk, coffee, cap_cost)

            water -= espresso_water

            coffee -= espresso_coffee

            print(f'Remaining in the bank water:{water}, milk:{milk}, coffee:{coffee}, money: {total}')

            while True:
                welcome(MENU, water, milk, coffee)

    elif choose_one == 'cappuccino':
        cappuccino_water = int(checkFor(MENU, 'cappuccino', "ingredients", 'water'))
        cappuccino_coffee = int(checkFor(MENU, 'cappuccino', "ingredients", 'coffee'))
        cappuccino_milk = int(checkFor(MENU, 'cappuccino', "ingredients", 'coffee'))

        if water < cappuccino_water:
            print(f'Not enough water! In machine: {water}ml.You need: {cappuccino_water}ml')

            # print(f'Not enough resources!\n You need {cappuccino_water} ml of water and {cappuccino_coffee}coffee gr, and {cappuccino_milk}milk ml ')
            # print(f'But machine have: {water} ml, {coffee} gr, {milk} ml')

        elif coffee < cappuccino_coffee:
            print(f'Not enough water! In machine: {coffee}ml.You need: {cappuccino_coffee}ml')


        elif milk < cappuccino_milk:
            print(f'Not enough water! In machine: {milk}ml.You need: {cappuccino_milk}ml')




        elif insert < cappuccino_price:
            print('Not enough money!')
            welcome(MENU, water, milk, coffee)


        else:
            res = round(cappuccino_price - insert, 1)
            print('Enjoy your coffee ☕')
            print(f'That is your change {-res} $')
            cap_cost = MENU['cappuccino']['cost']
            total += math_operation(water, milk, coffee, cap_cost)

            water -= cappuccino_water
            coffee -= cappuccino_coffee
            milk -= cappuccino_milk

            print(f'Remaining in the bank water:{water}, milk:{milk}, coffee:{coffee}, money: {total}')
            while True:
                welcome(MENU, water, milk, coffee)


welcome(MENU, water, milk, coffee)
print('Goodbye!')
