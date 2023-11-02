def solution():
    jello_ratio = 1.5 / 16
    water_amount = 6 * 7.5
    jello_amount = water_amount * jello_ratio
    cost_per_tablespoon = 0.50
    total_cost = cost_per_tablespoon * jello_amount
    result = total_cost
    return result

print(solution())