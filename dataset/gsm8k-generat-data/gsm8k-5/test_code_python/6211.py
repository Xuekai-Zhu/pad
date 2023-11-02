def solution():
    tree_shadow = 10  # Shadow of the tree is 10 meters
    jane_shadow = 0.5  # Shadow of Jane is 0.5 meters
    jane_height = 1.5  # Jane's height is 1.5 meters

    # Calculate the height of the tree using similar triangles
    tree_height = (tree_shadow / jane_shadow) * jane_height
    result = tree_height
    return result

print(solution())