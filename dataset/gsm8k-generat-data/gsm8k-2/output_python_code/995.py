def solution():
    """A club opens up and charges $20 to enter. James buys 2 rounds for his 5 friends. He also buys 6 drinks for himself. Drinks cost $6 each. He decides to eat some food so he orders some fried chicken which costs $14. He leaves a 30% tip on everything he orders. How much did he spend for the night?"""
    entrance_fee = 20
    drink_price = 6
    num_rounds = 2
    num_friends = 5
    num_drinks = 6
    food_price = 14

    total_drink_price = drink_price * num_rounds * num_friends + drink_price * num_drinks
    subtotal = entrance_fee + total_drink_price + food_price
    tip = subtotal * 0.3
    total_price = subtotal + tip

    result = total_price
    return result

print(solution())