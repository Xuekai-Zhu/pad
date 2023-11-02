def solution():
    """Alan went to the market and bought 20 eggs at the price of $2 per egg. He bought 6 chickens for the price of $8 per chicken. How much money did Alan spend at the market?"""
    egg_price = 2
    chicken_price = 8
    egg_count = 20
    chicken_count = 6
    egg_cost = egg_price * egg_count
    chicken_cost = chicken_price * chicken_count
    total_cost = egg_cost + chicken_cost
    result = total_cost
    return result

print(solution())