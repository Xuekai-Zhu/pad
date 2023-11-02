def solution():
    
    sets_of_steak_knives = 2
    steak_knives_per_set = 4
    total_steak_knives = sets_of_steak_knives * steak_knives_per_set
    total_cost = 80 * sets_of_steak_knives
    cost_per_knife = total_cost / total_steak_knives
    result = cost_per_knife
    return result

print(solution())