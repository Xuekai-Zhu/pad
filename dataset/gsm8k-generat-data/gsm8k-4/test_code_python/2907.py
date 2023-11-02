def solution():
    """There are 350 trees in the park, 70% of which are pine trees. How many are not pine trees?"""
    # Define the total number of trees
    total_trees = 350
    # Calculate the number of pine trees
    pine_trees = total_trees * 0.7
    # Calculate the number of non-pine trees
    nonpine_trees = total_trees - pine_trees
    result = nonpine_trees
    return result

print(solution())