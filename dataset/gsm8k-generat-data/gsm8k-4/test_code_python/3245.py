def solution():
    """James has a small tree outside his window with 30 branches with 90 twigs per branch. 30% of the twigs sprout 4 leaves and the rest sprout 5 leaves. How many leaves are on the tree total?"""
    # Define the number of branches and twigs per branch
    branches = 30
    twigs_per_branch = 90

    # Calculate the total number of twigs
    total_twigs = branches * twigs_per_branch

    # Calculate the number of twigs sprouting 4 leaves and 5 leaves, respectively
    sprout_4_leaves = total_twigs * 0.3
    sprout_5_leaves = total_twigs - sprout_4_leaves

    # Calculate the total number of leaves
    total_leaves = (sprout_4_leaves * 4) + (sprout_5_leaves * 5)

    # return the result
    result = total_leaves
    return result

print(solution())