def solution():
    apple_trees_width = 10  # Each apple tree will be 10 feet wide
    apple_trees_spacing = 12  # There should be 12 feet between each apple tree
    peach_trees_width = 12  # Each peach tree will be 12 feet wide
    peach_trees_spacing = 15  # There should be 15 feet between each peach tree

    # Calculate the space required for the apple trees
    total_apple_width = 2 * apple_trees_width  # Two apple trees will be planted
    total_apple_spacing = 1 * apple_trees_spacing  # There will be only one spacing between the apple trees
    total_apple_space = total_apple_width + total_apple_spacing

    # Calculate the space required for the peach trees
    total_peach_width = 2 * peach_trees_width  # Two peach trees will be planted
    total_peach_spacing = 1 * peach_trees_spacing  # There will be only one spacing between the peach trees
    total_peach_space = total_peach_width + total_peach_spacing

    # Calculate the total space required for all trees
    total_space = total_apple_space + total_peach_space
    result = total_space
    return result

print(solution())