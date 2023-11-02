def solution():
    """A 750 ml bottle of spirits costs $30.00 and has 16 servings per bottle. Most restaurants will charge $8.00 for one serving. How much money does a restaurant make on a bottle of spirits?"""
    bottle_cost = 30.00
    servings_per_bottle = 16
    serving_price = 8.00
    revenue_per_bottle = servings_per_bottle * serving_price
    profit_per_bottle = revenue_per_bottle - bottle_cost
    result = profit_per_bottle
    return result

print(solution())