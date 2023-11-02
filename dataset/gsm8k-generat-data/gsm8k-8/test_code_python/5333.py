def solution():
    # Calculate the total number of slices
    total_slices = 5 * 20

    # Calculate the number of slices that will be cut into smaller pieces
    smaller_slices = total_slices / 2

    # Calculate the total number of pieces
    total_pieces = total_slices + (smaller_slices * 3)
    result = total_pieces
    return result

print(solution())