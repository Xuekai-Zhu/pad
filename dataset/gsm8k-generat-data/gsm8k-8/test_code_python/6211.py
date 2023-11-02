def solution():
    # Define the given values
    jane_height = 1.5
    jane_shadow = 0.5
    tree_shadow = 10

    # Calculate the height of the tree
    tree_height = (jane_height / jane_shadow) * tree_shadow
    result = tree_height
    return result

print(solution())