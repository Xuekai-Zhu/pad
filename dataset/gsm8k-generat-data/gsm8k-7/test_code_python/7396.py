def solution():
    bottle_size_ml = 750
    bottle_cost = 30.0
    servings_per_bottle = 16
    serving_price = 8.0

    # Calculate the total revenue from selling all 16 servings
    total_revenue = servings_per_bottle * serving_price

    # Calculate the profit from selling one bottle of spirits
    profit_per_bottle = total_revenue - bottle_cost

    result = profit_per_bottle
    return result

print(solution())