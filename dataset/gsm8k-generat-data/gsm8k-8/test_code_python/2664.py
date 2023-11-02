def solution():
    # Calculate the total number of pizza slices
    total_slices = 4 * 12

    # Subtract the number of slices eaten by the guests
    slices_left = total_slices - 39

    result = slices_left
    return result

print(solution())