def solution():
    # Calculate the number of twigs that sprout 4 leaves
    sprout_4 = round(0.3 * 90)  # 30% of the twigs sprout 4 leaves

    # Calculate the number of twigs that sprout 5 leaves
    sprout_5 = 90 - sprout_4

    # Calculate the total number of leaves on the tree
    total_leaves = (sprout_4 * 4) + (sprout_5 * 5)

    result = total_leaves
    return result

print(solution())