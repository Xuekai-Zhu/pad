def solution():
    cost_of_sofa = 1250
    cost_of_armchairs = 425 * 2
    total_cost = 2430
    cost_of_coffee_table = total_cost - cost_of_sofa - cost_of_armchairs
    result = cost_of_coffee_table
    return result

print(solution())