def solution():
    # Calculate the total number of leaves on one tree
    leaves_per_branch = 40 * 60  # each branch has 40 sub-branches with 60 leaves each
    leaves_per_tree = leaves_per_branch * 10  # the tree has 10 branches
    # Calculate the total number of leaves on all four trees
    total_leaves = leaves_per_tree * 4
    result = total_leaves
    return result

print(solution())