def solution():
    # Calculate the number of pink trees
    pink_trees = 42/3

    # Calculate the number of red trees
    red_trees = 2

    # Calculate the number of white trees
    white_trees = 42 - pink_trees - red_trees

    result = white_trees
    return result

print(solution())