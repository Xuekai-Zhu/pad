def solution():
    
    total_sets = 2
    knives_per_set = 4
    set_cost = 80
    total_cost = total_sets * set_cost
    total_knives = total_sets * knives_per_set
    cost_per_knife = total_cost / total_knives
    result = cost_per_knife
    return result

print(solution())