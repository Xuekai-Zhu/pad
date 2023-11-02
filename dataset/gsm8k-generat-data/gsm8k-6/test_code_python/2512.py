def solution():
    # Calculate the cost of each ingredient
    eggplants_cost = 5 * 2  # 5 pounds of eggplants at $2.00 per pound
    zucchini_cost = 4 * 2  # 4 pounds of zucchini at $2.00 per pound
    tomatoes_cost = 4 * 3.5  # 4 pounds of tomatoes at $3.50 per pound
    onions_cost = 3 * 1  # 3 pounds of onions at $1.00 per pound
    basil_cost = 2.5  # 1 pound of basil is sold for $2.50 per half pound

    # Calculate the total cost of all the ingredients
    total_cost = eggplants_cost + zucchini_cost + tomatoes_cost + onions_cost + basil_cost

    # Calculate the cost of each quart of ratatouille
    cost_per_quart = total_cost / 4

    result = cost_per_quart
    return result

print(solution())