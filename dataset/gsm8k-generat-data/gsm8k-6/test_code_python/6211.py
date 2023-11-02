def solution():
    # Use proportions to calculate the height of the tree
    tree_shadow = 10  # meters
    jane_shadow = 0.5  # meters
    jane_height = 1.5  # meters
    tree_height = (tree_shadow / jane_shadow) * jane_height  # height of the tree in meters
    result = tree_height
    return result

print(solution())