def solution():
    # Calculate the cost of the apples
    cost_apples = 5 * 2  # 5 kilograms of apples at $2 per kilogram
    # Calculate the cost of the sugar
    cost_sugar = 3 * (cost_apples - 1)  # 3 packs of sugar at $1 cheaper per pack than the cost of 1 kilogram of apples
    # Calculate the cost of the walnuts
    cost_walnuts = 0.5 * 6  # 500 grams of walnuts at $6 per kilogram
    # Calculate the total cost
    total_cost = cost_apples + cost_sugar + cost_walnuts
    result = total_cost
    return result

print(solution())