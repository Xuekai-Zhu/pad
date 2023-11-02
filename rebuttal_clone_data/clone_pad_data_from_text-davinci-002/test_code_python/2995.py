def solution():
    initial_trees = 400
    percentage_cut = 20
    trees_cut = initial_trees * (percentage_cut / 100)
    trees_planted = trees_cut * 5
    total_trees = initial_trees + trees_planted
    result = total_trees
    
    return result

print(solution())