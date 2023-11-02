def solution():
    
    num_trees = 8
    fruits_per_tree = 200
    fraction_picked = 2/5
    fruits_remaining = num_trees * fruits_per_tree * (1 - fraction_picked)
    result = fruits_remaining
    return result

print(solution())