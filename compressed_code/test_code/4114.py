def solution():
    
    total_trees = 42
    pink_trees = total_trees // 3
    red_trees = 2
    white_trees = total_trees - pink_trees - red_trees
    result = white_trees
    return result

print(solution())