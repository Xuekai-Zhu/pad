def solution():
    """It’s Meghan’s turn to pick up her team's coffee order. She needs 2 drip coffees that are $2.25 each and one double shot espresso that’s $3.50. She needs 2 lattes that are $4.00 and needs to add vanilla syrup to one of those for an additional $0.50. She also needs 2 cold brew coffees that are $2.50 each and 1 cappuccino for $3.50. How much is the coffee order?"""
    # Define the prices of each item
    drip_coffee_price = 2.25
    double_shot_espresso_price = 3.5
    latte_price = 4.0
    vanilla_syrup_price = 0.5
    cold_brew_coffee_price = 2.5
    cappuccino_price = 3.5

    # Calculate the total cost of the order
    total_cost = (2 * drip_coffee_price) + double_shot_espresso_price + (2 * latte_price) + vanilla_syrup_price + (2 * cold_brew_coffee_price) + cappuccino_price

    # return the result
    result = total_cost
    return result

print(solution())