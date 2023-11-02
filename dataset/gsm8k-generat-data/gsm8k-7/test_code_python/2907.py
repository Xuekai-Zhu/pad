def solution():
    total_trees = 350
    pine_percentage = 0.7

    # Calculate the number of pine trees
    num_pine_trees = total_trees * pine_percentage

    # Calculate the number of non-pine trees
    num_non_pine_trees = total_trees - num_pine_trees

    result = num_non_pine_trees
    return result

print(solution())