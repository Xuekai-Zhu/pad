def solution():
    cost_oranges = 12
    kg_oranges = 1
    kg_apples = 3
    cost_apples = cost_oranges / 2

    # Calculate the total cost of all apples
    total_apple_cost = kg_apples * cost_apples

    # Calculate the cost per kg of apples
    cost_per_kg_apples = total_apple_cost / kg_apples
    result = cost_per_kg_apples
    return result

print(solution())