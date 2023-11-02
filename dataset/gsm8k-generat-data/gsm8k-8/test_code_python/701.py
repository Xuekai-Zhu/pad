def solution():
    # Calculate the total number of slices of pizza
    total_slices = 3 * 12

    # Calculate the cost per slice of pizza
    cost_per_slice = 72 / total_slices

    # Calculate the cost of 5 slices
    cost_of_5_slices = cost_per_slice * 5
    result = cost_of_5_slices
    return result

print(solution())