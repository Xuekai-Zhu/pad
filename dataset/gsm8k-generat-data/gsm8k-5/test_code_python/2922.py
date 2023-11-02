def solution():
    basil_leaves = 12  # Sabrina needs 12 basil leaves
    sage_leaves = basil_leaves / 2  # Sabrina needs twice as many basil leaves as sage leaves
    verbena_leaves = sage_leaves + 5  # Sabrina needs 5 more verbena leaves than sage leaves

    # Calculate the total number of leaves Sabrina needs
    total_leaves = basil_leaves + sage_leaves + verbena_leaves
    result = total_leaves
    return result

print(solution())