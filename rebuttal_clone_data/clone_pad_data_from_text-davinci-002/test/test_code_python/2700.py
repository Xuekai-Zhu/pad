def solution():
    desired_temperature_drop = 1.8
    cost_per_tree = 6
    temperature_drop_per_tree = 0.1
    trees_needed = desired_temperature_drop / temperature_drop_per_tree
    total_cost = cost_per_tree * trees_needed
    result = total_cost
    
    return result

print(solution())