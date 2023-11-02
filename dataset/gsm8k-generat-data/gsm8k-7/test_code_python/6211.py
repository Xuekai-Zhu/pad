def solution():
    jane_height = 1.5
    jane_shadow = 0.5
    tree_shadow = 10

    # Calculate the height of the tree using proportions
    tree_height = jane_height * (tree_shadow / jane_shadow)
    result = tree_height
    return result

print(solution())