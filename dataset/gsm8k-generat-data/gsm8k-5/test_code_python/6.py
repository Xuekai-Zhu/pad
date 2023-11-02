def solution():
    # Calculate the total number of slices of pizza
    num_large_slices = 2 * 16  # Each large pizza has 16 slices, and he bought 2
    num_small_slices = 2 * 8  # Each small pizza has 8 slices, and he bought 2
    total_slices = num_large_slices + num_small_slices  # The total number of pizza slices

    result = total_slices
    return result

print(solution())