def solution():
    """There are 350 trees in the park, 70% of which are pine trees. How many are not pine trees?"""
    total_trees = 350
    pine_trees = 0.7 * total_trees
    non_pine_trees = total_trees - pine_trees
    result = non_pine_trees
    return result

print(solution())