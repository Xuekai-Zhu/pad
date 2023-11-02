def solution():
    total_sets = 2
    knives_per_set = 4
    total_knives = total_sets * knives_per_set
    cost_per_set = 80.00
    total_cost = cost_per_set * total_sets
    cost_per_knife = total_cost / total_knives
    result = cost_per_knife
    return result

print(solution())