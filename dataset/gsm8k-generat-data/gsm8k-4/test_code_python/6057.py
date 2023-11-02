def solution():
    """A tree on a farm has 10 branches. Each branch has 40 sub-branches with 60 leaves each. If the total number of trees on the farm is 4 and they have the same number of leaves, calculate the total number of leaves on all the trees."""
    # Define the number of branches, sub-branches, and leaves per sub-branch on one tree
    branches = 10
    sub_branches = 40
    leaves_per_subbranch = 60

    # Calculate the total number of leaves on one tree
    total_leaves_per_tree = branches * sub_branches * leaves_per_subbranch

    # Calculate the total number of leaves on all four trees
    total_leaves = total_leaves_per_tree * 4

    result = total_leaves
    return result

print(solution())