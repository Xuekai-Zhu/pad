def solution():
    # Calculate the cost of the kitchen module
    cost_kitchen = 20000

    # Calculate the cost of the bathroom modules
    cost_bathroom = 2 * 12000  # Denny plans to build two 150 square foot bathrooms

    # Calculate the cost of the remaining modules
    area_remaining = 2000 - 400 - (2 * 150)  # Calculate the remaining square footage
    cost_remaining = area_remaining * 100  # Calculate the cost of the remaining modules

    # Calculate the total cost
    total_cost = cost_kitchen + cost_bathroom + cost_remaining
    result = total_cost
    return result

print(solution())