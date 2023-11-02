def solution():
    # Calculate the total number of servings Tricia needs for 2 weeks
    servings_per_day = 0.5 * 6  # Tricia drinks half a container a day, which is 3 servings
    total_servings = servings_per_day * 14  # 2 weeks = 14 days
    # Calculate the total cost of the bottles Tricia needs to buy
    cost_per_bottle = 3.00  # The coffee is on sale for $3.00 a bottle
    bottles_needed = total_servings / 6  # 1 container has 6 servings
    total_cost = bottles_needed * cost_per_bottle
    result = total_cost
    return result

print(solution())