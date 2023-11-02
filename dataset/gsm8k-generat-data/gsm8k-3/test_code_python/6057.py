def solution():
    """A tree on a farm has 10 branches. Each branch has 40 sub-branches with 60 leaves each. If the total number of trees on the farm is 4 and they have the same number of leaves, calculate the total number of leaves on all the trees."""
    # Calculate the total number of leaves on each tree
    leaves_per_branch = 40 * 60
    total_leaves_per_tree = 10 * leaves_per_branch

    # Calculate the total number of leaves on all the trees
    num_trees = 4
    total_leaves = num_trees * total_leaves_per_tree

    # Display the total number of leaves
    result = total_leaves
    return result

print(solution())