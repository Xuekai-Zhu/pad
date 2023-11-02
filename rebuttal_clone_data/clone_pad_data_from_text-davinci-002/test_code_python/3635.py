def solution():
    total_cost = 37
    total_notebooks = 12
    cost_of_red = 3 * 4
    cost_of_green = 2 * 2
    cost_of_blue = total_cost - cost_of_red - cost_of_green
    cost_per_blue = cost_of_blue / (total_notebooks - 5)
    result = cost_per_blue
    return result

print(solution())