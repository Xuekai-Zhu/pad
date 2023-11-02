def solution():
    """James has a small tree outside his window with 30 branches with 90 twigs per branch. 30% of the twigs sprout 4 leaves and the rest sprout 5 leaves. How many leaves are on the tree total?"""
    branches = 30
    twigs_per_branch = 90
    total_twigs = branches * twigs_per_branch
    sprout_4_leaves = 0.3 * total_twigs
    sprout_5_leaves = 0.7 * total_twigs
    total_leaves = (sprout_4_leaves * 4) + (sprout_5_leaves * 5)
    result = total_leaves
    return result

print(solution())