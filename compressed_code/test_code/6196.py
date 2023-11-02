def solution():
    
    younger_sister_cost = 4 * 15
    total_cost = younger_sister_cost * 2
    older_sister_cost = total_cost / 2
    lego_set_cost = 20
    lego_sets = older_sister_cost / lego_set_cost
    result = lego_sets
    return result

print(solution())