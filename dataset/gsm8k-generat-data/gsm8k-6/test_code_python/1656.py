def solution():
    # Convert fence length to feet
    fence_length = 25 * 3  # 1 yard = 3 feet

    # Determine number of trees needed
    tree_width = 1.5  # in feet
    total_width = fence_length / tree_width
    num_trees = int(total_width)  # round down to nearest whole number

    # Calculate total cost of trees
    cost_per_tree = 8.00
    total_cost = num_trees * cost_per_tree

    result = total_cost
    return result

print(solution())