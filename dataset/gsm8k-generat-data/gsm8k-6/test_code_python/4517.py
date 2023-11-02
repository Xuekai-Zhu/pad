def solution():
    # Calculate the cost of each type of fruit
    cost_bananas = 1 * 4
    cost_apples = 2 * 3
    cost_strawberries = (4/12) * 24
    cost_avocados = 3 * 2
    cost_grapes = 2 * 1

    # Calculate the total cost of the fruit basket
    total_cost = cost_bananas + cost_apples + cost_strawberries + cost_avocados + cost_grapes
    result = total_cost
    return result

print(solution())