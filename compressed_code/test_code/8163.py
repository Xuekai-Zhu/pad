def solution():
    
    total_trees = 400
    cut_percentage = 0.2
    cut_trees = total_trees * cut_percentage
    trees_planted = cut_trees * 5
    remaining_trees = total_trees - cut_trees + trees_planted
    result = remaining_trees
    return result

print(solution())