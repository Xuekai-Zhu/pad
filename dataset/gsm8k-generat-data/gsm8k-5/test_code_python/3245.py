def solution():
    # Calculate the total number of twigs on the tree
    total_twigs = 30 * 90  # 30 branches with 90 twigs per branch

    # Calculate the number of twigs that sprout 4 leaves and the number that sprout 5 leaves
    sprout_4 = int(0.3 * total_twigs)  # 30% of the twigs sprout 4 leaves
    sprout_5 = total_twigs - sprout_4  # The rest sprout 5 leaves

    # Calculate the total number of leaves on the tree
    total_leaves = (4 * sprout_4) + (5 * sprout_5)

    result = total_leaves
    return result

print(solution())