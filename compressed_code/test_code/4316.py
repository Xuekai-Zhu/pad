def solution():
    
    forest_trees = 5000
    desert_trees = forest_trees - (3/5 * forest_trees)
    total_trees = forest_trees + desert_trees
    result = total_trees
    return result

print(solution())