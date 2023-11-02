def solution():
    total_trees = 42
    red_trees = 2
    pink_trees = total_trees // 3 # integer division
    white_trees = total_trees - red_trees - pink_trees
    result = white_trees
    return result

print(solution())