def solution():
    fence_length = 25  # The length of the fence is 25 yards
    tree_width = 1.5/3  # The trees are 1.5 feet wide, which is 1/3 yard
    number_of_trees = fence_length / tree_width  # Calculate the number of trees needed
    cost_per_tree = 8.00  # The trees are on sale for $8.00 each

    # Calculate the total cost of the trees
    total_cost = number_of_trees * cost_per_tree
    result = total_cost
    return result

print(solution())