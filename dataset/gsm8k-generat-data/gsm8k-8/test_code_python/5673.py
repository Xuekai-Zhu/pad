def solution():
    # Define John and Sam's slices eaten
    john_slices = 3
    sam_slices = 2 * john_slices

    # Calculate total slices eaten
    total_slices_eaten = john_slices + sam_slices

    # Calculate slices remaining
    slices_remaining = 12 - total_slices_eaten
    result = slices_remaining
    return result

print(solution())