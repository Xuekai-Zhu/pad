def solution():
    total_trees = 400
    cut_trees = 0.2 * total_trees
    new_trees = 5 * cut_trees
    total_trees = total_trees - cut_trees + new_trees
    result = total_trees
    return result

print(solution())