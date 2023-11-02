def solution():
    sets_of_drill_bits = 5
    cost_per_set = 6
    tax_rate = 0.1
    total_cost = sets_of_drill_bits * cost_per_set * (1 + tax_rate)
    result = total_cost
    return result

print(solution())