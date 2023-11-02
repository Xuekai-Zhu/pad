def solution():
    num_apple_trees = 2 
    apple_tree_width = 10
    apple_tree_spacing = 12

    num_peach_trees = 2 
    peach_tree_width = 12
    peach_tree_spacing = 15

    # Calculate the total width of the apple trees
    total_apple_width = num_apple_trees * apple_tree_width

    # Calculate the spacing needed for the apple trees
    total_apple_spacing = (num_apple_trees - 1) * apple_tree_spacing
    
    # Calculate the total width of the peach trees
    total_peach_width = num_peach_trees * peach_tree_width

    # Calculate the spacing needed for the peach trees
    total_peach_spacing = (num_peach_trees - 1) * peach_tree_spacing

    # Calculate the total space needed for all the trees
    total_space = total_apple_width + total_apple_spacing + total_peach_width + total_peach_spacing
    result = total_space
    return result

print(solution())