def solution():
    # Calculate the total cost of the ingredients
    cost_eggplants = 5 * 2  # 5 pounds of eggplants at $2.00 a pound
    cost_zucchini = 4 * 2  # 4 pounds of zucchini at $2.00 a pound
    cost_tomatoes = 4 * 3.5  # 4 pounds of tomatoes at $3.50 a pound
    cost_onions = 3 * 1  # 3 pounds of onions at $1.00 a pound
    cost_basil = 2.5  # 1 pound of basil at $2.50 per half pound
    total_cost = cost_eggplants + cost_zucchini + cost_tomatoes + cost_onions + cost_basil

    # Calculate the cost per quart
    quarts = 4  # Yield is 4 quarts
    cost_per_quart = total_cost / quarts
    result = cost_per_quart
    return result

print(solution())