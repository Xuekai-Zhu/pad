def solution():
    
    num_trees = 8
    num_fruits_per_tree = 200
    fraction_picked = 2/5
    total_fruits_remaining = num_trees * num_fruits_per_tree * (1 - fraction_picked)
    result = total_fruits_remaining
    return result

print(solution())