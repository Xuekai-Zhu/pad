def solution():
    """Amiyah is cutting some trees to build a cow shade. For every tree she cuts, she plants 5 new trees. If there were 400 trees on her farm and she cut 20% of them, calculate the total number of trees on the farm."""
    # Define the initial number of trees
    initial_trees = 400

    # Calculate the number of trees Amiyah cut
    cut_trees = initial_trees * 0.2

    # Calculate the number of trees Amiyah planted after cutting the trees
    planted_trees = cut_trees * 5

    # Calculate the total number of trees on the farm
    total_trees = initial_trees - cut_trees + planted_trees

    # return the result
    result = total_trees
    return result

print(solution())