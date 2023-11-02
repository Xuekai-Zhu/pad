def solution():
    
    Hassan_apple_trees = 1
    Hassan_orange_trees = 2
    Ahmed_orange_trees = 8
    Ahmed_apple_trees = 4 * Hassan_apple_trees
    total_Hassan_trees = Hassan_apple_trees + Hassan_orange_trees
    total_Ahmed_trees = Ahmed_apple_trees + Ahmed_orange_trees
    difference = total_Ahmed_trees - total_Hassan_trees
    result = difference
    return result

print(solution())