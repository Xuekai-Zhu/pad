def solution():
    # Calculate the total number of leaves on one branch
    leaves_per_branch = 40 * 60

    # Calculate the total number of leaves on one tree
    leaves_per_tree = leaves_per_branch * 10

    # Calculate the total number of leaves on all the trees
    total_leaves = leaves_per_tree * 4
    result = total_leaves
    return result

print(solution())