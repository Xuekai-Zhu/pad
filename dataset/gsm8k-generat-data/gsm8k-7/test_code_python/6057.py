def solution():
    num_branches = 10
    num_subbranches = 40
    num_leaves_per_subbranch = 60
    num_trees = 4

    # Calculate the total number of leaves on one tree
    total_leaves_per_tree = num_branches * num_subbranches * num_leaves_per_subbranch

    # Calculate the total number of leaves on all trees
    total_leaves_all_trees = total_leaves_per_tree * num_trees
    result = total_leaves_all_trees
    return result

print(solution())