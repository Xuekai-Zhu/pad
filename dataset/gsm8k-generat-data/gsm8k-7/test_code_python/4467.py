def solution():
    cost_of_green_lettuce = 8
    cost_of_red_lettuce = 6
    cost_per_pound = 2

    # Calculate the total cost of all lettuce
    total_cost = cost_of_green_lettuce + cost_of_red_lettuce

    # Calculate the total weight of all lettuce
    total_weight = total_cost / cost_per_pound
    result = total_weight
    return result

print(solution())