def solution():
    """Alan went to the market and bought 20 eggs at the price of $2 per egg. He bought 6 chickens for the price of $8 per chicken. How much money did Alan spend at the market?"""
    # Define the price of eggs and chickens
    egg_price = 2
    chicken_price = 8

    # Calculate the total cost of the eggs and chickens
    egg_cost = 20 * egg_price
    chicken_cost = 6 * chicken_price

    # Calculate the total amount of money spent
    total_cost = egg_cost + chicken_cost

    # return the result
    result = total_cost
    return result

print(solution())