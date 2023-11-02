def solution():
    
    initial_trees = 2 * 4 
    trees_planted = 15 - 10 
    trees_total = initial_trees + trees_planted * 4 
    trees_total *= 2 
    result = trees_total
    return result

print(solution())