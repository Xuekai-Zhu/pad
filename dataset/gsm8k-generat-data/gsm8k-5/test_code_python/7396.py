def solution():
    bottle_size_ml = 750  # A bottle of spirits is 750 ml
    cost_per_bottle = 30.00  # The cost of a bottle of spirits is $30
    servings_per_bottle = 16  # There are 16 servings in a bottle
    price_per_serving = 8.00  # The price for one serving is $8

    # Calculate the revenue generated from one bottle of spirits
    revenue_per_bottle = servings_per_bottle * price_per_serving

    # Calculate the profit made from one bottle of spirits
    profit_per_bottle = revenue_per_bottle - cost_per_bottle

    result = profit_per_bottle
    return result

print(solution())