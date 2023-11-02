def solution():
    """Albert wants a paintbrush that costs $1.50, a set of paints that costs $4.35, and a wooden easel that costs $12.65. Albert already has $6.50. How much more money does Albert need?"""
    # Define the prices of the paintbrush, set of paints, and wooden easel
    paintbrush_price = 1.5
    paints_price = 4.35
    easel_price = 12.65

    # Define the amount of money Albert already has
    albert_money = 6.5

    # Calculate the total cost of the items Albert wants to buy
    total_cost = paintbrush_price + paints_price + easel_price

    # Calculate how much more money Albert needs
    more_money_needed = total_cost - albert_money

    # return the result
    result = more_money_needed
    return result

print(solution())