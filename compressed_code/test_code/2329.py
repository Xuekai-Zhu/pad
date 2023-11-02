def solution():
    
    initial_trees = 400
    cut_trees = initial_trees * 0.2
    remaining_trees = initial_trees - cut_trees
    planted_trees = cut_trees * 5
    total_trees = remaining_trees + planted_trees
    result = total_trees
    return result

print(solution())