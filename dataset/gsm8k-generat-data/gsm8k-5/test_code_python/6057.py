def solution():
    # Calculate the total number of leaves on one tree
    leaves_per_subbranch = 60  # Each sub-branch has 60 leaves
    subbranches_per_branch = 40  # Each branch has 40 sub-branches
    leaves_per_branch = leaves_per_subbranch * subbranches_per_branch  # Total leaves per branch
    total_leaves_one_tree = leaves_per_branch * 10  # There are 10 branches on each tree

    # Calculate the total number of leaves on all the trees
    total_trees = 4  # There are 4 trees on the farm
    total_leaves_all_trees = total_leaves_one_tree * total_trees
    result = total_leaves_all_trees
    return result

print(solution())