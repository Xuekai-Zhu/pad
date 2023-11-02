def solution():
    """Amiyah is cutting some trees to build a cow shade. For every tree she cuts, she plants 5 new trees. If there were 400 trees on her farm and she cut 20% of them, calculate the total number of trees on the farm."""
    # Define the initial number of trees on the farm
    total_trees = 400

    # Calculate the number of trees Amiyah cut
    trees_cut = total_trees * 0.2

    # Calculate the number of trees Amiyah planted
    trees_planted = trees_cut * 5

    # Calculate the final number of trees on the farm
    final_trees = total_trees - trees_cut + trees_planted

    # Display the final number of trees
    result = final_trees
    return result

print(solution())