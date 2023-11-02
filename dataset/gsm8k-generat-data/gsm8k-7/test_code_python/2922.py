def solution():
    num_basil_leaves = 12

    # Calculate the number of sage leaves Sabrina needs
    num_sage_leaves = num_basil_leaves / 2

    # Calculate the number of verbena leaves Sabrina needs
    num_verbena_leaves = num_sage_leaves + 5

    # Calculate the total number of leaves Sabrina needs
    total_leaves = num_basil_leaves + num_sage_leaves + num_verbena_leaves
    result = total_leaves
    return result

print(solution())