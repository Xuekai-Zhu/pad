def solution():
    num_branches = 30
    num_twigs_per_branch = 90
    sprout_percentage = 0.3
    four_leaves = 4
    five_leaves = 5

    # Calculate the total number of twigs on the tree
    total_twigs = num_branches * num_twigs_per_branch

    # Calculate the number of sprouted twigs
    sprouted_twigs = total_twigs * sprout_percentage

    # Calculate the number of leaves on the four-leafed twigs
    num_four_leaves = sprouted_twigs * four_leaves

    # Calculate the number of leaves on the five-leafed twigs
    num_five_leaves = (total_twigs - sprouted_twigs) * five_leaves

    # Calculate the total number of leaves on the tree
    total_leaves = num_four_leaves + num_five_leaves
    result = total_leaves
    return result

print(solution())