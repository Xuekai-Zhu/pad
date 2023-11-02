def solution():
    fence_length = 25  # yards
    tree_width = 1.5  # feet
    tree_cost = 8.0

    # Convert fence length from yards to feet
    fence_length_feet = fence_length * 3

    # Calculate the number of trees needed to cover the fence length
    num_trees = fence_length_feet / tree_width

    # Round up to the nearest whole number of trees
    num_trees = math.ceil(num_trees)

    # Calculate the total cost of all tree saplings
    total_cost = num_trees * tree_cost
    result = total_cost
    return result

print(solution())