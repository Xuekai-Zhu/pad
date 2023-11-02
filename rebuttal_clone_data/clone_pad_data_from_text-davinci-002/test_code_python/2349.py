def solution():
    cost_of_meal = 6
    cost_of_soda = cost_of_meal / 3
    cost_of_jeremys_order = cost_of_meal + cost_of_soda
    total_cost = cost_of_meal + cost_of_soda + cost_of_jeremys_order
    result = total_cost
    return result

print(solution())