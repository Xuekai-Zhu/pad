def solution():
    
    temp_drop = 1.8
    temp_drop_per_tree = 0.1
    trees_needed = temp_drop / temp_drop_per_tree
    cost_per_tree = 6
    total_cost = trees_needed * cost_per_tree
    result = total_cost
    return result

print(solution())