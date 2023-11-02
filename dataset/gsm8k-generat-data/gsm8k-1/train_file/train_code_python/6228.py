def solution():
    """It’s Meghan’s turn to pick up her team's coffee order. She needs 2 drip coffees that are $2.25 each and one double shot espresso that’s $3.50. She needs 2 lattes that are $4.00 and needs to add vanilla syrup to one of those for an additional $0.50. She also needs 2 cold brew coffees that are $2.50 each and 1 cappuccino for $3.50. How much is the coffee order?"""
    drip_coffee_cost = 2.25
    double_shot_cost = 3.50
    latte_cost = 4.00
    vanilla_syrup_cost = 0.50
    cold_brew_cost = 2.50
    cappuccino_cost = 3.50

    total_cost = (2 * drip_coffee_cost) + double_shot_cost + \
        (2 * latte_cost) + vanilla_syrup_cost + \
        (2 * cold_brew_cost) + cappuccino_cost

    result = total_cost
    return result

print(solution())