def solution():
    # Calculate the total number of twigs on the tree
    total_twigs = 30 * 90

    # Calculate the number of twigs that sprout 4 leaves
    sprout_4_leaves = 0.3 * total_twigs

    # Calculate the number of twigs that sprout 5 leaves
    sprout_5_leaves = 0.7 * total_twigs

    # Calculate the total number of leaves
    total_leaves = (sprout_4_leaves * 4) + (sprout_5_leaves * 5)
    result = total_leaves
    return result

print(solution())