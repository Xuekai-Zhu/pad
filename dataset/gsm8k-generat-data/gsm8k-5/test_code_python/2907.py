def solution():
    total_trees = 350
    pine_trees = total_trees * 0.7

    # Calculate the number of trees that are not pine trees
    not_pine_trees = total_trees - pine_trees
    result = not_pine_trees
    return result

print(solution())