def solution():
    """A tree on a farm has 10 branches. Each branch has 40 sub-branches with 60 leaves each. If the total number of trees on the farm is 4 and they have the same number of leaves, calculate the total number of leaves on all the trees."""
    branches_per_tree = 10
    subbranches_per_branch = 40
    leaves_per_subbranch = 60
    leaves_per_branch = subbranches_per_branch * leaves_per_subbranch
    leaves_per_tree = branches_per_tree * leaves_per_branch
    total_leaves = leaves_per_tree * 4
    result = total_leaves
    return result

print(solution())